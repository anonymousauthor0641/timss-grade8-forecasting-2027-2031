"""
Create raw, processed, and final model datasets for the TIMSS Türkiye eighth-grade
science and mathematics forecasting study.

This script replaces the older PISA reading dataset-generation script.
"""

from pathlib import Path
import pandas as pd
import numpy as np

OUT = Path("outputs/datasets")
OUT.mkdir(parents=True, exist_ok=True)

cycles = [1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023]

science_raw = pd.DataFrame({
    "Country": [
        "United States of America", "Australia", "Hong Kong", "United Kingdom",
        "Iran", "Israel", "Italy", "Japan", "Republic of Korea", "Lithuania",
        "Hungary", "Malaysia", "Singapore", "Türkiye", "Jordan"
    ],
    1995: [513, 514, 522, 533, 470, 524, 480, 571, 546, 477, 554, 534, 607, np.nan, 449],
    1999: [515, 540, 530, 538, 448, 468, 493, 550, 549, 488, 552, 492, 568, 433, 450],
    2003: [527, 527, 556, 533, 453, 481, 491, 571, 558, 519, 506, 426, 578, np.nan, 449],
    2007: [520, 515, 530, 542, 459, 468, 495, 554, 553, 519, 539, 471, 567, 454, 482],
    2011: [525, 519, 535, 533, 474, 516, 501, 558, 560, 514, 522, 426, 590, 483, 449],
    2015: [530, 512, 546, 537, 456, 507, 499, 571, 556, 519, 527, 471, 597, 493, 426],
    2019: [522, 528, 504, 517, 449, 513, 500, 570, 561, 534, 530, 460, 608, 515, 452],
    2023: [513, 520, 528, 531, 419, 481, 501, 557, 545, 519, 522, 426, 606, 530, 413],
})

mathematics_raw = pd.DataFrame({
    "Country": [
        "United States of America", "Australia", "Hong Kong", "United Kingdom",
        "Iran", "Israel", "Italy", "Japan", "Republic of Korea", "Lithuania",
        "Hungary", "Malaysia", "Singapore", "Türkiye", "Jordan"
    ],
    1995: [492, 509, 569, 498, 428, 522, 476, 605, 607, 472, 537, 519, 643, np.nan, 406],
    1999: [502, 525, 582, 496, 422, 466, 479, 579, 587, 482, 532, 519, 604, 429, 428],
    2003: [504, 505, 586, 525, 411, 496, 484, 570, 589, 502, 552, 411, 605, np.nan, 424],
    2007: [508, 496, 572, 513, 403, 463, 480, 570, 597, 506, 517, 474, 593, 432, 427],
    2011: [509, 505, 586, 507, 415, 516, 498, 570, 613, 502, 505, 440, 611, 452, 406],
    2015: [518, 505, 594, 518, 436, 511, 494, 586, 606, 511, 514, 465, 621, 458, 386],
    2019: [515, 517, 578, 515, 446, 519, 497, 594, 607, 520, 517, 461, 616, 496, 420],
    2023: [487, 509, 575, 525, 423, 487, 501, 595, 596, 514, 506, 411, 605, 509, 388],
})

# Türkiye dependent-variable imputation
science_processed = science_raw.copy()
mathematics_processed = mathematics_raw.copy()

science_processed.loc[science_processed["Country"] == "Türkiye", 1995] = 433
science_processed.loc[science_processed["Country"] == "Türkiye", 2003] = (433 + 454) / 2

mathematics_processed.loc[mathematics_processed["Country"] == "Türkiye", 1995] = 429
mathematics_processed.loc[mathematics_processed["Country"] == "Türkiye", 2003] = (429 + 432) / 2

science_independent_raw = pd.DataFrame({
    "TIMSS Cycle": [1999, 2003, 2007, 2011, 2015, 2019, 2023],
    "Students Confident in Science": [
        "Categorical data is present / No SCL index", np.nan, 1.60,
        10.2664504, 10.6500438, 10.8249259, 10.9464101
    ],
    "Students Like Learning Science": [
        "Categorical data is present / No SCL index", np.nan, 1.31,
        10.6027853, 10.7377560, 10.7335518, 10.7385090
    ],
    "Students Value Science": [
        "Categorical data is present / No SCL index", np.nan, 1.40,
        10.0075404, 10.4067338, 10.3419201, 9.7877011
    ],
    "Class Size": [48, np.nan, 31.79, 29.90, 29.43, 27.85, 28.15],
})

