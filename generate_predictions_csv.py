#!/usr/bin/env python3
"""
Generate CSV table with actual velocity, ET predictions, RF predictions, and coordinates.
Uses the same model configuration as model_analysis_result.ipynb
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')

# Configuration - matching model_analysis_result.ipynb
DATA_PATH = '/home/kangah/Desktop/remotesensing/10_years/Data/data_17_params_final_XYTableToPoint_TableToExcel.csv'
OUTPUT_PATH = '/home/kangah/Desktop/MasterThesisLsu/velocity_predictions.csv'

print("="*70)
print("GENERATING VELOCITY PREDICTIONS CSV")
print("Using model configuration from model_analysis_result.ipynb")
print("="*70)

# 1. Load Data
print("\n[1/7] Loading data...")
csv_data = pd.read_csv(DATA_PATH)
print(f"Data shape: {csv_data.shape}")

# 2. Rename columns (matching notebook)
csv_data = csv_data.rename(columns={
    'X': 'long', 'Y': 'lat', 'VEL': 'Velocity',
    'Geology_EB': 'Geology', 'EBR_NLCD_2': 'LULC',
    'twi_btr': 'Top_Wetness_Index', 'Precipitat': 'Precipitation',
    'dis_rail': 'Distance_from_railway', 'dista_brid': 'Distance_from_bridge',
    'dis_fr_rd_btr': 'Distance_from_road',
    'aspect_btr': 'Aspect', 'slope': 'Slope', 'elevation_': 'DEM',
    'Dist_River': 'Distance_from_river', 'Dist_Fault': 'Distance_From_Fault',
})

# 3. Feature Engineering (matching notebook)
print("\n[2/7] Feature engineering...")
csv_data['Fault_DEM'] = csv_data['Distance_From_Fault'] * csv_data['DEM']
csv_data['River_DEM'] = csv_data['Distance_from_river'] * csv_data['DEM']
csv_data['Slope_DEM'] = csv_data['Slope'] * csv_data['DEM']
csv_data['Fault_squared'] = csv_data['Distance_From_Fault'] ** 2
csv_data['DEM_squared'] = csv_data['DEM'] ** 2
csv_data['log_Fault'] = np.log1p(csv_data['Distance_From_Fault'])

feature_cols = [col for col in csv_data.columns
                if col not in ['long', 'lat', 'Velocity', 'OBJECTID'] and
                csv_data[col].dtype in ['int64', 'float64']]

print(f"Features ({len(feature_cols)})")

# 4. Data Augmentation (matching notebook)
print("\n[3/7] Data augmentation...")

def augment_data(X, y, noise_factor=0.02, n_interpolations=1):
    """Augment data with Gaussian noise and interpolation"""
    X_aug = [X.copy()]
    y_aug = [y.copy()]
    
    # Gaussian noise augmentation
    for _ in range(2):
        X_noisy = X.copy()
        for col in X.columns:
            noise = np.random.normal(0, noise_factor * X[col].std(), len(X))
            X_noisy[col] = X[col] + noise
        X_aug.append(X_noisy)
        y_aug.append(y.copy())
    
    # SMOTE-like interpolation
    np.random.seed(42)
    n_samples = len(X)
    for _ in range(n_interpolations):
        idx1 = np.random.choice(n_samples, n_samples)
        idx2 = np.random.choice(n_samples, n_samples)
        alpha = np.random.uniform(0.3, 0.7, n_samples)
        
        X_interp = pd.DataFrame(index=range(n_samples), columns=X.columns)
        for col in X.columns:
            X_interp[col] = alpha * X.iloc[idx1][col].values + (1 - alpha) * X.iloc[idx2][col].values
        y_interp = pd.Series(alpha * y.iloc[idx1].values + (1 - alpha) * y.iloc[idx2].values)
        
        X_aug.append(X_interp)
        y_aug.append(y_interp)
    
    return pd.concat(X_aug, ignore_index=True), pd.concat(y_aug, ignore_index=True)

# Prepare data
X = csv_data[feature_cols].fillna(csv_data[feature_cols].median())
y = csv_data['Velocity']
coords = csv_data[['long', 'lat']].copy()

# Split BEFORE augmentation (matching notebook)
X_train_orig, X_test, y_train_orig, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
test_indices = X_test.index

# Augment training data only
X_train_aug, y_train_aug = augment_data(X_train_orig, y_train_orig)
print(f"Augmented training data: {len(X_train_aug)} samples ({len(X_train_aug)/len(X_train_orig):.1f}x original)")

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_aug)
X_test_scaled = scaler.transform(X_test)
X_all_scaled = scaler.transform(X)

# 5. Train Models (memory-efficient version)
print("\n[4/7] Training models (memory-efficient: 200 estimators)...")

import gc

print("Training Extra Trees...")
et_model = ExtraTreesRegressor(
    n_estimators=200,
    max_depth=30,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=4  # Limit parallel jobs to save RAM
)
et_model.fit(X_train_scaled, y_train_aug)
print("✓ Extra Trees trained")
gc.collect()

print("Training Random Forest...")
rf_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=25,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=4  # Limit parallel jobs to save RAM
)
rf_model.fit(X_train_scaled, y_train_aug)
print("✓ Random Forest trained")
gc.collect()

# 6. Generate predictions for ALL locations
print("\n[5/7] Generating predictions for all locations...")
et_predictions = et_model.predict(X_all_scaled)
rf_predictions = rf_model.predict(X_all_scaled)

# 7. Calculate test set metrics
print("\n[6/7] Calculating test set metrics...")
et_test_pred = et_model.predict(X_test_scaled)
rf_test_pred = rf_model.predict(X_test_scaled)

et_r2 = r2_score(y_test, et_test_pred)
et_rmse = np.sqrt(mean_squared_error(y_test, et_test_pred))
et_mae = mean_absolute_error(y_test, et_test_pred)

rf_r2 = r2_score(y_test, rf_test_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_test_pred))
rf_mae = mean_absolute_error(y_test, rf_test_pred)

print(f"Extra Trees  - R²: {et_r2:.4f}, RMSE: {et_rmse:.4f}, MAE: {et_mae:.4f}")
print(f"Random Forest - R²: {rf_r2:.4f}, RMSE: {rf_rmse:.4f}, MAE: {rf_mae:.4f}")

# 8. Create output DataFrame
print("\n[7/7] Creating CSV file...")
output_df = pd.DataFrame({
    'Longitude': coords['long'],
    'Latitude': coords['lat'],
    'Actual_Velocity_mm_yr': y,
    'ET_Predicted_Velocity_mm_yr': et_predictions,
    'RF_Predicted_Velocity_mm_yr': rf_predictions,
    'ET_Residual_mm_yr': y.values - et_predictions,
    'RF_Residual_mm_yr': y.values - rf_predictions
})

# Round to 4 decimal places
output_df = output_df.round(4)

# Save to CSV
output_df.to_csv(OUTPUT_PATH, index=False)

print("\n" + "="*70)
print("CSV GENERATION COMPLETE!")
print("="*70)
print(f"\nOutput file: {OUTPUT_PATH}")
print(f"Total locations: {len(output_df)}")
print(f"\nColumns:")
for col in output_df.columns:
    print(f"  - {col}")

print(f"\nTest Set Performance (matches notebook):")
print(f"  Extra Trees:   R²={et_r2:.4f}, RMSE={et_rmse:.2f} mm/yr, MAE={et_mae:.2f} mm/yr")
print(f"  Random Forest: R²={rf_r2:.4f}, RMSE={rf_rmse:.2f} mm/yr, MAE={rf_mae:.2f} mm/yr")

print(f"\nFirst 5 rows:")
print(output_df.head().to_string(index=False))
