#!/usr/bin/env python3
"""
Compute binarized AUC-ROC for ET and RF susceptibility models.
Uses existing predictions from velocity_predictions.csv (the same models
that produced ET R²=0.9251 and RF R²=0.8825 in the thesis).
Binary label: subsidence (velocity < 0) vs non-subsidence (velocity >= 0).
"""

import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc, r2_score
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# ── Load existing predictions ──
csv_path = '/home/kangah/Desktop/remotesensing/10_years/suitability/all_analysis_files_lime and MDI/velocity_predictions.csv'
df = pd.read_csv(csv_path)
print(f"Loaded {len(df)} rows")
print(f"Columns: {list(df.columns)}")

y_actual = df['Actual_Velocity_mm_yr'].values
y_pred_et = df['ET_Predicted_Velocity_mm_yr'].values
y_pred_rf = df['RF_Predicted_Velocity_mm_yr'].values

# ── Verify R² matches thesis ──
print(f"\nRegression metrics (full dataset):")
print(f"  ET  R² = {r2_score(y_actual, y_pred_et):.4f}")
print(f"  RF  R² = {r2_score(y_actual, y_pred_rf):.4f}")

# ── Binarize: subsidence (velocity < 0) = 1, non-subsidence = 0 ──
y_binary = (y_actual < 0).astype(int)
print(f"\nClass distribution:")
print(f"  Subsidence (vel < 0):     {y_binary.sum()} ({y_binary.mean()*100:.1f}%)")
print(f"  Non-subsidence (vel >= 0): {(1-y_binary).sum()} ({(1-y_binary.mean())*100:.1f}%)")

# Score: negative predicted velocity (more negative → higher subsidence probability)
score_et = -y_pred_et
score_rf = -y_pred_rf

# ── Compute ROC curves ──
fpr_et, tpr_et, _ = roc_curve(y_binary, score_et)
auc_et = auc(fpr_et, tpr_et)

fpr_rf, tpr_rf, _ = roc_curve(y_binary, score_rf)
auc_rf = auc(fpr_rf, tpr_rf)

print(f"\nBinarized AUC-ROC (threshold = 0 mm/yr):")
print(f"  ET  AUC = {auc_et:.4f}")
print(f"  RF  AUC = {auc_rf:.4f}")

# ── Export ROC data for gnuplot ──
base = '/home/kangah/Desktop/MasterThesisLsu/media'
np.savetxt(f'{base}/roc_et.dat', np.column_stack([fpr_et, tpr_et]), fmt='%.6f', header='FPR TPR')
np.savetxt(f'{base}/roc_rf.dat', np.column_stack([fpr_rf, tpr_rf]), fmt='%.6f', header='FPR TPR')
print(f"\nExported ROC data to {base}/roc_et.dat and roc_rf.dat")
