"""
Scale harmonization for 1999 TIMSS independent variables.

This script documents the weighted-average and approximate SCL-equivalent transformation
used for 1999 categorical response distributions.
"""

from pathlib import Path
import pandas as pd

OUT = Path("outputs/datasets")
OUT.mkdir(parents=True, exist_ok=True)

def transform_three_category(weighted_average: float) -> float:
    """Map 1-3 weighted average scale to approximate 4-16 harmonization interval."""
    return 4 + ((weighted_average - 1) / (3 - 1)) * (16 - 4)

def transform_four_category(weighted_average: float) -> float:
    """Map 1-4 weighted average scale to approximate 4-16 harmonization interval."""
    return 4 + ((weighted_average - 1) / (4 - 1)) * (16 - 4)

science_intermediate = pd.DataFrame({
    "TIMSS Cycle": [1999],
    "Students Confident in Science": [2.1435],
    "Students Like Learning Science": [3.1544],
    "Students Value Science": [2.4102],
    "Class Size": [48],
})

mathematics_intermediate = pd.DataFrame({
    "TIMSS Cycle": [1999],
    "Students Confident in Mathematics": [1.9827],
    "Students Like Learning Mathematics": [2.9711],
    "Students Value Mathematics": [2.3469],
    "Class Size": [48],
})

science_1999_harmonized = pd.DataFrame({
    "TIMSS Cycle": [1999],
    "Students Confident in Science": [transform_three_category(2.1435)],
    "Students Like Learning Science": [transform_four_category(3.1544)],
    "Students Value Science": [transform_three_category(2.4102)],
    "Class Size": [48],
})

mathematics_1999_harmonized = pd.DataFrame({
    "TIMSS Cycle": [1999],
    "Students Confident in Mathematics": [transform_three_category(1.9827)],
    "Students Like Learning Mathematics": [transform_four_category(2.9711)],
    "Students Value Mathematics": [transform_three_category(2.3469)],
    "Class Size": [48],
})

with pd.ExcelWriter(OUT / "independent_variables_1999_harmonization_details.xlsx") as writer:
    science_intermediate.to_excel(writer, sheet_name="Science Intermediate", index=False)
    mathematics_intermediate.to_excel(writer, sheet_name="Mathematics Intermediate", index=False)
    science_1999_harmonized.to_excel(writer, sheet_name="Science 1999 Harmonized", index=False)
    mathematics_1999_harmonized.to_excel(writer, sheet_name="Mathematics 1999 Harmonized", index=False)

print("1999 harmonization details saved.")
