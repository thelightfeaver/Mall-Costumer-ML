# ds.modeling.predict

Módulo CLI para predicción con modelo entrenado.

## Función principal

### `main(features_path, model_path, predictions_path)`

Carga un modelo KMeans serializado y genera predicciones.

**Parámetros:**

- `features_path` (`Path`): Ruta a features de test. Default: `data/processed/test_features.csv`
- `model_path` (`Path`): Ruta al modelo. Default: `models/model.pkl`
- `predictions_path` (`Path`): Ruta de salida. Default: `data/processed/test_predictions.csv`

**CLI:**

```bash
python -m ds.modeling.predict --model-path models/model.pkl
```
