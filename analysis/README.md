# Analysis

Note: all shell commands/scripts should be run from the main directory (the one above this one), unless otherwise indicated.

## Pre-requirements

- [Pixi](https://pixi.sh/latest/installation/)

## Setup

<!-- 0. Fill in `config/.env.template` and save it as `.env` in the main directory -->

1. Create the pixi environment and install all required packages:
```shell
pixi install --freeze
```

2. Get data files using [dvc](https://dvc.org/). This requires you to authenticate with a Google account that has access to the GCP service account below, which is used to access our GCP storage bucket.
```shell
gcloud auth application-default login --impersonate-service-account="cs-dvc@csemken.iam.gserviceaccount.com"
dvc pull
```

3. Set up R environment
```shell
R -e "IRkernel::installspec()"
Rscript -e 'install.packages("vscDebugger", repos = "https://manuelhentschel.r-universe.dev")'
```

4. (Optional) Install the [pre-commit](https://pre-commit.com/) git hooks. This will automatically run linters before `git commit`. It will also install the dvc hooks, which automatically run `dvc checkout` and `dvc push` after `git checkout` and before `git push`, respectively.
```shell
pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit
```

## Reproducing the analysis

To execute any modules after inputs or code have changed, run
```
dvc repro
```

To reproduce the entire analysis, run
```
dvc repro --force
```

## Working with jupyter notebooks

Jupyter notebooks (`.ipynb` files) should be tracked with DVC, since they contain results and can be large. To track changes to the code of the notebook, we convert it into a plain python file using [jupytext](https://jupytext.readthedocs.io/).

After creating a new python notebook run `bin/add-notebook.sh notebook.ipynb` where `notebook.ipynb` is the notebook’s path.
This will create the jupytext representation (`jupytext --set-formats ipynb,auto notebook.ipynb`) and add the notebook to DVC (`dvc add notebook.ipynb`)).

To update jupytext files, run `bin/update-notebooks.sh`.
This updates all jupytext representations (`jupytext --to py --use-source-timestamp ./**/*.ipynb`) and adds the current notebooks to DVC (`dvc add ./**/*.ipynb`).
