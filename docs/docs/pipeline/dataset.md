# Dataset — Carga de datos

**Módulo:** `ds.dataset`

Esta etapa carga el archivo CSV crudo y lo guarda en el directorio interim sin transformaciones.

## Uso

```bash
python -m ds.dataset
```

### Parámetros CLI

| Parámetro | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `--input-path` | `data/raw/raw.csv` | Ruta al archivo CSV de entrada |
| `--output-path` | `data/interim/raw_interim.csv` | Ruta de salida del archivo interim |

### Ejemplo con rutas personalizadas

```bash
python -m ds.dataset --input-path data/raw/otro.csv --output-path data/interim/otro_interim.csv
```

## ¿Qué hace?

1. Lee el archivo CSV desde `data/raw/`
2. Registra en log la forma del dataset y las columnas
3. Guarda el dataset en `data/interim/`

## Datos de entrada

El archivo `raw.csv` contiene:

| Columna | Tipo | Ejemplo |
|---------|------|---------|
| CustomerID | int | 1 |
| Gender | str | Male, Female |
| Age | int | 19 |
| Annual Income (k$) | int | 15 |
| Spending Score (1-100) | int | 39 |
