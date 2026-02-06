#!/usr/bin/env python3
"""
Regenerate SHAP plots with bold labels for thesis visibility.
Uses saved SHAP values if available, otherwise recomputes.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings
import gc
import os

warnings.filterwarnings('ignore')

# Set matplotlib to use bold fonts
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Configuration
SHAP_SAMPLE_SIZE = 500
BACKGROUND_SIZE = 50
DATA_PATH = '/home/kangah/Desktop/remotesensing/10_years/Data/data_17_params_final_XYTableToPoint_TableToExcel.csv'
SAVE_DIR = '/home/kangah/Desktop/MasterThesisLsu/media'

print("="*70)
print("REGENERATING SHAP PLOTS WITH BOLD LABELS")
print("="*70)

# 1. Load Data
print("\n[1/6] Loading data...")
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
print("\n[2/6] Feature engineering...")
csv_data['Fault_DEM'] = csv_data['Distance_From_Fault'] * csv_data['DEM']
csv_data['River_DEM'] = csv_data['Distance_from_river'] * csv_data['DEM']
csv_data['Slope_DEM'] = csv_data['Slope'] * csv_data['DEM']
csv_data['Fault_squared'] = csv_data['Distance_From_Fault'] ** 2
csv_data['DEM_squared'] = csv_data['DEM'] ** 2
csv_data['log_Fault'] = np.log1p(csv_data['Distance_From_Fault'])

feature_cols = [col for col in csv_data.columns
                if col not in ['long', 'lat', 'Velocity', 'OBJECTID'] and
                csv_data[col].dtype in ['int64', 'float64']]

print(f"Features ({len(feature_cols)}): {feature_cols}")

# 4. Prepare Data
print("\n[3/6] Preparing data...")
X = csv_data[feature_cols].fillna(csv_data[feature_cols].median())
y = csv_data['Velocity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Models
print("\n[4/6] Training models...")

print("Training Extra Trees...")
et_model = ExtraTreesRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
)
et_model.fit(X_train_scaled, y_train)
print("✓ Extra Trees trained")

print("Training Random Forest...")
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train_scaled, y_train)
print("✓ Random Forest trained")

# 6. SHAP Analysis with BOLD labels
print("\n[5/6] Computing SHAP values and generating plots with BOLD labels...")

np.random.seed(42)
sample_idx = np.random.choice(len(X_train_scaled), SHAP_SAMPLE_SIZE, replace=False)
X_sample = X_train_scaled[sample_idx]

# Extra Trees SHAP
print("\nComputing SHAP for Extra Trees...")
et_explainer = shap.TreeExplainer(et_model)
et_shap_values = et_explainer.shap_values(X_sample)

# ET Summary Plot with BOLD labels
fig, ax = plt.subplots(figsize=(12, 10))
shap.summary_plot(et_shap_values, X_sample, feature_names=feature_cols, show=False)
plt.title('SHAP Summary Plot - Extra Trees', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('SHAP value (impact on model output)', fontsize=14, fontweight='bold')
# Make y-axis labels bold
ax = plt.gca()
for label in ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(12)
for label in ax.get_xticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
plt.tight_layout()
plt.savefig(f'{SAVE_DIR}/shap_summary_et.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: shap_summary_et.png")

# ET Bar Plot with BOLD labels
fig, ax = plt.subplots(figsize=(12, 10))
mean_shap_et = np.abs(et_shap_values).mean(axis=0)
shap_df_et = pd.DataFrame({
    'Feature': feature_cols,
    'Mean |SHAP|': mean_shap_et
}).sort_values('Mean |SHAP|', ascending=True)

colors_et = plt.cm.tab20(np.linspace(0, 1, len(shap_df_et)))
bars = ax.barh(shap_df_et['Feature'], shap_df_et['Mean |SHAP|'], color=colors_et)
ax.set_xlabel('Mean |SHAP Value|', fontsize=14, fontweight='bold')
ax.set_ylabel('Feature', fontsize=14, fontweight='bold')
ax.set_title('SHAP Feature Importance - Extra Trees', fontsize=16, fontweight='bold', pad=20)
for label in ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
for label in ax.get_xticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
plt.tight_layout()
plt.savefig(f'{SAVE_DIR}/shap_bar_et.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: shap_bar_et.png")

del et_shap_values, et_explainer
gc.collect()

# Random Forest SHAP
print("\nComputing SHAP for Random Forest...")
rf_explainer = shap.TreeExplainer(rf_model)
rf_shap_values = rf_explainer.shap_values(X_sample)

# RF Summary Plot with BOLD labels
fig, ax = plt.subplots(figsize=(12, 10))
shap.summary_plot(rf_shap_values, X_sample, feature_names=feature_cols, show=False)
plt.title('SHAP Summary Plot - Random Forest', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('SHAP value (impact on model output)', fontsize=14, fontweight='bold')
ax = plt.gca()
for label in ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(12)
for label in ax.get_xticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
plt.tight_layout()
plt.savefig(f'{SAVE_DIR}/shap_summary_rf.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: shap_summary_rf.png")

# RF Bar Plot with BOLD labels
fig, ax = plt.subplots(figsize=(12, 10))
mean_shap_rf = np.abs(rf_shap_values).mean(axis=0)
shap_df_rf = pd.DataFrame({
    'Feature': feature_cols,
    'Mean |SHAP|': mean_shap_rf
}).sort_values('Mean |SHAP|', ascending=True)

colors_rf = plt.cm.tab20(np.linspace(0, 1, len(shap_df_rf)))
bars = ax.barh(shap_df_rf['Feature'], shap_df_rf['Mean |SHAP|'], color=colors_rf)
ax.set_xlabel('Mean |SHAP Value|', fontsize=14, fontweight='bold')
ax.set_ylabel('Feature', fontsize=14, fontweight='bold')
ax.set_title('SHAP Feature Importance - Random Forest', fontsize=16, fontweight='bold', pad=20)
for label in ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
for label in ax.get_xticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(11)
plt.tight_layout()
plt.savefig(f'{SAVE_DIR}/shap_bar_rf.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: shap_bar_rf.png")

print("\n" + "="*70)
print("[6/6] SHAP PLOTS WITH BOLD LABELS COMPLETE!")
print("="*70)
print(f"\nOutput files saved to: {SAVE_DIR}")
print("  - shap_summary_et.png")
print("  - shap_bar_et.png")
print("  - shap_summary_rf.png")
print("  - shap_bar_rf.png")
