# ds.dataset

Módulo CLI para la carga de datos crudos al directorio interim.

## Función principal

### `main(input_path, output_path)`

Carga un CSV crudo y lo guarda en interim.

**Parámetros:**

- `input_path` (`Path`): Ruta al CSV de entrada. Default: `data/raw/raw.csv`
- `output_path` (`Path`): Ruta de salida. Default: `data/interim/raw_interim.csv`

**Ejemplo:**

```python
from ds.dataset import main

main(input_path="data/raw/raw.csv", output_path="data/interim/raw_interim.csv")
```

**CLI:**

```bash
python -m ds.dataset --input-path data/raw/raw.csv
```
