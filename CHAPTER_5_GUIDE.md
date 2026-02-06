# CHAPTER 5 QUICK REFERENCE GUIDE

## STRUCTURE OVERVIEW

**Total Sections**: 6 main sections  
**Total Subsections**: 21 subsections  
**Estimated Length**: 25-30 pages  
**Required Figures**: 15-18  
**Required Tables**: 2

---

## SECTION BREAKDOWN

### 5.1 SBAS-InSAR Deformation Analysis (4-5 pages)
- **5.1.1** Spatial Distribution of Subsidence Velocity
- **5.1.2** Temporal Evolution of Deformation
- **5.1.3** Validation Against GNSS Measurements
- **5.1.4** Discussion: Observed Subsidence Patterns

**Key Points to Include:**
- Mean velocity, std dev, min/max values
- Spatial hotspot identification
- Temporal trends (linear/non-linear)
- GNSS comparison (1LSU and GMVS)
- Physical interpretation of patterns

---

### 5.2 Spatial Susceptibility Mapping (5-6 pages)
- **5.2.1** Model Training and Performance Comparison
- **5.2.2** Subsidence Susceptibility Maps
- **5.2.3** Discussion: Model Selection and Spatial Predictions

**Key Points to Include:**
- ET vs RF performance (R² = 0.9063 vs 0.8037)
- Statistical significance (p < 0.001)
- Susceptibility map description
- High/moderate/low risk zones (km² and %)
- Urban planning implications

---

### 5.3 Feature Importance (5-6 pages)
- **5.3.1** MDI Analysis
- **5.3.2** SHAP Value Analysis
- **5.3.3** LIME Local Explanations
- **5.3.4** Discussion: Physical Interpretation

**Key Points to Include:**
- Top 5 features: LULC, faults, River_DEM, DEM, wells
- SHAP values for each feature
- Nonlinear relationships (fault <1km threshold)
- LIME examples for high/moderate/low risk
- Comparison with other cities

---

### 5.4 Temporal Forecasting (6-7 pages)
- **5.4.1** Model Training and Validation Performance
- **5.4.2** Subsidence Forecasts to 2030
- **5.4.3** Uncertainty Analysis
- **5.4.4** Discussion: Forecast Reliability

**Key Points to Include:**
- Performance: R²=0.9368, r=0.9723, NSE=0.93XX
- 2030 forecast: -0.530 mm/yr mean velocity
- Cumulative displacement: -6.42 mm
- Constrained vs unconstrained comparison
- Uncertainty quantification and sources

---

### 5.5 Integrated Assessment (3-4 pages)
- **5.5.1** Consistency Between Susceptibility and Forecast
- **5.5.2** Comparison with Previous EBRP Studies
- **5.5.3** Implications for Urban Planning

**Key Points to Include:**
- Spatial correlation between ET and LSTM
- Comparison with Abdalla2024, Zou2016
- Urban planning recommendations
- Infrastructure management strategies
- Groundwater management needs
- Flood risk considerations

---

### 5.6 Limitations (2-3 pages)
- **5.6.1** InSAR-Related Limitations
- **5.6.2** Machine Learning Model Limitations
- **5.6.3** Temporal Forecasting Limitations
- **5.6.4** Validation Limitations
- **5.6.5** Future Improvements

**Key Points to Include:**
- Honest assessment of all limitations
- Decorrelation, atmospheric effects, reference frame
- Model assumptions and extrapolation issues
- Limited validation period (2 years)
- Future improvement suggestions

---

## REQUIRED FIGURES (15-18 total)

### Section 5.1 (3-4 figures)
1. **fig:velocity_map** - Mean velocity map (2017-2025)
2. **fig:timeseries** - Time-series at 5 representative locations
3. **fig:gnss_validation** - InSAR vs GNSS scatter plot
4. *(Optional)* Coherence map

### Section 5.2 (3 figures)
5. **fig:predicted_vs_observed** - ET vs RF scatter plots
6. **fig:susceptibility_map_et** - ET susceptibility map
7. **fig:susceptibility_comparison** - ET vs RF comparison + difference map

### Section 5.3 (4-5 figures)
8. **fig:mdi_importance** - Feature importance bar chart
9. **fig:shap_summary** - SHAP beeswarm plot
10. **fig:shap_fault** - SHAP dependence for faults
11. **fig:shap_river_dem** - SHAP dependence for River_DEM interaction
12. **fig:lime_examples** - LIME explanations for 3 locations

### Section 5.4 (4-5 figures)
13. **fig:lstm_validation** - Predicted vs observed + time-series
14. **fig:constraint_effect** - Constrained vs unconstrained
15. **fig:forecast_maps** - 2030 velocity forecast map
16. **fig:cumulative_displacement** - Cumulative displacement (2025-2030)
17. **fig:forecast_timeseries** - Forecast time-series at locations
18. **fig:uncertainty** - Uncertainty growth with horizon
19. *(Optional)* **fig:uncertainty_map** - Spatial uncertainty map

### Section 5.5 (1 figure)
20. **fig:spatial_temporal_consistency** - ET vs LSTM scatter

---

## REQUIRED TABLES (2 total)

### Section 5.2
- **tab:model_performance** - ET vs RF performance metrics

### Section 5.4
- **tab:lstm_performance** - LSTM validation metrics

---

## WRITING CHECKLIST FOR EACH SUBSECTION

- [ ] Start with transition sentence from previous subsection
- [ ] Present quantitative results with specific values
- [ ] Reference all figures and tables
- [ ] Provide physical interpretation
- [ ] Compare with literature where relevant
- [ ] Discuss implications
- [ ] End with bridge to next subsection

