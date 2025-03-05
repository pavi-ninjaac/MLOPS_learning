"""
This module contains the pre-processing methods.
"""
import os

import pandas as pd
from config.config_file_parser import SparkConfig
from core.constants import airflow
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession


def load_data(file_name: str = "train.csv") -> pd.DataFrame:
    """
    Load the data from the target folder into spark object.

    :param file_name: The file name.
    """
    data = pd.read_csv(os.path.join(airflow.TARGET_DATA_DIR, file_name))
    config = SparkConfig()

    # Create a spark connection and load the data.
    spark = SparkSession.builder \
                    .master("spark://172.22.0.9:7077") \
                    .appName("sample_application") \
                    .config("spark.eventLog.enabled", "false") \
                    .config("spark.ui.showConsoleProgress", "true") \
                    .getOrCreate()

    spark_df = spark.createDataFrame(data)
    return spark_df

def pre_process_data(data):
    """
    Pre-process the data by only picking 3 features.

    :param data: The data dataframe.
    """
    # Select ["Pclass", "Age", "SibSp", "Fare", "Survived"] features from the spark dataframe.
    x = data.select(["Pclass", "Age", "SibSp", "Fare", "Survived"])
    return x

def train_model(data):
    """
    Train the logestic regression model.
    """
    features = ["Pclass", "Age", "SibSp", "Fare"]
    target = "Survived"

    # Convert all the features into one column as comma separated.
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    assembled_df = assembler.transform(data).select("features", target)

    train_data, test_data = assembled_df.randomSplit([0.8, 0.2])


    lr = LinearRegression(featuresCol="features", labelCol=target)
    lr_model = lr.fit(train_data)

    # evaluate the model.
    predictions = lr_model.transform(test_data)
    evaluator = RegressionEvaluator(labelCol=target, predictionCol="prediction", metricName="rmse")
    rmse = evaluator.evaluate(predictions)

    print("the model training is happned.")
    return "The training done"

def evaluate_model():
    """
    Evaluate the model.
    """
    return "Evaluation done"
