# Predicción

**Módulo:** `ds.modeling.predict`

Carga un modelo entrenado y realiza predicciones sobre nuevos datos.

## Uso

```bash
python -m ds.modeling.predict
```

### Parámetros CLI

| Parámetro | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `--features-path` | `data/processed/test_features.csv` | Ruta a las features de test |
| `--model-path` | `models/model.pkl` | Ruta al modelo entrenado |
| `--predictions-path` | `data/processed/test_predictions.csv` | Ruta de salida de predicciones |

## ¿Qué hace?

1. **Carga** el modelo serializado desde `models/model.pkl` con `joblib`
2. Lee las features de entrada
3. Genera predicciones de cluster para cada registro
