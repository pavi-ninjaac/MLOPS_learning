FROM python:3.10-bullseye as spark-base

ARG SPARK_VERSION=3.4.3

# Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      unzip \
      rsync \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Optional env variables
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
# Haddop is optional.
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

# Make the directories, inside the container.
RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

RUN curl -L https://archive.apache.org/dist/spark/spark-3.4.3/spark-3.4.3-bin-hadoop3.tgz -o spark-3.4.3-bin-hadoop3.tgz \
    && tar xvzf spark-3.4.3-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
    && rm -rf spark-3.4.3-bin-hadoop3.tgz


# ping is very much needed to check connectivity.
RUN apt-get update && apt-get install -y iputils-ping

# Install python deps.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3


# If you dont have it you may need to create this file.
COPY conf/spark-defaults.conf "$SPARK_HOME/conf"

# Make the binaries and scripts executable and set the PYTHONPATH.
RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

# Create a folder to store the data files.
RUN mkdir -p /opt/spark/data/
RUN chmod 777 /opt/spark/data

ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
