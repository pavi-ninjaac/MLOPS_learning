FROM apache/airflow:2.10.3
COPY ./airflow/requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
