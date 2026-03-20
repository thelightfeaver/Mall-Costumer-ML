from pathlib import Path

import pandas as pd
import typer
from loguru import logger
from tqdm import tqdm

from ds.config import INTERIM_DATA_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = INTERIM_DATA_DIR / "raw_interim.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
):
    # load interim dataset
    df = pd.read_csv(input_path)
    logger.info(f"Interim dataset loaded with shape: {df.shape}")

    # Clean dataset
    logger.info("Cleaning dataset...")
    sum_na = df.isna().sum()
    sum_null = df.isnull().sum()
    sum_duplicates = df.duplicated().sum()
    logger.info(f"Missing values:\n{sum_na}")
    logger.info(f"Null values:\n{sum_null}")
    logger.info(f"Duplicate rows: {sum_duplicates}")

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    logger.info(f"Dataset cleaned. New shape: {df.shape}")

    # Drop unnecessary columns
    df.drop(columns=["CustomerID"], inplace=True)

    # Rename columns
    logger.info("Renaming columns...")
    df.rename(
        columns={
            "Gender": "gender",
            "Age": "age",
            "Annual Income (k$)": "annual_income",
            "Spending Score (1-100)": "score",
        },
        inplace=True,
    )

    df.to_csv(output_path, index=False)
    logger.success(f"Features saved to {output_path}")


if __name__ == "__main__":
    app()
