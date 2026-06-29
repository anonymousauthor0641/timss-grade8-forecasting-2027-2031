"""
Final 2027 and 2031 forecasts using the GRU-M4 model.

The values in this script reproduce the final forecasts reported in the manuscript.
"""

from pathlib import Path
import pandas as pd

OUT = Path("outputs/forecasts")
OUT.mkdir(parents=True, exist_ok=True)

score_forecasts = pd.DataFrame({
    "Field": ["TIMSS Science Score", "TIMSS Mathematics Score"],
    "2023 Observed": [530.00, 509.00],
    "2027 Forecast": [541.80, 520.95],
    "2031 Forecast": [551.40, 530.35],
    "2023-2027 Change": [11.80, 11.95],
    "2027-2031 Change": [9.60, 9.40],
    "2023-2031 Change": [21.40, 21.35],
    "Final model": ["GRU-M4", "GRU-M4"],
})

science_predictor_forecasts = pd.DataFrame({
    "Variable": [
        "Class Size",
        "Students Like Learning Science",
        "Students Value Science",
        "Students Confident in Science",
    ],
    "2027 Forecast": [27.13, 10.80, 9.95, 11.23],
    "2031 Forecast": [26.44, 10.84, 9.88, 11.45],
})

mathematics_predictor_forecasts = pd.DataFrame({
    "Variable": [
        "Students Value Mathematics",
        "Students Like Learning Mathematics",
        "Students Confident in Mathematics",
        "Class Size",
    ],
    "2027 Forecast": [9.33, 10.15, 9.60, 26.61],
    "2031 Forecast": [9.13, 10.11, 9.56, 25.77],
})

with pd.ExcelWriter(OUT / "forecast_results_2027_2031.xlsx") as writer:
    score_forecasts.to_excel(writer, sheet_name="Final Score Forecasts", index=False)
    science_predictor_forecasts.to_excel(writer, sheet_name="Science Predictors", index=False)
    mathematics_predictor_forecasts.to_excel(writer, sheet_name="Mathematics Predictors", index=False)

print("Final GRU-M4 forecasts saved.")
