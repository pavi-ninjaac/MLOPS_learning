from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False, # dependency task
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'mysql_etl_dag',  # DAG name
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2023, 7, 21),
    catchup=False, # If the dag enabled after few days of start day, should we run the task for the start day or not.
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='bash /home/pavithra/projects/MLOPS_learning/3_Airflow/scripts/wrapper_script.sh ',#give a space after the path
    dag=dag,
)