---

## FIGURE CREATION GUIDELINES

### Maps (velocity, susceptibility, forecast):
- **Size**: Full page width (0.9\textwidth)
- **Color scheme**: Diverging (blue-white-red for subsidence)
- **Include**: Scale bar, north arrow, legend
- **Overlay**: Infrastructure, faults, major features
- **Resolution**: 300 DPI minimum

### Scatter Plots (validation, comparison):
- **Size**: 0.7-0.9\textwidth
- **Include**: 1:1 line, R² value, RMSE
- **Color**: Density gradient or categories
- **Axes**: Clear labels with units

### Time-Series Plots:
- **Size**: 0.9\textwidth
- **Include**: Error bars or uncertainty bands
- **Legend**: Clear location labels
- **Axes**: Date format, velocity units

### Bar Charts (feature importance):
- **Size**: 0.8\textwidth
- **Orientation**: Horizontal (easier to read labels)
- **Include**: Error bars if available
- **Color**: Single color or categorical

### SHAP Plots:
- **Beeswarm**: 0.9\textwidth, show top 10-15 features
- **Dependence**: 0.7\textwidth, include interaction colors
- **Color bar**: Indicate feature values

---

## DATA YOU'LL NEED TO FILL IN

### From InSAR Processing:
- [ ] Mean velocity: _____ mm/yr
- [ ] Std dev: _____ mm/yr
- [ ] Max subsidence: _____ mm/yr
- [ ] Max uplift: _____ mm/yr
- [ ] Coherence percentage: _____%
- [ ] GNSS comparison: r = ____, RMSE = ____ mm/yr

### From ML Models:
- [ ] ET RMSE: _____ mm/yr
- [ ] ET MAE: _____ mm/yr
- [ ] RF RMSE: _____ mm/yr
- [ ] RF MAE: _____ mm/yr
- [ ] Training time: _____ seconds

### From Feature Importance:
- [ ] LULC importance: _____
- [ ] Fault importance: _____
- [ ] River_DEM importance: _____
- [ ] DEM importance: _____
- [ ] Well importance: _____

### From LSTM:
- [ ] LSTM RMSE: _____ mm/yr
- [ ] LSTM MAE: _____ mm/yr
- [ ] NSE: _____
- [ ] Number of training pixels: _____
- [ ] Number of epochs: _____
- [ ] MSE loss: _____

### From Forecasts:
- [ ] 2030 mean velocity: -0.530 mm/yr (from abstract)
- [ ] 2030 cumulative: -6.42 mm (from abstract)
- [ ] Deceleration percentage: _____%
- [ ] High-risk area: _____ km²
- [ ] Moderate-risk area: _____ km²
- [ ] Low-risk area: _____ km²

---

## DISCUSSION POINTS TO COVER

### 5.1 Discussion:
- Why subsidence occurs where it does
- Comparison with Houston, New Orleans, other Gulf Coast cities
- Relationship to aquifer extraction patterns
- Temporal stability vs change

### 5.2 Discussion:
- Why ET outperforms RF (random splits, multicollinearity)
- Spatial patterns match known drivers
- Urban planning implications
- Infrastructure risk zones

### 5.3 Discussion:
- LULC dominance (urbanization effects)
- Fault threshold behavior (1 km)
- Coupled processes (River_DEM interaction)
- Comparison with Hangzhou, Tehran, etc.
- Actionable mitigation strategies

### 5.4 Discussion:
- Physics constraints improve forecasts
- Stabilization trend is geomechanically consistent
- Spatial heterogeneity in deceleration
- Infrastructure implications
- Uncertainty sources and confidence

### 5.5 Discussion:
- Model consistency validates both approaches
- Extends previous EBRP studies
- Provides actionable recommendations
- Multiple stakeholder benefits

---

## RECOMMENDED CITATIONS TO INCLUDE

### In each section:
- **5.1**: Berardino2002, Ferretti2001, Abdalla2024, Higgins2016
- **5.2**: Geurts2006, HosseinzadehLLand2024
- **5.3**: Higgins2016, Abdalla2024, [other subsidence cities]
- **5.4**: Higgins2016, Raissi2019, Zhu2024, Mirmazloumi2023
- **5.5**: Abdalla2024, Zou2016, [EBRP studies]
- **5.6**: [relevant limitation citations]

---

## COMMON WRITING MISTAKES TO AVOID

❌ **Don't**: "The results show that..."  
✅ **Do**: "ET achieves R² = 0.9063..."

❌ **Don't**: Describe figures in detail  
✅ **Do**: Refer to figures, highlight key findings

❌ **Don't**: Repeat methods  
✅ **Do**: Focus on results and interpretation

❌ **Don't**: Over-interpret limitations  
✅ **Do**: Be honest but concise

❌ **Don't**: Use vague terms ("good," "bad")  
✅ **Do**: Use quantitative comparisons

---

## FINAL POLISH CHECKLIST

- [ ] Every figure has a caption and is referenced
- [ ] Every table has a caption and is referenced
- [ ] All numerical values have appropriate precision
- [ ] Units are consistent throughout
- [ ] Statistical significance is addressed
- [ ] All claims are supported by results or citations
- [ ] Discussion connects to objectives (Chapter 1)
- [ ] Transitions between sections are smooth
- [ ] Limitations are acknowledged
- [ ] Implications are clearly stated
- [ ] Writing is concise and precise

---

**Template file**: `CHAPTER_5_TEMPLATE.tex`  
**This guide**: `CHAPTER_5_GUIDE.md`

Good luck with your Chapter 5! 🚀
