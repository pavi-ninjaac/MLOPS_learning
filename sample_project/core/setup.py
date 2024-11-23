from pyspark.sql import SparkSession


def setup_pyspark_cluster() -> SparkSession:
    """
    Setup the spark session.
    """
    spark:SparkSession = SparkSession.builder \
                            .master("spark://172.17.0.2:7077") \
                            .appName('sample_application') \
                            .config("spark.eventLog.enabled", "false") \
                            .config("spark.ui.showConsoleProgress", "true") \
                            .getOrCreate()
    return spark
