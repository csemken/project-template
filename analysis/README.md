# Analysis

Note: all shell commands/scripts should be run from the main directory (the one above this one), unless otherwise indicated.

## Pre-requirements

- [Conda](https://docs.anaconda.com/miniconda/miniconda-install/)

## Setup

<!-- 0. Fill in `config/.env.template` and save it as `.env` in the main directory -->

1. Create the conda environment and install all required packages:
```shell
conda env create --prefix .conda --file environment.lock.yml
conda activate ./.conda
```

Optionally, shorten the conda prompt name:
```shell
conda config --set env_prompt '({name}) '
conda deactivate
conda activate ./.conda
```

## Add/update software

Add required conda/pip packages to `environment.yml`. To install them use:
```shell
conda install [package]
conda env export --no-build --prefix ./.conda | sed -e '1d;$d' -e '/^  - defaults$/s/  - defaults/  - nodefaults/' > environment.lock.yml
```

To update all packages use:
```shell
conda env update --prune --prefix .conda --file environment.yml
conda env export --no-build --prefix ./.conda | sed -e '1d;$d' -e '/^  - defaults$/s/  - defaults/  - nodefaults/' > environment.lock.yml
```

## Working with jupyter notebooks

Jupyter notebooks (`.ipynb` files) should be tracked with DVC, since they contain results and can be large. To track changes to the code of the notebook, we convert it into a plain python file using [jupytext](https://jupytext.readthedocs.io/).

After creating a new python notebook run `bin/add-notebook.sh notebook.ipynb` where `notebook.ipynb` is the notebook’s path.
This will create the jupytext representation (`jupytext --set-formats ipynb,auto notebook.ipynb`) and add the notebook to DVC (`dvc add notebook.ipynb`)).

To update jupytext files, run `bin/update-notebooks.sh`.
This updates all jupytext representations (`jupytext --to py --use-source-timestamp ./**/*.ipynb`) and adds the current notebooks to DVC (`dvc add ./**/*.ipynb`).
