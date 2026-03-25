import json
import os

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