mathematics_independent_raw = pd.DataFrame({
    "TIMSS Cycle": [1999, 2003, 2007, 2011, 2015, 2019, 2023],
    "Students Confident in Mathematics": [
        "Categorical data is present / No SCL index", np.nan, 1.85,
        9.7237013, 9.7460840, 9.8069472, 9.5624215
    ],
    "Students Like Learning Mathematics": [
        "Categorical data is present / No SCL index", np.nan, 1.40,
        10.2440056, 10.2531972, 10.3306394, 10.1049970
    ],
    "Students Value Mathematics": [
        "Categorical data is present / No SCL index", np.nan, 1.16,
        9.9821519, 10.0530892, 10.0583487, 9.2934072
    ],
    "Class Size": [48, np.nan, 32.19, 30.29, 29.23, 27.23, 28.14],
})

# Final harmonized independent-variable datasets used in modelling
science_independent_harmonized = pd.DataFrame({
    "TIMSS Cycle": [1999, 2003, 2007, 2011, 2015, 2019, 2023],
    "Students Confident in Science": [10.8580, 10.4882, 10.1183, 10.2664504, 10.6500438, 10.8249259, 10.9464101],
    "Students Like Learning Science": [12.6080, 11.6052, 10.6024, 10.6027853, 10.7377560, 10.7335518, 10.7385090],
    "Students Value Science": [12.4600, 11.3886, 10.3171, 10.0075404, 10.4067338, 10.3419201, 9.7877011],
    "Class Size": [48.0000, 39.8950, 31.7900, 29.9000, 29.4300, 27.8500, 28.1500],
})

mathematics_independent_harmonized = pd.DataFrame({
    "TIMSS Cycle": [1999, 2003, 2007, 2011, 2015, 2019, 2023],
    "Students Confident in Mathematics": [9.9100, 9.8628, 9.8155, 9.7237013, 9.7460840, 9.8069472, 9.5624215],
    "Students Like Learning Mathematics": [11.8840, 11.1011, 10.3181, 10.2440056, 10.2531972, 10.3306394, 10.1049970],
    "Students Value Mathematics": [12.0700, 11.2160, 10.3620, 9.9821519, 10.0530892, 10.0583487, 9.2934072],
    "Class Size": [48.0000, 40.0950, 32.1900, 30.2900, 29.2300, 27.2300, 28.1400],
})

turkiye_scores = pd.DataFrame({
    "TIMSS Cycle": cycles,
    "Science Score": [433, 433, 443.5, 454, 483, 493, 515, 530],
    "Mathematics Score": [429, 429, 430.5, 432, 452, 458, 496, 509],
})

science_model_dataset = turkiye_scores[["TIMSS Cycle", "Science Score"]].merge(
    science_independent_harmonized, on="TIMSS Cycle", how="left"
)

mathematics_model_dataset = turkiye_scores[["TIMSS Cycle", "Mathematics Score"]].merge(
    mathematics_independent_harmonized, on="TIMSS Cycle", how="left"
)

# Save outputs
science_raw.to_excel(OUT / "01_timss_science_scores_raw.xlsx", index=False)
mathematics_raw.to_excel(OUT / "02_timss_mathematics_scores_raw.xlsx", index=False)
science_independent_raw.to_excel(OUT / "03_science_independent_variables_raw.xlsx", index=False)
mathematics_independent_raw.to_excel(OUT / "04_mathematics_independent_variables_raw.xlsx", index=False)

science_processed.to_excel(OUT / "05_timss_science_scores_processed.xlsx", index=False)
mathematics_processed.to_excel(OUT / "06_timss_mathematics_scores_processed.xlsx", index=False)
science_independent_harmonized.to_excel(OUT / "07_science_independent_variables_harmonized.xlsx", index=False)
mathematics_independent_harmonized.to_excel(OUT / "08_mathematics_independent_variables_harmonized.xlsx", index=False)
science_model_dataset.to_excel(OUT / "09_final_science_model_dataset.xlsx", index=False)
mathematics_model_dataset.to_excel(OUT / "10_final_mathematics_model_dataset.xlsx", index=False)

print(f"Datasets saved to: {OUT.resolve()}")
