Dataset Folder Readme

This folder contains raw, processed, and model-output datasets prepared for the TIMSS Türkiye eighth-grade science and mathematics forecasting study.

Folder structure:

Raw_Data/
- Original or pre-processing-stage TIMSS achievement scores and independent-variable tables.
- Missing values are retained where they existed in the source tables.
- 1999 independent variables are documented as categorical/no SCL where applicable.

Processed_Data/
- Completed and harmonized datasets.
- Includes imputed Türkiye achievement scores for 1995 and 2003.
- Includes 1999 intermediate weighted average scores and final harmonized independent-variable datasets.

Model_Outputs/
- ARIMAX coefficients and M0-M4 model structures.
- Rolling back-testing metric scores for ARIMA, Prophet, LSTM, and GRU.
- Final GRU-M4 forecasts for the 2027 and 2031 cycles.

Important notes:
1. The 1999 weighted average scores are intermediate values derived from categorical response distributions.
2. The 1999 transformed values should be interpreted as approximate SCL-equivalent values, not official TIMSS SCL scores.
3. The 2007 raw category-index values are not directly equivalent to the later SCL-type values.
4. The 2027 and 2031 forecasts should be interpreted as exploratory and conditional projections rather than definitive future outcomes.
