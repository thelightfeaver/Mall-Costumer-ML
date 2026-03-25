from pathlib import Path

import mlflow
import joblib as jp
import pandas as pd
from loguru import logger
from sklearn.metrics import silhouette_score
import typer

from src.config import MODELS_DIR, PROCESSED_DATA_DIR, URL_MLFLOW_TRACKING
from src.util import configure_mlflow_experiment, export_metrics

app = typer.Typer()


@app.command()
def main(
    model_path: Path = MODELS_DIR / "model.pkl",
    test_data_path: Path = PROCESSED_DATA_DIR / "test_data.csv",
):
    configure_mlflow_experiment("customer_segmentation", URL_MLFLOW_TRACKING)
    mlflow.sklearn.autolog(log_input_examples=True, log_model_signatures=True)

    with mlflow.start_run():
        logger.info("Loading test features...")
        X_test = pd.read_csv(test_data_path)
        model = jp.load(model_path)
        x_predict = model.predict(X_test)
        score = silhouette_score(X_test, x_predict)
        logger.info(f"Silhouette score: {score}")
        mlflow.log_metric("silhouette_score", score)

        # Export metrics to JSON file.
        json_path = MODELS_DIR / "model_metrics.json"
        entry = {"silhouette_score": score, "best_params": model.get_params()}
        export_metrics(entry, json_path)
        logger.info(f"Model metrics saved to {json_path}.")



if __name__ == "__main__":
    app()
