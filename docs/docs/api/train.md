# ds.modeling.train

Módulo CLI para entrenamiento del modelo KMeans.

## Función principal

### `main(features_path, data_test_path, model_path)`

Entrena un modelo KMeans(n_clusters=3) y lo serializa con joblib.

**Parámetros:**

- `features_path` (`Path`): Ruta a features. Default: `data/processed/features.csv`
- `data_test_path` (`Path`): Ruta para guardar test split. Default: `data/processed/test_data.csv`
- `model_path` (`Path`): Ruta del modelo. Default: `models/model.pkl`

**Pipeline:**

1. `LabelEncoder` sobre columna `gender`
2. `train_test_split` (80/20, random_state=42)
3. `KMeans.fit()` sobre datos de entrenamiento
4. `joblib.dump()` del modelo

**CLI:**

```bash
python -m ds.modeling.train --features-path data/processed/features.csv
```
