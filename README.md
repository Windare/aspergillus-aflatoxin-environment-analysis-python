# Environmental Effects on Aspergillus Count and Aflatoxin Production

This project uses Python to explore how moisture and temperature relate to Aspergillus count and aflatoxin production. The analysis includes visual comparisons and a correlation summary for the measured variables.

## Questions explored

- How does moisture relate to Aspergillus count and aflatoxin levels?
- How does temperature relate to the same measurements?
- Which variables appear more strongly associated in the combined dataset?

## Data preparation

The CSV files in `data/raw/` are the cleaned working files exported after the initial Excel preparation. In Excel, the data was arranged into analysis-ready tables so that the Python notebook could focus on comparison, visualization, and summary statistics.

The Excel preparation included:

- arranging the measurements into separate tables for moisture and temperature analysis;
- checking that the variables were consistently named across files;
- preparing summary tables for Aspergillus count and aflatoxin measurements;
- exporting the cleaned tables as CSV files for Python analysis.

## Methods used

- Data cleaning and organization with Pandas
- Line and bar chart visualization with Matplotlib
- Exploratory comparison across moisture and temperature levels
- Correlation summary for numeric variables

## Repository structure

```text
├── data/raw/
├── notebooks/01_environmental_effects_aflatoxin_analysis.ipynb
├── reports/figures/
├── reports/tables/
├── src/environmental_aflatoxin_analysis.py
├── requirements.txt
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
python src/environmental_aflatoxin_analysis.py
```

## What I practised

This project helped me practise exploratory analysis, visual comparison of experimental conditions, and summarizing relationships between numeric variables.
