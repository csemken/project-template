# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

import pandas as pd

df_iris = pd.read_csv(
    "../../../data/raw/test_iris/iris.csv",
    names=["sepal_length", "sepal_width", "pedal_length", "pedal_width", "class"],
)
df_iris.head(2)
