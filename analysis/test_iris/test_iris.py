"""Test module that saves a statistic about the iris test data into release"""

from pathlib import Path

import pandas as pd

from analysis import utils


def main() -> int:
    # load data
    df_iris = pd.read_csv(
        "data/raw/test_iris/iris.csv",
        names=["sepal_length", "sepal_width", "pedal_length", "pedal_width", "class"],
    )

    # save number of observations as autofilling value
    release_folder = Path("data/release/test_iris/")
    release_folder.mkdir(exist_ok=True)
    autofilling = {
        "iris_obs": len(df_iris),
    }
    (release_folder / "autofilling.tex").write_text(
        utils.dict_to_autofilling_values(autofilling)
    )


if __name__ == "__main__":
    raise SystemExit(main())
