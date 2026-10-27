# F1 DataLab — Formula 1 2025 Season Analytics

A beginner-friendly data analytics project using Python, Pandas, Matplotlib, and Excel to explore Formula 1 race-result data from the 2025 season.

> **Project status:** Driver and constructor analysis is working. Race-status classification, retirement analysis, final validation, and portfolio polish remain before the project can be called complete.

## Project goals

- Load and inspect Formula 1 race-results data from a CSV.
- Calculate driver points from the available records.
- Calculate constructor points from the same records.
- Visualize results with charts.
- Review race-result statuses carefully before counting retirements.
- Practice an end-to-end analytics workflow: data inspection, aggregation, visualization, validation, and communication.

## Tools and technologies

- **Python** — analysis scripting
- **Pandas** — loading, grouping, aggregation, and exporting
- **Matplotlib** — charts
- **Microsoft Excel** — PivotTables and an initial dashboard
- **Visual Studio Code** — development environment

## Project structure

```text
F1_DataLab/
├── data/
│   └── race_results_2025.csv
├── notebooks/
├── outputs/
│   ├── driver_points.csv
│   ├── constructor_points.csv
│   ├── driver_leaderboard.png
│   ├── constructor_performance.png
│   ├── non_time_results_to_review.csv
│   └── f1_results_copy.csv
├── main.py
└── README.md
```

The exact contents of `outputs/` depend on the version of `main.py` that has been run. Generated files should be reproducible by running the script.

## Dataset

The source file is `data/race_results_2025.csv`.

The current script reports:
- **480** race-result records
- **21** unique driver names in the file
- **10** constructor names
- **2,424** total points across the recorded rows

These figures are calculated from the local CSV. They do not by themselves prove that the file contains every official 2025 Formula 1 result. Validate the source and its coverage before publishing the results as official season standings.

### Fields used

| Column | Use |
|---|---|
| `season` | Season identifier |
| `round` | Event round |
| `Track` | Circuit/event label |
| `Position` | Recorded finishing position |
| `FullName` | Driver grouping |
| `TeamName` | Constructor grouping |
| `GridPosition` | Starting position |
| `Laps` | Laps completed |
| `Time/Retired` | Recorded time, gap, or status text |
| `Points` | Points recorded for a result |
| `drs_zones` | DRS-zone count |

## Setup

### 1. Check Python

Install Python and confirm it is available in the terminal:

```powershell
python --version
```

### 2. Open the project

Open the `F1_DataLab` folder in Visual Studio Code. Open a terminal from that folder, so the terminal path ends in `F1_DataLab`.

### 3. Install dependencies

```powershell
python -m pip install pandas matplotlib
```

If your system uses the Windows Python launcher, this may also work:

```powershell
py -m pip install pandas matplotlib
```

### 4. Run the analysis

```powershell
python main.py
```

The script reads the CSV from `data/` and writes analysis outputs to `outputs/`.

## Analyses implemented

### 1. Dataset overview

The script prints the number of rows, unique drivers, constructors, and the sum of recorded points.

### 2. Driver points leaderboard

The script groups rows by `FullName`, sums `Points`, and sorts totals from highest to lowest.

Current top ten from the local dataset:

| Rank in this dataset | Driver | Points |
|---:|---|---:|
| 1 | Lando Norris | 394 |
| 2 | Max Verstappen | 389 |
| 3 | Oscar Piastri | 381 |
| 4 | George Russell | 289 |
| 5 | Charles Leclerc | 225 |
| 6 | Kimi Antonelli | 135 |
| 7 | Lewis Hamilton | 135 |
| 8 | Alexander Albon | 70 |
| 9 | Carlos Sainz Jr. | 54 |
| 10 | Nico Hülkenberg | 51 |

These are calculations from the provided CSV. Independently validate them before describing them as official championship standings.

### 3. Constructor points leaderboard

The script groups rows by `TeamName`, sums `Points`, and sorts totals from highest to lowest.

| Rank in this dataset | Constructor | Points |
|---:|---|---:|
| 1 | McLaren | 775 |
| 2 | Mercedes | 424 |
| 3 | Red Bull | 410 |
| 4 | Ferrari | 360 |
| 5 | Williams | 124 |
| 6 | Racing Bulls | 88 |
| 7 | Aston Martin | 80 |
| 8 | Haas | 73 |
| 9 | Kick Sauber | 70 |
| 10 | Alpine | 20 |

### 4. Charts

Matplotlib creates horizontal bar charts for the top ten drivers and constructor totals. The images are saved in `outputs/`.

### 5. Race-result status review — in progress

The `Time/Retired` field contains a mixture of times, time gaps, lap deficits, and text statuses. Examples in the current file include `Accident`, `Brakes`, `+1 lap`, `Car underweight`, and `Illegal skid block wear`.

These values must not all be counted as retirements. The next step is to define and document a status-classification rule, inspect ambiguous values, and calculate retirement statistics by circuit. Disqualifications and classified/lapped results should be kept distinct from retirements wherever the source supports that distinction.

## Validation and limitations

- Driver and constructor totals are calculated from the same local CSV.
- The sum of driver points and constructor points should reconcile when each row is assigned to one driver and one constructor and the same `Points` values are used.
- A dataset can be internally consistent without being complete or officially verified.
- The file currently contains 480 rows and 21 unique driver names. Confirm the source's scope and quality before interpreting these as complete-season counts.
- Status text requires cleaning and explicit classification before retirement counts are published.
- Driver and constructor rankings are different analyses: constructor points combine points attributed to the team's recorded drivers.

## Planned next steps

- [ ] Inspect unique values and missing values in relevant columns.
- [ ] Validate the CSV source and coverage against a reliable reference.
- [ ] Define a transparent rule for classifying retirements, disqualifications, classified finishes, and other statuses.
- [ ] Calculate retirements by circuit and visualize the result.
- [ ] Add data-quality checks and helpful error messages to `main.py`.
- [ ] Verify all outputs are reproducible from a clean run.
- [ ] Add final screenshots of the Excel dashboard and Python charts.
- [ ] Write a final project summary and publish a LinkedIn post after the analysis is complete.

## Skills demonstrated

- CSV ingestion
- Data inspection and aggregation with Pandas
- Grouping and sorting
- Data visualization with Matplotlib
- Excel PivotTables and charts
- Exporting processed data and chart images
- Data validation and communicating analytical limitations

## Author

**Praveen Kumar**  
Project: F1 DataLab — Formula 1 2025 Season Analytics

---

*This is a learning and portfolio project. Results describe the local dataset and should not be represented as official statistics until the dataset's source and completeness have been verified.*
