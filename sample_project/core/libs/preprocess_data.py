"""
This module contains the pre-processing methods.
"""
import os

import pandas as pd
from core.constants import airflow


def load_data(file_name: str = "train.csv") -> pd.DataFrame:
    """
    Load the data from the target folder.

    :param file_name: The file name.
    """
    data = pd.read_csv(os.path.join(airflow.TARGET_DATA_DIR, file_name))

    return data

def pre_process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Pre-process the data by only picking 3 features.

    :param data: The data dataframe.
    """
    x = data.iloc[:, ["Pclass", "Age", "SibSp", "Fare", "Survived"]]
    return x

def train_model(data: pd.DataFrame):
    """
    Train the logestic regression model.
    """
    print("the model training is happned.")
