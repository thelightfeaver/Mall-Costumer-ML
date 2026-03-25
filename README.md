# ds

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

<a target="_blank" href="https://www.python.org/downloads/release/python-3130/">
    <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white" />
</a>
<a target="_blank" href="https://pip.pypa.io/en/stable/">
    <img src="https://img.shields.io/badge/pip-package%20manager-3775A9?logo=pypi&logoColor=white" />
</a>

A short description of the project.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         ds and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── ds   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes ds a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

# Installation
To install the package, run the following command in the terminal:

Windows:
```cmd
scoop install make
```


MacOS:
```bash 
brew install make
```

Linux:
```bash
sudo apt-get install make
```


## Usage
To run the project, use the following command in the terminal:

```bash
make <target>
```

Where `<target>` is one of the following:

```
requirements             Install Python dependencies
clean                    Delete all compiled Python files
lint                     Lint using ruff (use `make format` to do formatting)
format                   Format source code with ruff
test                     Run tests
create_environment       Set up Python interpreter environment
mlflow                   init mlflow tracking server
mlflow_docker            Init mlflow with docker
all                      Build all pipeline stages
```

# Workflow
1. Run `make create_environment` to set up the Python environment.
2. Run `make requirements` to install the required dependencies.
3. Run `make mlflow_docker` or `make mlflow` to start the MLflow tracking server using Docker.
4. Run `make all` to execute the entire data processing and modeling pipeline.