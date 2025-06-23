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

    if os.path.exists(path) is None:
        return None
    if not path.endswith(".csv"):
        return None
    file_data = pd.read_csv(path)
    if file_data is None:
        return None

    shape = file_data.shape
    print(f"Loading dataset of dimensions {shape}")
    return file_data
