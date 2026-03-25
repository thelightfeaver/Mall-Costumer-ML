from pathlib import Path

import joblib as jp
import mlflow
import pandas as pd
import typer
from loguru import logger
from sklearn.metrics import silhouette_score

from src.config import MODELS_DIR, PROCESSED_DATA_DIR, URL_MLFLOW_TRACKING
from src.util import configure_mlflow_experiment, load_run_id

app = typer.Typer()


@app.command()
def main(
    model_path: Path = MODELS_DIR / "model.pkl",
    test_data_path: Path = PROCESSED_DATA_DIR / "test_data.csv",
):
    configure_mlflow_experiment("customer_segmentation", URL_MLFLOW_TRACKING)
    mlflow.sklearn.autolog(log_input_examples=True, log_model_signatures=True)

    with mlflow.start_run(run_id=load_run_id()):
        logger.info("Loading test features...")
        X_test = pd.read_csv(test_data_path)
        model = jp.load(model_path)
        x_predict = model.predict(X_test)
        score = silhouette_score(X_test, x_predict)
        logger.info(f"Silhouette score: {score}")
        mlflow.log_metric("silhouette_score", score)


if __name__ == "__main__":
    app()
