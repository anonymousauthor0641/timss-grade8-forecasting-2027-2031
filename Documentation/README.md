# Data-Driven Forecasting of Türkiye's TIMSS Eighth-Grade Science and Mathematics Achievement

This repository contains the datasets, Python scripts, forecasting outputs, figures, and supplementary documentation associated with the study on Türkiye's TIMSS eighth-grade science and mathematics projections for the 2027 and 2031 cycles.

## Study Overview

This study generates exploratory and conditional projections for Türkiye's TIMSS eighth-grade science and mathematics achievement scores for the 2027 and 2031 cycles. ARIMA, Prophet, LSTM, and GRU models were compared across M0-M4 model specifications. The GRU-M4 model produced the most favorable rolling back-testing performance and was used for the final projections.

## Main Methodological Steps

1. Missing dependent-variable values were imputed.
2. Scale inconsistencies in the independent variables were harmonized.
3. Missing independent-variable values were imputed.
4. ARIMAX-based coefficient estimation was used only to determine the order of independent-variable inclusion.
5. ARIMA, Prophet, LSTM, and GRU models were compared across M0-M4 specifications.
6. Rolling back-testing was conducted using Türkiye's 2011, 2015, 2019, and 2023 TIMSS cycles.
7. Final projections for 2027 and 2031 were generated using the GRU-M4 model.

## Important Note

The projections should be interpreted as exploratory and conditional estimates rather than definitive future outcomes.
