import pandas as pd
from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer

from ds.config import PROCESSED_DATA_DIR, RAW_DATA_DIR, INTERIM_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    
    input_path: Path = RAW_DATA_DIR / "raw.csv",
    output_path: Path = INTERIM_DATA_DIR / "raw_interim.csv",
):
    df = pd.read_csv(input_path)

    logger.success(f"Dataset loaded with shape: {df.shape}")
    logger.info(f"Columns: {df.columns.tolist()}")
    logger.info(f"Count: {df.count()}")
    logger.info("Saving dataset to interim directory...")
    df.to_csv(output_path, index=False)
    logger.success(f"Dataset saved to {output_path}")
    


if __name__ == "__main__":
    app()
