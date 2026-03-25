from pathlib import Path

import pandas as pd
import typer
from loguru import logger
from tqdm import tqdm

from src.config import INTERIM_DATA_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "raw.csv",
    output_path: Path = INTERIM_DATA_DIR / "raw_interim.csv",
):
    df = pd.read_csv(
        "https://gist.githubusercontent.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf/raw/8bd6144a87988213693754baaa13fb204933282d/Mall_Customers.csv"
    )

    logger.success(f"Dataset loaded with shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    logger.info(f"Count: {df.count()}")
    logger.info("Saving dataset to interim directory...")
    df.to_csv(input_path, index=False)
    df.to_csv(output_path, index=False)
    logger.success(f"Dataset saved to {output_path}")


if __name__ == "__main__":
    app()
