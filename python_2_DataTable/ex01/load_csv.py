import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return a Dataset object.

    Args:
        path (str): The path to the CSV file.

    Returns:
        Dataset: A Dataset object containing the data from the CSV file.
    """

    assert os.path.exists(path), "The specified path does not exist."
    assert path.endswith(".csv"), "The file has not .csv extension"
    file_data = pd.read_csv(path)
    assert file_data is not None, (
        "Dataset could not be loaded. Please check the file path."
    )

    shape = file_data.shape
    print(f"Loading dataset of dimensions {shape}")
    return file_data


def main():
    try:
        load("life_expectancy_years.csv")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
