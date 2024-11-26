"""
This file contains information about collecting file from one place and put in other place
without any modification :) .
Sounds useless right. this is just to practice the multi-dag things
"""

import os

import pandas as pd
from constants import airflow


def replace_file(file_name: str) -> None:
    """
    Re-place the file from one path to target path for no fucking reason.
    """
    data = pd.read_csv(os.path.join(airflow.SOURCE_DATA_DIR, file_name))
    target_file_path :str = os.path.join(airflow.TARGET_DATA_DIR, file_name)

    data.to_csv(target_file_path, index=False)
    print(f"Data saved to the target directory {target_file_path}")
