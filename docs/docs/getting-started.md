# Primeros pasos

## Requisitos previos

- Python 3.13
- Conda (opcional, para entorno virtual)
- pip

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd ds
```

### 2. Crear entorno virtual (opcional)

```bash
make create_environment
conda activate ds
```

### 3. Instalar dependencias

```bash
make requirements
```

Esto instalará todos los paquetes listados en `requirements.txt`:

- pandas, numpy, scikit-learn — procesamiento y modelado
- seaborn, matplotlib — visualización
- typer — interfaz de línea de comandos
- loguru — logging
- ruff — linting/formateo
- mkdocs — documentación
- pytest — testing

## Ejecutar el pipeline completo

```bash
make all
```

Esto ejecuta en orden: `data → features → train → predict`.

### Ejecutar etapas individualmente

```bash
# 1. Cargar datos crudos → interim
python -m ds.dataset

# 2. Limpiar y generar features → processed
python -m ds.features

# 3. Entrenar modelo KMeans
python -m ds.modeling.train

# 4. Predecir con modelo entrenado
python -m ds.modeling.predict
```

## Exploración de datos

El notebook de exploración se encuentra en `notebooks/1-exploration.ipynb`. Contiene:

- Carga del dataset procesado
- Análisis de outliers con IQR
- Visualización con boxplot
- Distribución por género

## Documentación

Para servir la documentación localmente:

```bash
cd docs
mkdocs serve
```

Luego abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.
