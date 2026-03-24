from pathlib import Path

import joblib as jp
import pandas as pd
import typer
from loguru import logger
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm

from ds.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    data_test_path: Path = PROCESSED_DATA_DIR / "test_data.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    # -----------------------------------------
):
    logger.info("Loading data...")
    df = pd.read_csv(features_path)
    lr = LabelEncoder()
    df["gender"] = lr.fit_transform(df["gender"])
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
    X_test.to_csv(data_test_path, index=False)

    logger.info("Data loaded and split into training and test sets.")
    logger.info("Initializing KMeans with specified parameters...")
    kmn = KMeans(n_clusters=3, random_state=42, max_iter=1000)
    pipe = make_pipeline(kmn)

    logger.info("Training model...")

    pipe.fit(X_train)
    logger.success("Model training complete.")
    jp.dump(pipe, model_path)
    logger.info(f"Model saved to {model_path}.")


if __name__ == "__main__":
    app()
