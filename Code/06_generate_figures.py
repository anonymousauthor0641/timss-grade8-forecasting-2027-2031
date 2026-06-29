"""
Generate simple forecast figures for Türkiye's TIMSS science and mathematics scores.
"""

from pathlib import Path
import matplotlib.pyplot as plt

OUT = Path("outputs/figures")
OUT.mkdir(parents=True, exist_ok=True)

science_years = [1999, 2003, 2007, 2011, 2015, 2019, 2023, 2027, 2031]
science_scores = [433, 443.5, 454, 483, 493, 515, 530, 541.80, 551.40]

math_years = [1999, 2003, 2007, 2011, 2015, 2019, 2023, 2027, 2031]
math_scores = [429, 430.5, 432, 452, 458, 496, 509, 520.95, 530.35]

plt.figure(figsize=(8, 5))
plt.plot(science_years, science_scores, marker="o")
plt.xlabel("TIMSS Cycle")
plt.ylabel("Science Score")
plt.title("Türkiye TIMSS Eighth-Grade Science Score Forecasts")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT / "science_forecast_2027_2031.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(math_years, math_scores, marker="o")
plt.xlabel("TIMSS Cycle")
plt.ylabel("Mathematics Score")
plt.title("Türkiye TIMSS Eighth-Grade Mathematics Score Forecasts")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT / "mathematics_forecast_2027_2031.png", dpi=300)
plt.close()

print("Forecast figures saved.")
