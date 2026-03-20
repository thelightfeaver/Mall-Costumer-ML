# Estructura del Proyecto

```
ds/
├── Makefile                  # Comandos de automatización (make all, make test, etc.)
├── pyproject.toml            # Metadatos del paquete y configuración de ruff
├── README.md                 # Descripción general del proyecto
├── requirements.txt          # Dependencias de Python
│
├── data/
│   ├── external/             # Datos de fuentes externas
│   ├── raw/                  # Datos originales sin modificar
│   │   └── raw.csv           # Dataset de clientes (CustomerID, Gender, Age, etc.)
│   ├── interim/              # Datos intermedios transformados
│   │   └── raw_interim.csv   # Copia limpia del dataset crudo
│   └── processed/            # Datos finales listos para modelado
│       └── features.csv      # Features procesados (gender, age, annual_income, score)
│
├── docs/                     # Documentación con MkDocs
│   ├── mkdocs.yml
│   └── docs/
│
├── ds/                       # Código fuente del proyecto
│   ├── __init__.py
│   ├── config.py             # Rutas y configuración global
│   ├── dataset.py            # Carga de datos: raw → interim
│   ├── features.py           # Limpieza y feature engineering: interim → processed
│   ├── plots.py              # Generación de visualizaciones
│   └── modeling/
│       ├── __init__.py
│       ├── train.py          # Entrenamiento del modelo KMeans
│       └── predict.py        # Predicción con modelo entrenado
│
├── models/                   # Modelos serializados (.pkl)
├── notebooks/                # Notebooks de exploración
│   └── 1-exploration.ipynb
├── reports/
│   └── figures/              # Gráficas generadas
├── references/               # Diccionarios de datos y materiales de referencia
└── tests/
    └── test_data.py          # Tests del proyecto
```

## Flujo de datos

```
raw.csv → dataset.py → raw_interim.csv → features.py → features.csv → train.py → model.pkl
                                                                      → predict.py → predicciones
```

| Etapa | Entrada | Salida | Módulo |
|-------|---------|--------|--------|
| Carga | `data/raw/raw.csv` | `data/interim/raw_interim.csv` | `ds.dataset` |
| Features | `data/interim/raw_interim.csv` | `data/processed/features.csv` | `ds.features` |
| Entrenamiento | `data/processed/features.csv` | `models/model.pkl` | `ds.modeling.train` |
| Predicción | `data/processed/test_features.csv` | `data/processed/test_predictions.csv` | `ds.modeling.predict` |
