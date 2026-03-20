# Entrenamiento — KMeans Clustering

**Módulo:** `ds.modeling.train`

Entrena un modelo de **KMeans** con 3 clusters para segmentar clientes.

## Uso

```bash
python -m ds.modeling.train
```

### Parámetros CLI

| Parámetro | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `--features-path` | `data/processed/features.csv` | Ruta a las features |
| `--data-test-path` | `data/processed/test_data.csv` | Ruta para guardar datos de test |
| `--model-path` | `models/model.pkl` | Ruta para guardar el modelo entrenado |

## ¿Qué hace?

1. **Carga** `features.csv`
2. **Codifica** la columna `gender` con `LabelEncoder` (Male=1, Female=0)
3. **Divide** los datos en train/test (80/20) con `train_test_split`
4. **Guarda** los datos de test en `data/processed/test_data.csv`
5. **Entrena** un modelo `KMeans(n_clusters=3, random_state=42)`
6. **Serializa** el modelo con `joblib` en `models/model.pkl`

## Modelo

- **Algoritmo:** KMeans
- **Número de clusters:** 3
- **Random state:** 42
- **Preprocesamiento:** LabelEncoder para la columna `gender`
- **Split:** 80% train, 20% test
