"""
Data ingestion module for Project Aegis.

This module handles loading datasets from disk and
provides basic validation and logging.
"""

from pathlib import Path
import logging

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataframe.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    logging.info(f"Loading file: {file_path}")

    df = pd.read_csv(path)

    logging.info(
        f"Successfully loaded {len(df)} rows and {len(df.columns)} columns"
    )

    return df