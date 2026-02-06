#!/usr/bin/env python3
"""
Calculate MAE, RMSE, R² on proper train/test split for thesis.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import warnings
import time

warnings.filterwarnings('ignore')

# Configuration
DATA_PATH = '/home/kangah/Desktop/remotesensing/10_years/Data/data_17_params_final_XYTableToPoint_TableToExcel.csv'

print("="*70)
print("CALCULATING MODEL METRICS FOR THESIS")
print("="*70)

# 1. Load Data
print("\n[1/5] Loading data...")
csv_data = pd.read_csv(DATA_PATH)
print(f"Data shape: {csv_data.shape}")

# 2. Rename columns
csv_data = csv_data.rename(columns={
    'X': 'long', 'Y': 'lat', 'VEL': 'Velocity',
    'Geology_EB': 'Geology', 'EBR_NLCD_2': 'LULC',
    'twi_btr': 'Top_Wetness_Index', 'Precipitat': 'Precipitation',
    'dis_rail': 'Distance_from_railway', 'dista_brid': 'Distance_from_bridge',
    'dis_fr_rd_btr': 'Distance_from_road',
    'aspect_btr': 'Aspect', 'slope': 'Slope', 'elevation_': 'DEM',
    'Dist_River': 'Distance_from_river', 'Dist_Fault': 'Distance_From_Fault',
})

# 3. Feature Engineering
print("\n[2/5] Feature engineering...")
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

# 4. Prepare Data with train/test split
print("\n[3/5] Preparing data with 80/20 train/test split...")
X = csv_data[feature_cols].fillna(csv_data[feature_cols].median())
y = csv_data['Velocity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {X_train.shape[0]} samples")
print(f"Test:  {X_test.shape[0]} samples")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Models and calculate metrics
print("\n[4/5] Training models and calculating metrics...")

# Extra Trees
print("\nTraining Extra Trees...")
start_time = time.time()
et_model = ExtraTreesRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
)
et_model.fit(X_train_scaled, y_train)
et_train_time = time.time() - start_time
et_predictions = et_model.predict(X_test_scaled)

et_r2 = r2_score(y_test, et_predictions)
et_rmse = np.sqrt(mean_squared_error(y_test, et_predictions))
et_mae = mean_absolute_error(y_test, et_predictions)
print(f"✓ Extra Trees: R²={et_r2:.4f}, RMSE={et_rmse:.4f}, MAE={et_mae:.4f}, Time={et_train_time:.1f}s")

# Random Forest
print("\nTraining Random Forest...")
start_time = time.time()
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train_scaled, y_train)
rf_train_time = time.time() - start_time
rf_predictions = rf_model.predict(X_test_scaled)

rf_r2 = r2_score(y_test, rf_predictions)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_predictions))
rf_mae = mean_absolute_error(y_test, rf_predictions)
print(f"✓ Random Forest: R²={rf_r2:.4f}, RMSE={rf_rmse:.4f}, MAE={rf_mae:.4f}, Time={rf_train_time:.1f}s")

# 6. Print results for thesis
print("\n" + "="*70)
print("METRICS FOR THESIS (Test Set Performance)")
print("="*70)

print(f"""
┌─────────────────┬─────────┬─────────────────┬─────────────────┬──────────────────┐
│ Model           │ R²      │ RMSE (mm/yr)    │ MAE (mm/yr)     │ Training Time(s) │
├─────────────────┼─────────┼─────────────────┼─────────────────┼──────────────────┤
│ Extra Trees     │ {et_r2:.4f}  │ {et_rmse:.4f}           │ {et_mae:.4f}           │ {et_train_time:.1f}              │
│ Random Forest   │ {rf_r2:.4f}  │ {rf_rmse:.4f}           │ {rf_mae:.4f}           │ {rf_train_time:.1f}              │
└─────────────────┴─────────┴─────────────────┴─────────────────┴──────────────────┘
""")

print("\nFor LaTeX table:")
print(f"Extra Trees    & {et_r2:.4f} & {et_rmse:.2f} & {et_mae:.2f} & {et_train_time:.0f} \\\\")
print(f"Random Forest  & {rf_r2:.4f} & {rf_rmse:.2f} & {rf_mae:.2f} & {rf_train_time:.0f} \\\\")

# Save metrics to file for reference
metrics_df = pd.DataFrame({
    'Model': ['Extra Trees', 'Random Forest'],
    'R2': [et_r2, rf_r2],
    'RMSE_mm_yr': [et_rmse, rf_rmse],
    'MAE_mm_yr': [et_mae, rf_mae],
    'Training_Time_s': [et_train_time, rf_train_time]
})
metrics_df.to_csv('/home/kangah/Desktop/MasterThesisLsu/model_metrics.csv', index=False)
print("\nMetrics saved to: model_metrics.csv")
