"""
Dag file for model training.
"""
import pandas as pd
from airflow.decorators import dag, task
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from core.libs.preprocess_data import (
    evaluate_model,
    load_data,
    pre_process_data,
    train_model,
)

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

@dag(
        dag_id="train_model_2",
        default_args=default_args,
        schedule_interval=None,  # Run on demand
        catchup=False,
        description="DAG to preprocess data and train the model."
)
def model_training_pipeline():
    """
    The pipeline for training the model and evaluation.
    """

    # Step 1: Trigger the data collection DAG
    trigger_data_collection = TriggerDagRunOperator(
        task_id="trigger_data_collection",
        trigger_dag_id="data_collection_dag",  # DAG ID of the data collection DAG
        wait_for_completion=True,  # Wait for the triggered DAG to complete
        reset_dag_run=True,  # Reset any previous unfinished DAG runs
    )

    @task
    def load_data_task():
        """
        Load the data into the spark object.
        """
        return load_data()

    @task
    def pre_process_data_task(data):
        """
        preprocess the data.
        """
        return pre_process_data(data)

    @task
    def train_model_task(data):
        return train_model(data)

    @task
    def evaluate_model_task(model):
        return evaluate_model()

     # Setting dependencies
    data = load_data_task()
    processed_data = pre_process_data_task(data)
    trained_model = train_model_task(processed_data)
    evaluate_model_task(trained_model)

    # Ensure the pipeline waits for the data collection DAG to complete
    trigger_data_collection >> data

model_training_pipeline_dag = model_training_pipeline()
