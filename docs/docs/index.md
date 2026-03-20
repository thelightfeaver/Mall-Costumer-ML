# DS — Segmentación de Clientes

Proyecto de Data Science para segmentación de clientes usando **KMeans Clustering**. Construido con la plantilla [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/).

## Descripción

Este proyecto implementa un pipeline completo de ciencia de datos que:

1. **Carga** datos crudos de clientes (`raw.csv`) con información de género, edad, ingreso anual y puntuación de gasto.
2. **Limpia y transforma** los datos eliminando duplicados, valores nulos y renombrando columnas.
3. **Entrena** un modelo de KMeans para segmentar clientes en 3 clusters.
4. **Predice** la segmentación de nuevos datos usando el modelo entrenado.

## Dataset

El dataset contiene las siguientes columnas originales:

| Columna | Descripción |
|---------|-------------|
| `CustomerID` | Identificador único del cliente |
| `Gender` | Género del cliente (Male/Female) |
| `Age` | Edad del cliente |
| `Annual Income (k$)` | Ingreso anual en miles de dólares |
| `Spending Score (1-100)` | Puntuación de gasto (1-100) |

## Comandos rápidos

```bash
make all              # Ejecutar todo el pipeline
make requirements     # Instalar dependencias
make clean            # Limpiar archivos compilados
make lint             # Verificar estilo de código con ruff
make format           # Formatear código con ruff
make test             # Ejecutar tests con pytest
```

## Tecnologías

- **Python 3.13** — Lenguaje principal
- **pandas** — Manipulación de datos
- **scikit-learn** — Modelo KMeans y preprocesamiento
- **typer** — CLI para cada etapa del pipeline
- **loguru** — Logging
- **seaborn / matplotlib** — Visualización
- **ruff** — Linting y formateo
- **mkdocs** — Documentación