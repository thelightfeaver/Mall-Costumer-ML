# Features — Limpieza y transformación

**Módulo:** `ds.features`

Esta etapa toma los datos interim, los limpia y genera las features finales para modelado.

## Uso

```bash
python -m ds.features
```

### Parámetros CLI

| Parámetro | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `--input-path` | `data/interim/raw_interim.csv` | Ruta al dataset interim |
| `--output-path` | `data/processed/features.csv` | Ruta de salida de features |

## ¿Qué hace?

1. **Carga** el dataset interim
2. **Detecta** valores faltantes, nulos y duplicados (logging)
3. **Elimina** filas con NaN y duplicados
4. **Elimina** la columna `CustomerID` (no es relevante para el modelo)
5. **Renombra** columnas a formato snake_case:

| Original | Renombrado |
|----------|-----------|
| `Gender` | `gender` |
| `Age` | `age` |
| `Annual Income (k$)` | `annual_income` |
| `Spending Score (1-100)` | `score` |

6. **Guarda** el dataset limpio en `data/processed/features.csv`

## Datos de salida

El archivo `features.csv` contiene:

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `gender` | str | Género (Male/Female) |
| `age` | int | Edad |
| `annual_income` | int | Ingreso anual (k$) |
| `score` | int | Puntuación de gasto (1-100) |
