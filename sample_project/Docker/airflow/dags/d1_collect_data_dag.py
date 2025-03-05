"""
Dag file for the collect data task.
"""

from airflow.decorators import dag, task
from core.libs.collect_data import replace_file

default_args = {
    'owner': 'airflow',
    'retries': 1,
}


@dag(
        dag_id="data_collection_dag",
        default_args=default_args,
        schedule_interval=None,  # Run on demand
        catchup=False,
        description="DAG to collect data and store it in a target location"
)
def data_collection_pipeline():
    """
    The pipeline for collecting the data.
    """

    @task
    def collect_data(file_name: str="train.csv"):
        """
        Collect file task.

        :param file_name: The file name.
        """
        replace_file(file_name=file_name)

    collect_data()

data_collection_pipeline_dag = data_collection_pipeline()
