
# 1 | What is Apache Spark, and how does it differ from Hadoop MapReduce?

spark is a distributed computing system for fast, scalable processing of large datasets. It is widely used for big data analytics, machine learning

- Speed:

Spark is significantly faster because it processes data in memory, while MapReduce writes intermediate data to disk.

- Ecosystem Integration:

Spark includes libraries for SQL (Spark SQL), machine learning (MLlib), streaming (Spark Streaming), and graph processing (GraphX). MapReduce relies on separate tools (e.g., Hive, Pig).

- Data Processing:

Spark supports batch, real-time, interactive, and graph processing. MapReduce is limited to batch processing.


# 2 | * Explain the Spark execution model and the difference between transformations and actions.

- Transformations:

Define operations to transform data (e.g., map, filter, flatMap).
Lazy Evaluation: Do not execute immediately; only create a DAG.
Examples: map(), filter(), groupByKey().
- Actions:

Trigger execution of the DAG, performing transformations and returning results.
Examples: collect(), count(), saveAsTextFile().

# 3 | what is RDD
RDD - resilient Distributed Dataset

- this is the fundamental data structure in Apache Spark,
- This type of dataset is unchangeable and immutable, which means it will automatically recover if there is a system failure
- this type of datasets stored across the cluster nodes, making the distirbuted processing effecient. Distributed: Data is partitioned across multiple nodes for parallel processing.
- Lazy Evaluation: Operations are not executed immediately but are recorded as a lineage graph.

Types of RDD Operations:
- Transformations: Create a new RDD from an existing one (e.g., map, filter, flatMap).
- Actions: Trigger computation and return results (e.g., collect, count, saveAsTextFile).


# 4 | DataFrame:

- Definition: A higher-level abstraction built on RDDs, organized into named columns (like a table in SQL).
- Features: Optimized by Catalyst for execution, supports SQL-like operations.
- Use Case: Efficient handling of structured data and query optimization.

# 5 | How does PySpark use partitions?



# 6 | Role of Driver and Executors in Spark
Driver:

- Definition: The central coordinator of a Spark application.
- Responsibilities:
    - Converts the user-defined application into a Directed Acyclic Graph (DAG).
    - Manages job scheduling and splits the DAG into stages.
    - Sends tasks to executors for execution.
    - Collects and tracks task execution results.

Lifecycle: The driver runs throughout the application and monitors progress.

Executors:

- Definition: Worker processes running on cluster nodes.
- Responsibilities:
    - Execute the tasks assigned by the driver.
    - Store data in-memory (caching) for faster computation.
    - Report task progress and results back to the driver.

Structure:
Each executor has its own memory and CPU cores for processing.

# 7 |   so for each action one job will be there ?
yes each action will trigger a separate job,
```
rdd = spark.parallelize([1, 2, 3, 4, 5])
rdd_sum = rdd.reduce(lambda x, y: x + y)  # First job
rdd_count = rdd.count()                  # Second job
Each action (reduce() and count()) triggers a separate job.
```
note:
- Jobs are independent; each action processes the data from scratch unless caching/persisting is used.

# 8 | components of a job:
DAG (Directed Acyclic Graph):

- A job is divided into multiple stages using a DAG of execution.
- The DAG represents the logical flow of transformations and their dependencies.

Stages:

- Each job is split into stages based on shuffle boundaries.
- Stages represent a set of tasks that can be executed in parallel.
Two types:
- Shuffle Map Stage: Produces intermediate results for shuffling.
- Result Stage: Produces the final output.

Tasks:

- Each stage consists of tasks executed in parallel on partitions of the data.
- Tasks are the smallest unit of work in Spark.

Driver:

- Coordinates the job execution, creates stages, and schedules tasks.

Executors:

- Perform the actual computation and store intermediate results.

# Questions for machine learning:
# 1 | What is MLlib in Spark?
MLlib (Machine Learning Library) is Spark's distributed machine learning framework. It simplifies scalable machine learning by providing efficient, parallelized implementations of common algorithms.

Distributed Processing:

- Leverages Spark’s in-memory computation and parallel processing capabilities.
- Works seamlessly across a cluster for scalability.

Algorithms:

- Supports a variety of ML tasks:
- Classification: Logistic Regression, SVM.
- Regression: Linear Regression.
- Clustering: K-Means.
- Recommendation: ALS (Collaborative Filtering).

Pipelines:

-Provides an abstraction for building ML workflows (data preprocessing, model training, evaluation).

Integration:

- Integrates with DataFrames for structured data handling.
- Works with Spark SQL for feature engineering and querying data.

# 2 | What are ML Pipelines in Spark?
like scikit-learn here also we have pipeline, which is used to define the flow of the data pre-processing steps -- getting -- scallling- tranforming - fitting the model
-  are a way to structure and organize entire machine learning workflows into a series of sequential steps.
```
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("MLPipelineExample").getOrCreate()

# Load dataset
data = spark.read.csv("data.csv", header=True, inferSchema=True)

# Define feature columns
feature_columns = ["feature1", "feature2", "feature3"]

# Define stages of the pipeline
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
lr = LogisticRegression(featuresCol="scaled_features", labelCol="label")

# Create pipeline
pipeline = Pipeline(stages=[assembler, scaler, lr])

# Split data into training and test sets
train_data, test_data = data.randomSplit([0.8, 0.2])

# Train the pipeline
model = pipeline.fit(train_data)

# Make predictions
predictions = model.transform(test_data)

```
# 3 | Explain the difference between StringIndexer and OneHotEncoder in Spark.

StringIndexer - label encoding in scikit-learn
OneHotEncoder - one-hot encoding in scikit-learn

# 4 | 