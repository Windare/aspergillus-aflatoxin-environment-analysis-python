from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def line_plot(df, x_col, y_cols, title, xlabel, ylabel, output_path):
    plt.figure(figsize=(9, 5))
    for col in y_cols:
        plt.plot(df[x_col], df[col], marker='o', label=col)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main(project_root: str | Path = '.') -> None:
    root = Path(project_root)
    data_dir = root / 'data' / 'raw'
    figures_dir = root / 'reports' / 'figures'
    tables_dir = root / 'reports' / 'tables'
    figures_dir.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)

    moisture = pd.read_csv(data_dir / 'moisture_summary.csv')
    temperature = pd.read_csv(data_dir / 'temperature_summary.csv')
    combined = pd.read_csv(data_dir / 'aspergillus_aflatoxin_temperature.csv')

    line_plot(
        moisture,
        'Moisture',
        ['AspergillusCount', 'AFB1', 'AFB2', 'AFG1', 'AFG2'],
        'Moisture effect on Aspergillus count and aflatoxins',
        'Moisture',
        'Measured value',
        figures_dir / 'moisture_effect_summary.png',
    )
    line_plot(
        temperature,
        'Temperature',
        ['AspergillusCount', 'AFB1', 'AFB2', 'AFG1', 'AFG2'],
        'Temperature effect on Aspergillus count and aflatoxins',
        'Temperature',
        'Measured value',
        figures_dir / 'temperature_effect_summary.png',
    )

    corr = combined.corr(numeric_only=True).round(3)
    corr.to_csv(tables_dir / 'correlation_summary.csv')
    print(corr)


if __name__ == '__main__':
    main(Path(__file__).resolve().parents[1])
