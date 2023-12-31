# Analysis

Note: all shell commands/scripts should be run from the main directory (the one above this one), unless otherwise indicated.

## Pre-requirements

- Python ≥3.10
- Python module venv (included in Python except on Debian/Ubuntu/etc)

## Setup

<!-- 0. Fill in `config/.env.template` and save it as `.env` in the main directory -->

1. Create a [virtual environment](https://docs.python.org/3/library/venv.html):
```shell
python3 -m venv .venv
```

2. Install the requirements:
```shell
source .venv/bin/activate
pip3 install -r config/requirements.txt
```

3. Get data files using [dvc](https://dvc.org/). This requires you to authenticate with a Google account that has access to our dvc Google Drive folder.
```shell
dvc pull
```

(On a server, open the authentication URL on a PC, follow the instructions, copy the URL and run `cd /tmp && wget <URL>` in a different terminal on the server.)

4. (Optional) Install the [pre-commit](https://pre-commit.com/) git hooks. This will automatically run linters before `git commit`. It will also install the dvc hooks, which automatically run `dvc checkout` and `dvc push` after `git checkout` and before `git push`, respectively.
```shell
pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit
```

5. (Optional) Use VScode configuration, by creating a symlink:
```shell
ln -s config/.vscode
```

Go to extensions and install the recommended extensions.

## Reproducing the analysis

To execute any modules after inputs or code have changed, run
```
dvc repro
```

To reproduce the entire analysis, run
```
dvc repro --force
```

## Adding/updating python requirements

Add required packages to `config/requirements.in`. To install new requirements use:
```shell
source .venv/bin/activate && pip-compile config/requirements.in && pip-sync config/requirements.txt
```

To update requirements use:
```shell
source .venv/bin/activate && pip-compile --upgrade config/requirements.in && pip-sync config/requirements.txt
```

## Working with jupyter notebooks

Jupyter notebooks (`.ipynb` files) should be tracked with DVC, since they contain results and can be large. To track changes to the code of the notebook, we convert it into a plain python file using [jupytext](https://jupytext.readthedocs.io/).

After creating a new python notebook run `bin/add-notebook.sh notebook.ipynb` where `notebook.ipynb` is the notebook’s path.
This will create the jupytext representation (`jupytext --set-formats ipynb,auto notebook.ipynb`) and add the notebook to DVC (`dvc add notebook.ipynb`)).

To update jupytext files, run `bin/update-notebooks.sh`.
This updates all jupytext representations (`jupytext --to py --use-source-timestamp ./**/*.ipynb`) and adds the current notebooks to DVC (`dvc add ./**/*.ipynb`).
