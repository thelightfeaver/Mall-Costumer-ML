import joblib as jp
import pandas as pd
from sklearn.metrics import silhouette_score

from src.config import MODELS_DIR, PROCESSED_DATA_DIR


def test_code_is_tested():
    model = jp.load(MODELS_DIR / "model.pkl")
    test_data = pd.read_csv(PROCESSED_DATA_DIR / "test_data.csv")

    y_pred = model.predict(test_data)
    assert len(y_pred) == len(test_data), "Predictions should match the number of samples"
    score = silhouette_score(test_data, y_pred)
    assert score > 0.2, "Silhouette score should be greater than 0.2"
   
