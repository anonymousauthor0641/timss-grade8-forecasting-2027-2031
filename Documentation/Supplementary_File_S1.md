# Supplementary File S1

## Supplementary Materials for:
Data-Driven Forecasting of Türkiye's TIMSS Eighth-Grade Science and Mathematics Achievement for the 2027 and 2031 Cycles Using Time-Series and Deep Learning Models

## S1. Data Sources
The study uses publicly available TIMSS data obtained from the International Association for the Evaluation of Educational Achievement (IEA). Eighth-grade science and mathematics achievement scores were collected for the TIMSS cycles from 1995 to 2023.

The study focuses on Türkiye's future TIMSS eighth-grade science and mathematics achievement projections for the 2027 and 2031 cycles. To support model training under the limited number of Türkiye-specific TIMSS cycles, achievement score data from 15 countries with complete historical series were included during model training. The final forecasts were generated only for Türkiye.

## S2. Study Variables

Dependent variables:
- TIMSS Science Score
- TIMSS Mathematics Score

Science independent variables:
- Class Size
- Students Like Learning Science
- Students Value Science
- Students Confident in Science

Mathematics independent variables:
- Students Value Mathematics
- Students Like Learning Mathematics
- Students Confident in Mathematics
- Class Size

## S3. Missing Data Treatment

Türkiye had missing achievement score values for the 1995 and 2003 TIMSS cycles.

- 1995: nearest-year estimation using 1999 values.
- 2003: linear interpolation between 1999 and 2007.

For independent variables:
- 1999: weighted average calculation and approximate SCL-equivalent harmonization.
- 2003: linear interpolation between harmonized 1999 and retrospectively harmonized 2007 values.
- 2007: retrospectively harmonized values included in the final modelling dataset.
- 2011-2023: reported SCL-type values used directly.

## S4. Scale Harmonization

For the 1999 cycle, selected student variables were available as categorical response distributions. Three-category variables were coded as 1-3. Four-category like learning variables were coded as 1-4. Weighted average scores were calculated using valid response percentages.

The weighted average scores were transformed into approximate SCL-equivalent values using a 4-16 methodological harmonization interval. These values should not be interpreted as official TIMSS SCL scores.

## S5. ARIMAX-Based Variable Ordering

ARIMAX-based coefficient estimation was used only to determine the order in which independent variables were included in the M1-M4 model specifications. ARIMAX was not used as the final forecasting model.

Science:
M0: Science Score
M1: Science Score + Class Size
M2: Science Score + Class Size + Students Like Learning Science
M3: Science Score + Class Size + Students Like Learning Science + Students Value Science
M4: Science Score + Class Size + Students Like Learning Science + Students Value Science + Students Confident in Science

Mathematics:
M0: Mathematics Score
M1: Mathematics Score + Students Value Mathematics
M2: Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics
M3: Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics + Students Confident in Mathematics
M4: Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics + Students Confident in Mathematics + Class Size

## S6. Forecasting Models
- ARIMA
- Prophet
- LSTM
- GRU

## S7. Deep Learning Model Configuration
Epoch: 100
Batch size: 4
Optimizer: Adam
Learning rate: 0.001
Loss function: MSE
Activation function: Tanh
Sliding window size: 3

## S8. Rolling Back-Testing Procedure

Step 1: train 1995, 1999, 2003, 2007; test 2011.
Step 2: train 1995, 1999, 2003, 2007, 2011; test 2015.
Step 3: train 1995, 1999, 2003, 2007, 2011, 2015; test 2019.
Step 4: train 1995, 1999, 2003, 2007, 2011, 2015, 2019; test 2023.

## S9. Evaluation Metrics
- MAE
- MSE
- RMSE
- DTW

## S10. Final Forecasts
TIMSS Science Score: 2027 = 541.80; 2031 = 551.40.
TIMSS Mathematics Score: 2027 = 520.95; 2031 = 530.35.

These results should be interpreted as exploratory and conditional projections rather than definitive future outcomes.
