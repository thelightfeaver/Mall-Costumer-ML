from pathlib import Path
import pandas as pd
from loguru import logger
from tqdm import tqdm
import typer

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
    df.dropna(inplace=True)
    logger.info(f"Dataset shape after cleaning: {df.shape}")

    # Drop unnecessary columns
    df.drop(columns=["CustomerID"], inplace=True)

    # Rename columns
    logger.info("Renaming columns...")
    df.rename(columns={
        "Gender": "gender",
        "Age": "age",
        "Annual Income (k$)": "annual_income",
        "Spending Score (1-100)": "score",
    }, inplace=True)

    
    df.to_csv(output_path, index=False)
    logger.success(f"Features saved to {output_path}")
    

if __name__ == "__main__":
    app()
