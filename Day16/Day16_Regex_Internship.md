
# **Day 16 - Regex Software Services Internship**

## **Overview**

Today marked the beginning of our Data Engineering training. We explored the distinctions between Data Science and Data Engineering, followed by an in-depth look at Big Data concepts, Hadoop architecture, and a brief introduction to `boto3` for AWS interactions.

---

## **Difference Between Data Science and Data Engineering**

| Feature | Data Scientist | Data Engineer |
|--------|----------------|---------------|
| Role | Analyzes data to derive insights | Builds and manages data pipelines |
| Tools | Python, R, Machine Learning Libraries | Hadoop, Spark, Kafka |
| Output | Models, dashboards | Datasets, infrastructure |
| Focus | Statistics, ML, Visualization | ETL, Data Warehousing, Processing |

---

## **Big Data**

Big Data refers to extremely large datasets that cannot be managed or processed using traditional data processing tools.

### **5 V’s of Big Data**

1. **Volume** – Amount of data.
2. **Velocity** – Speed of data generation and processing.
3. **Variety** – Different types of data (structured, unstructured).
4. **Veracity** – Data quality and trustworthiness.
5. **Value** – Worth derived from the data.

---

## **Distributed Computing**

Distributed computing involves dividing a large computational task among multiple systems (nodes) that work together. This improves performance and fault tolerance.

**Diagram:**
```
+------------+      +------------+
|   Client   | ---> |   Master   | ---> Controls Tasks
+------------+      +------------+
                          |
                -------------------
                |        |        |
              Node1   Node2    Node3
```

---

## **Introduction to Hadoop**

Hadoop is an open-source framework that allows for the distributed processing of large datasets across clusters of computers.

### **Why Hadoop?**

- Manages large volumes of data
- Cost-effective
- Scalable and fault tolerant

### **Versions of Hadoop**

| Version | Description |
|---------|-------------|
| Hadoop 1.x | Uses MapReduce only for processing |
| Hadoop 2.x (YARN) | Introduced YARN for better resource management and scalability |

### **Storage in Hadoop**

- **HDFS** – Hadoop Distributed File System
- **Blocks** – Data is stored in blocks (default size 64MB or 128MB)
- **NameNode** – Stores metadata
- **DataNode** – Stores actual data

### **Processing in Hadoop**

- **MapReduce** – A programming model for processing large datasets
- **YARN (Yet Another Resource Negotiator)** – Resource manager in Hadoop 2.x

### **Diagram: Hadoop Storage and Processing**

```
+-------------+       +-------------------+
|   Client    |-----> |     NameNode      |
+-------------+       +-------------------+
                            |
            -------------------------------------
            |              |                 |
        +--------+     +--------+       +--------+
        |DataNode|     |DataNode|       |DataNode|
        +--------+     +--------+       +--------+
```

---

## **Hadoop Fault Tolerance**

Hadoop is fault tolerant because:

- It stores multiple replicas of data blocks.
- If one DataNode fails, the data is retrieved from another.
- NameNode periodically receives heartbeat signals from DataNodes.

**Single Point of Failure (SPOF)** is managed using **Secondary NameNode** in Hadoop 1 and **High Availability (HA)** in Hadoop 2.

---

## **YARN (Yet Another Resource Negotiator)**

YARN separates resource management and job scheduling, improving efficiency and scalability.

### **Components**:

- **Resource Manager** – Manages cluster resources.
- **Node Manager** – Manages execution on each node.
- **Application Master** – Manages individual job execution.

---

## **Boto3 (AWS SDK for Python)**

Boto3 allows Python developers to write software that makes use of Amazon services like S3, EC2, etc.

**Common Uses:**
- Upload/download files to S3
- Start/stop EC2 instances
- Manage AWS resources programmatically

Example (upload to S3):
```python
import boto3

s3 = boto3.client('s3')
s3.upload_file('local_file.txt', 'bucket-name', 'file.txt')
```

---

✅ **End of Day 16**
