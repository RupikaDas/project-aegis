#Data ingestion module for Project Aegis.

#This module handles loading datasets from disk and provides basic validation and logging.

from pathlib import Path
import logging

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_csv(file_path: str) -> pd.DataFrame:

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