# Configuración

**Módulo:** `ds.config`

Centraliza las rutas y configuración global del proyecto.

## Variables de entorno

El módulo carga automáticamente variables desde un archivo `.env` usando `python-dotenv`.

## Rutas disponibles

| Variable | Ruta | Descripción |
|----------|------|-------------|
| `PROJ_ROOT` | `.` (raíz del proyecto) | Directorio raíz del proyecto |
| `DATA_DIR` | `data/` | Directorio principal de datos |
| `RAW_DATA_DIR` | `data/raw/` | Datos crudos originales |
| `INTERIM_DATA_DIR` | `data/interim/` | Datos intermedios |
| `PROCESSED_DATA_DIR` | `data/processed/` | Datos procesados para modelado |
| `EXTERNAL_DATA_DIR` | `data/external/` | Datos de fuentes externas |
| `MODELS_DIR` | `models/` | Modelos serializados |
| `REPORTS_DIR` | `reports/` | Reportes generados |
| `FIGURES_DIR` | `reports/figures/` | Gráficas y figuras |

## Logging

Se usa `loguru` como logger. Si `tqdm` está instalado, se configura para que los logs se muestren correctamente junto con barras de progreso.
