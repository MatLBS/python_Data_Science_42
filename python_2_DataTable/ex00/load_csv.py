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

    if not isinstance(path, str):
        return None
    if os.path.exists(path) is False:
        return None
    if not path.endswith(".csv"):
        return None
    try:
        file_data = pd.read_csv(path)
    except Exception:
        return None
    if file_data is None:
        return None

    shape = file_data.shape
    print(f"Loading dataset of dimensions {shape}")
    return file_data


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
