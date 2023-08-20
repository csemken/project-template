"""Test module that saves a statistic about the iris test data into release"""

from pathlib import Path

import pandas as pd


def main() -> int:
    # load data
    df_iris = pd.read_csv(
        "data/raw/test_iris/iris.csv",
        names=["sepal_length", "sepal_width", "pedal_length", "pedal_width", "class"],
    )

    # save number of observations as autofilling value
    Path("data/release/test_iris.tex").write_text(
        rf"\newcommand{{\irisobs}}{{\textnormal{{{len(df_iris)}}}}}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
