Code Folder Readme

This folder contains Python scripts prepared for the TIMSS Türkiye eighth-grade science and mathematics forecasting study.

Recommended execution order:

1. 00_create_timss_datasets.py
   - Creates raw, processed, intermediate, harmonized, and final model datasets.

2. 01_scale_harmonization.py
   - Documents and applies 1999 weighted average and approximate SCL-equivalent transformations.
   - Includes the 1-3 and 1-4 coding structures and the 4-16 harmonization interval.

3. 02_arimax_variable_ordering.py
   - Provides ARIMAX-based coefficient outputs and model-entry order.
   - ARIMAX is used only for variable-ordering, not as the final forecasting model.

4. 03_model_specifications.py
   - Creates M0-M4 model structures for science and mathematics.

5. 04_rolling_backtesting_metrics.py
   - Stores rolling back-testing predictions and calculates MAE, MSE, RMSE, and DTW.

6. 05_final_forecasting_gru_m4.py
   - Produces final 2027 and 2031 GRU-M4 forecasts.

7. 06_generate_figures.py
   - Generates science and mathematics forecast figures.

Outputs are saved under:
outputs/
├── datasets/
├── metrics/
├── forecasts/
└── figures/

Important note:
These scripts are designed to document and reproduce the analysis workflow reported in the manuscript. The projections are exploratory and conditional estimates, not definitive future outcomes.
