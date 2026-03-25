
from pathlib import Path

import mlflow
import joblib as jp
import pandas as pd
import typer
from loguru import logger
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ds.config import MODELS_DIR, PROCESSED_DATA_DIR
from ds.util import export_metrics

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    data_test_path: Path = PROCESSED_DATA_DIR / "test_data.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    # -----------------------------------------
):
    mlflow.sklearn.autolog() 
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
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
    logger.success("Model training complete.")

    # Use the best estimator from GridSearchCV directly.
    best_pipe = grid.best_estimator_

    # Output the model to folder.
    jp.dump(best_pipe, model_path)
    logger.info(f"Model saved to {model_path}.")

    x_predict = best_pipe.predict(X_test)
    score = silhouette_score(X_test, x_predict)
    logger.info(f"Silhouette score: {score}")

    # Export metrics to JSON file.
    json_path = MODELS_DIR / "model_metrics.json"
    entry = {"silhouette_score": score, "best_params": grid.best_params_}
    export_metrics(entry, json_path)
    logger.info(f"Model metrics saved to {json_path}.")


if __name__ == "__main__":
    app()
