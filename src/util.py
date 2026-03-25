import json
import os

import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient


def export_metrics(metrics: dict, path: str):
    """
    Export metrics to a JSON file. If the file exists, append the new metrics to the existing data.

    Args:
        metrics (dict): A dictionary containing the metrics to be exported.
        path (str): The file path where the metrics should be saved.
    """
    if os.path.exists(path):
        with open(path, "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(metrics)
    with open(path, "w") as f:
        json.dump(history, f, indent=4)


def configure_mlflow_experiment(experiment_name: str, tracking_uri: str):
    """
    Configure MLflow experiment by setting the tracking URI and ensuring the experiment exists (creating it if necessary).
    
    Args:
        experiment_name (str): The name of the MLflow experiment.
        tracking_uri (str): The URI of the MLflow tracking server.

    """

    # Set the tracking URI and ensure the experiment exists (create if it doesn't).
    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()
    experiments = client.search_experiments(
        view_type=ViewType.ALL,
        filter_string=f"name = '{experiment_name}'",
    )

    # If the experiment exists but is not active, restore it. If it doesn't exist, create it.
    if experiments:
        experiment = experiments[0]
        if experiment.lifecycle_stage != "active":
            client.restore_experiment(experiment.experiment_id)
    else:
        client.create_experiment(experiment_name)

    mlflow.set_experiment(experiment_name)
