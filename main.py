
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
DATA_FILE = Path("data/race_results_2025.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("F1 DATALAB | 2025 SEASON ANALYTICS")
print("=" * 40)

# Basic data overview
print(f"\nRace-result records: {len(df)}")
print(f"Unique drivers: {df['FullName'].nunique()}")
print(f"Constructors: {df['TeamName'].nunique()}")
print(f"Total points recorded: {df['Points'].sum():.0f}")

# 1. Driver championship
driver_points = (
    df.groupby("FullName")["Points"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 10 DRIVERS")
print(driver_points.head(10).to_string())

driver_points.to_csv(OUTPUT_DIR / "driver_points.csv")

top_drivers = driver_points.head(10).sort_values()

ax = top_drivers.plot(kind="barh", figsize=(10, 6))
ax.set_title("F1 2025 - Top 10 Drivers by Points")
ax.set_xlabel("Total points")
ax.set_ylabel("Driver")

for bar in ax.patches:
    ax.text(
        bar.get_width() + 3,
        bar.get_y() + bar.get_height() / 2,
        f"{bar.get_width():.0f}",
        va="center"
    )

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "driver_leaderboard.png", dpi=150)
plt.close()

# 2. Constructor championship
team_points = (
    df.groupby("TeamName")["Points"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCONSTRUCTOR STANDINGS")
print(team_points.to_string())

team_points.to_csv(OUTPUT_DIR / "constructor_points.csv")

ax = team_points.sort_values().plot(
    kind="barh", figsize=(10, 6)
)
ax.set_title("F1 2025 - Constructor Performance")
ax.set_xlabel("Total points")
ax.set_ylabel("Constructor")

for bar in ax.patches:
    ax.text(
        bar.get_width() + 3,
        bar.get_y() + bar.get_height() / 2,
        f"{bar.get_width():.0f}",
        va="center"
    )

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "constructor_performance.png", dpi=150)
plt.close()

# 3. Inspect possible retirements
status = df["Time/Retired"].astype("string").str.strip()

non_numeric_results = df[
    status.str.contains(
        r"[A-Za-z]",
        na=False,
        regex=True
    )
]

print("\nNON-TIME RESULTS TO REVIEW")
print(
    non_numeric_results[
        ["Track", "FullName", "TeamName", "Time/Retired"]
    ].head(20).to_string(index=False)
)

non_numeric_results.to_csv(
    OUTPUT_DIR / "non_time_results_to_review.csv",
    index=False
)

# 4. Save a clean copy of the dataset
df.to_csv(OUTPUT_DIR / "f1_results_copy.csv", index=False)

print("\nAnalysis complete!")
print("Check the outputs folder for CSV files and charts.")
