# ds.features

Módulo CLI para limpieza de datos y generación de features.

## Función principal

### `main(input_path, output_path)`

Limpia el dataset interim y genera features procesadas.

**Parámetros:**

- `input_path` (`Path`): Ruta al CSV interim. Default: `data/interim/raw_interim.csv`
- `output_path` (`Path`): Ruta de salida. Default: `data/processed/features.csv`

**Operaciones:**

1. Elimina filas con NaN
2. Elimina duplicados
3. Elimina columna `CustomerID`
4. Renombra columnas a snake_case

**CLI:**

```bash
python -m ds.features --input-path data/interim/raw_interim.csv
```
