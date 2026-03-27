from pathlib import Path

import joblib as jp
import mlflow
import pandas as pd
import typer
from loguru import logger
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.config import MODELS_DIR, PROCESSED_DATA_DIR, URL_MLFLOW_TRACKING
from src.util import configure_mlflow_experiment, save_run_id

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    data_test_path: Path = PROCESSED_DATA_DIR / "test_data.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
):
    configure_mlflow_experiment("customer_segmentation", URL_MLFLOW_TRACKING)
    mlflow.sklearn.autolog(silent=True)

    with mlflow.start_run() as run:
        # Guardar run_id
        save_run_id(run.info.run_id)

        # Prepare for training loading data, preprocessing, and training the model.
        logger.info("Loading data...")
        df = pd.read_csv(features_path)
        df = df.drop(columns=["gender"])

        X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
        X_test.to_csv(data_test_path, index=False)

        logger.info("Data loaded and split into training and test sets.")
        logger.info("Initializing KMeans with specified parameters...")
        kmn = KMeans()
        pipe = Pipeline([("scale", StandardScaler()), ("kmm", kmn)])

        # Parameter grid for GridSearchCV.
        params_grid = {"kmm__n_clusters": [2, 3, 4, 5], "kmm__algorithm": ["lloyd", "elkan"]}

        # Prepare GridSearchCV with the pipeline and parameter grid.
        grid = GridSearchCV(pipe, param_grid=params_grid, cv=5, n_jobs=-1)
        grid.fit(X_train)

        logger.info(f"Best parameters found: {grid.best_params_}")
        mlflow.log_params(grid.best_params_)
        logger.success("Model training complete.")

        # Use the best estimator from GridSearchCV directly.
        best_pipe = grid.best_estimator_

        # Output the model to folder.
        jp.dump(best_pipe, model_path)
        logger.info(f"Model saved to {model_path}.")


if __name__ == "__main__":
    app()
