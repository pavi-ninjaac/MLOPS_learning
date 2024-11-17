# What is Airflow and why it is used for.
- This is basically like luigi(I have used in sandvine). A automatic pipelining and scheduling tool. Where you can sya run this tasks in a order A, B, C at every 5 mins.
- Airflow is most famous for the ML related tasks, where you can automaically setup the getting data from database, Data manipulation, model training, model deployment.
- you can monitor the tasks, logs, put alerts if anything go wrong.

# Download it using Docker,
- don't wanna download in local machine, because I'll be using it with cloud.
- https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

```
Some directories in the container are mounted, which means that their contents are synchronized between your computer and the container. -to make things persistent.


./dags - you can put your DAG files here.

./logs - contains logs from task execution and scheduler.

./config - you can add custom log parser or add airflow_local_settings.py to configure cluster policy.

./plugins - you can put your custom plugins here.

This file uses the latest Airflow image (apache/airflow). If you need to install a new Python library or system library, you can build your image.


```
docker-compose file:
```
# YOu have to make sure you have these folders before running the docker compose.
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'


# initialize the database
docker compose up airflow-init

# Running Airflow
docker compose up

```

```
Accessing the web interface
Once the cluster has started up, you can log in to the web interface and begin experimenting with DAGs.

The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow.

```
cleaning up
```
docker compose down --volumes --rmi all
```


# Placement of files.
- you should paste your DAG file inside the ./dags folder. dag file calls -> bash script -> actual script.
