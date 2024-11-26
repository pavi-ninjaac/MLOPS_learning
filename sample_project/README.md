# Sample ML project using all the learned MLOps tools.
This project focus on using the mlops tools, so will pick a very easy ml problem and include the following things in it.
- 1 | mlflow - model tracking tool
- 2 | airflow - pipelining tool
- 3 | pyspark -model scalling and distributed processing.
- 4 | python
- 5 | doghub - for hosting mlflow.
- 6 | docker - Everything will be present inside the docker containers, And i should make sure the connectivity  bwt them too.
- 7 | docker-compose - for bringing the whole setup up or down.
- 8 | makefile - individual container operations.
- 9 | syslog setup - for tracking all kind of logs and setup related to that.
- 10 | config files - for string secret information.


# multi-container environment
- created the 3 docker-compose file to bring up needed containers up.
- did spark in my own way, mlflow is easy and straight forward, airflow is it's own documentation way.
- now everything is done and all the needed containers
```
pavithra@pmurugesan-lnx1:~/projects/MLOPS_learning/sample_project/Docker/spark$(git_branch)$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS                            PORTS                                                                                    NAMES
32f9f404e572   da-spark-image          "./entrypoint.sh wor…"   3 seconds ago    Up 2 seconds                                                                                                               spark-worker1
ca54577ad1e8   da-spark-image          "./entrypoint.sh wor…"   3 seconds ago    Up 2 seconds                                                                                                               spark-worker2
f5c50a03db02   da-spark-image          "./entrypoint.sh mas…"   4 seconds ago    Up 3 seconds (health: starting)   0.0.0.0:7077->7077/tcp, :::7077->7077/tcp, 0.0.0.0:9090->8080/tcp, [::]:9090->8080/tcp   spark-master
dad9adfc15d4   da-spark-image          "./entrypoint.sh wor…"   4 minutes ago    Up 4 minutes                                                                                                               spark-worker
8cf0ba16eeac   apache/airflow:2.10.3   "/usr/bin/dumb-init …"   5 minutes ago    Up 5 minutes (healthy)            8080/tcp                                                                                 airflow_airflow-scheduler_1
bb89868ad1fc   apache/airflow:2.10.3   "/usr/bin/dumb-init …"   5 minutes ago    Up 5 minutes (healthy)            8080/tcp                                                                                 airflow_airflow-triggerer_1
50ca99a085c7   apache/airflow:2.10.3   "/usr/bin/dumb-init …"   5 minutes ago    Up 5 minutes (healthy)            8080/tcp                                                                                 airflow_airflow-worker_1
1e2327354454   apache/airflow:2.10.3   "/usr/bin/dumb-init …"   5 minutes ago    Up 5 minutes (healthy)            0.0.0.0:8080->8080/tcp, :::8080->8080/tcp                                                airflow_airflow-webserver_1
aace9dcf12c6   postgres:13             "docker-entrypoint.s…"   5 minutes ago    Up 5 minutes (healthy)            5432/tcp                                                                                 airflow_postgres_1
6fde5aab8f28   redis:7.2-bookworm      "docker-entrypoint.s…"   5 minutes ago    Up 5 minutes (healthy)            6379/tcp                                                                                 airflow_redis_1
5ba0f735c900   mlflow_mlflow           "mlflow server --bac…"   33 minutes ago   Up 33 minutes                     0.0.0.0:5000->5000/tcp, :::5000->5000/tcp                                                mlflow_mlflow_1
pavithra@pmurugesan-lnx1:~/projects/MLOPS_learning/sample_project/Docker/spark$(git_branch)$
```
- Now codes need to be present inside the core/ folder and manage everything inside this.
- But make sure to place the corresponding dag file inside the Docker/airflow/dags
- Each component has a separate docker-compose.yaml file, But still just to keep everything in one place and mention the same docker network - kept everything in one dockerfile.





# Code availability.

- All the codes should present inside the airflow container- the codes are gonna run frm the airflow container.
- there should be a connectivity bwt the airflow and mlflow and spark.
- they should all present inside the same docker network.



# errors faced and debugging steps.
- 1. should give a proper container id to the spark initialization
```
# Should be the spark master container ip.
>> docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' spark-master
172.17.0.2


spark = SparkSession.builder \
                    .master("spark://172.17.0.2:7077") \
                    .appName('sample_application') \
                    .config("spark.eventLog.enabled", "false") \
                    .config("spark.ui.showConsoleProgress", "true") \
                    .getOrCreate()
```
- 2. all the containers should present in the same network for connectivity. (airflow, mlflow and spark)
- 3. Your local spark version should match the spark version inside the container.
- 4. your local python version should match the python version inside the cotainer.
```
I am using the spark version 3.4.3 everywhere after facing the issue of
24/11/23 22:11:19 WARN TaskSetManager: Lost task 0.0 in stage 0.0 (TID 0) (172.17.0.3 executor 0): java.io.InvalidClassException: org.apache.spark.rdd.RDD; local class incompatible: stream classdesc serialVersionUID = -857609805308345919, local class serialVersionUID = -1432615955171021378

```
- 4. The dataset you use in spark should present inside the container too. mounte it.
- 5. Connect to spark inside the container.
```
pyspark --master spark://spark-master:7077
```







# Airflow - debugging
- 1. if your dags are not present, run this inside the container.

```
airflow dags list


By default, the scheduler checks the dags_folder every 30 seconds for new or updated DAG files.
The min_file_process_interval sets the minimum time in seconds that must pass before a file is processed again.
```
- Make sure you have write permission to the folders, you are writing to. NOTE