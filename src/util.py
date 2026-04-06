import os

import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient

RUN_FILE = "run_id.txt"


def load_run_id() -> str:
    """
    Load the MLflow run ID from a file. If the file does not exist, return None.

    Returns:
        str: The MLflow run ID, or None if the file does not exist.
    """
    if os.path.exists(RUN_FILE):
        with open(RUN_FILE, "r") as f:
            return f.read().strip()
    return None


def save_run_id(run_id: str):
    """
    Save the MLflow run ID to a file.

    Args:
        run_id (str): The MLflow run ID to be saved.
    """
    with open(RUN_FILE, "w") as f:
        f.write(run_id)


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
    mlflow.config.enable_system_metrics_logging()
    mlflow.set_experiment(experiment_name)
