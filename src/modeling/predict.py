from pathlib import Path

import joblib as jp
import typer
from loguru import logger
from tqdm import tqdm

from src.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "test_features.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    predictions_path: Path = PROCESSED_DATA_DIR / "test_predictions.csv",
    # -----------------------------------------
):
    model = jp.load(model_path)
    logger.success("Model loaded successfully.")


if __name__ == "__main__":
    app()
