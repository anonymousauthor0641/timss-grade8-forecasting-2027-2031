"""
Rolling back-testing metric calculation for reported ARIMA, Prophet, LSTM, and GRU outputs.

This script stores the back-testing predictions reported in the manuscript and calculates
MAE, MSE, RMSE, and a simple DTW distance.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

OUT = Path("outputs/metrics")
OUT.mkdir(parents=True, exist_ok=True)

def dtw_distance(a, b):
    """Compute Dynamic Time Warping distance for two numeric sequences."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    n, m = len(a), len(b)
    dtw = np.full((n + 1, m + 1), np.inf)
    dtw[0, 0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(a[i - 1] - b[j - 1])
            dtw[i, j] = cost + min(dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1])
    return float(dtw[n, m])

def metrics(actual, predicted):
    return {
        "MAE": round(mean_absolute_error(actual, predicted), 2),
        "MSE": round(mean_squared_error(actual, predicted), 2),
        "RMSE": round(np.sqrt(mean_squared_error(actual, predicted)), 2),
        "DTW": round(dtw_distance(actual, predicted), 2),
    }

science_actual = [483.0, 493.0, 515.0, 530.0]
math_actual = [452.0, 458.0, 496.0, 509.0]

science_predictions = {
    ("ARIMA", "M0"): [480.0, 499.0, 510.0, 532.0],
    ("ARIMA", "M1"): [482.0, 497.0, 513.0, 531.0],
    ("Prophet", "M4"): [481.5, 494.0, 513.5, 528.0],
    ("LSTM", "M4"): [482.7, 493.2, 515.2, 529.5],
    ("GRU", "M4"): [483.1, 492.9, 515.1, 529.8],
}

mathematics_predictions = {
    ("ARIMA", "M3"): [452.0, 460.0, 494.0, 510.0],
    ("Prophet", "M4"): [452.0, 459.0, 495.0, 507.0],
    ("LSTM", "M4"): [452.2, 458.4, 496.3, 508.4],
    ("GRU", "M4"): [452.0, 458.1, 496.1, 508.9],
}

rows = []
for (model, spec), pred in science_predictions.items():
    row = {"Subject": "Science", "Forecasting model": model, "Model specification": spec}
    row.update(metrics(science_actual, pred))
    rows.append(row)

for (model, spec), pred in mathematics_predictions.items():
    row = {"Subject": "Mathematics", "Forecasting model": model, "Model specification": spec}
    row.update(metrics(math_actual, pred))
    rows.append(row)

metric_table = pd.DataFrame(rows)
metric_table.to_excel(OUT / "rolling_backtesting_metrics_selected_models.xlsx", index=False)

print("Rolling back-testing metric outputs saved.")
