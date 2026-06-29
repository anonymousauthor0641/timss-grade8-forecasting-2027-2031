"""
ARIMAX-based variable ordering for M1-M4 model specifications.

ARIMAX is used here only to determine the order of independent-variable inclusion.
It is not used as the final forecasting model.
"""

from pathlib import Path
import pandas as pd

OUT = Path("outputs/model_outputs")
OUT.mkdir(parents=True, exist_ok=True)

science_coefficients = pd.DataFrame({
    "Order": [1, 2, 3, 4],
    "Independent Variable": [
        "Class Size",
        "Students Like Learning Science",
        "Students Value Science",
        "Students Confident in Science",
    ],
    "Beta coefficient": [1.9969, 1.9478, 0.7611, 0.1288],
    "Model inclusion": ["M1", "M2", "M3", "M4"],
})

mathematics_coefficients = pd.DataFrame({
    "Order": [1, 2, 3, 4],
    "Independent Variable": [
        "Students Value Mathematics",
        "Students Like Learning Mathematics",
        "Students Confident in Mathematics",
        "Class Size",
    ],
    "Beta coefficient": [5.4031, 4.1274, 1.2359, 0.4272],
    "Model inclusion": ["M1", "M2", "M3", "M4"],
})

with pd.ExcelWriter(OUT / "arimax_coefficients_and_variable_ordering.xlsx") as writer:
    science_coefficients.to_excel(writer, sheet_name="Science", index=False)
    mathematics_coefficients.to_excel(writer, sheet_name="Mathematics", index=False)

print("ARIMAX variable-ordering outputs saved.")
