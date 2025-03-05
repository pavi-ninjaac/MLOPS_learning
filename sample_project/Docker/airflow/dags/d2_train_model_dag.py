"""
Dag file for model training.
"""

from airflow.decorators import dag, task
from airflow.sensors.external_task import ExternalTaskSensor
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
        dag_id="train_model",
        default_args=default_args,
        schedule_interval=None,  # Run on demand
        catchup=False,
        description="DAG to preprocess data and train the model."
)
def model_training_pipeline():
    """
    The pipeline for training the model and evaluation.
    """
    # This will just wait for the task to be done, it won't trigegr the dag.
    wait_for_data = ExternalTaskSensor(
        task_id="wait_for_data",
        external_dag_id="data_collection_dag",
        external_task_id=None,  # Wait for the entire DAG
        mode="poke",
        timeout=600,  # Timeout after 10 minutes
    )

    @task
    def load_data_task():
        """
        Load the data.
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
    wait_for_data >> data

model_training_pipeline_dag = model_training_pipeline()
