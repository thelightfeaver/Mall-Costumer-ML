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
    df = pd.read_csv(input_path)
    logger.info(f"Interim dataset loaded with shape: {df.shape}")

if __name__ == "__main__":
    app()
