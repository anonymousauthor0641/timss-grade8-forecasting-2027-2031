"""
Create M0-M4 model specification tables for science and mathematics.
"""

from pathlib import Path
import pandas as pd

OUT = Path("outputs/model_outputs")
OUT.mkdir(parents=True, exist_ok=True)

science_models = pd.DataFrame({
    "Model": ["M0", "M1", "M2", "M3", "M4"],
    "Variables": [
        "Science Score",
        "Science Score + Class Size",
        "Science Score + Class Size + Students Like Learning Science",
        "Science Score + Class Size + Students Like Learning Science + Students Value Science",
        "Science Score + Class Size + Students Like Learning Science + Students Value Science + Students Confident in Science",
    ],
})

mathematics_models = pd.DataFrame({
    "Model": ["M0", "M1", "M2", "M3", "M4"],
    "Variables": [
        "Mathematics Score",
        "Mathematics Score + Students Value Mathematics",
        "Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics",
        "Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics + Students Confident in Mathematics",
        "Mathematics Score + Students Value Mathematics + Students Like Learning Mathematics + Students Confident in Mathematics + Class Size",
    ],
})

with pd.ExcelWriter(OUT / "model_specifications_m0_m4.xlsx") as writer:
    science_models.to_excel(writer, sheet_name="Science M0-M4", index=False)
    mathematics_models.to_excel(writer, sheet_name="Mathematics M0-M4", index=False)

print("M0-M4 model specification tables saved.")
