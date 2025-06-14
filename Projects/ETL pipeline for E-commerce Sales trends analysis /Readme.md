
# E-commerce Sales Trends Analysis

This project focuses on building an end-to-end **ETL pipeline** for analyzing E-commerce sales data. The data is ingested from an S3 bucket, processed using Apache Spark on Databricks, and visualized using Amazon QuickSight.

---

## 🔧 Technologies Used

### 1. **Amazon S3**
Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Used here as both source and destination for raw and transformed data.

### 2. **Databricks**
Databricks is a cloud-based platform that provides a collaborative environment for working with Apache Spark. It simplifies big data processing and machine learning workflows.

### 3. **Apache Spark**
Apache Spark is an open-source, distributed computing system used for big data processing and analytics. It supports in-memory computation and is highly efficient for ETL tasks.

### 4. **PySpark**
PySpark is the Python API for Spark. It enables working with Spark using Python programming.

### 5. **AWS QuickSight**
QuickSight is a cloud-powered business analytics service that allows you to create and publish interactive dashboards. It is used here to visualize transformed and cleaned sales data.

### 6. **Python**
Python is used for scripting tasks like uploading data to S3 and initiating Spark transformations.

---

## 🔄 ETL Pipeline Overview

```text
+-------------+        +----------------+        +----------------+        +-------------------+        +------------------+
| Raw CSV     | -----> | Python Script  | -----> | Amazon S3      | -----> | Databricks (ETL)  | -----> | Amazon S3 Clean  |
| (Local)     |        | (Upload File)  |        | (Raw Layer)    |        | Spark Transform   |        | Data Layer       |
+-------------+        +----------------+        +----------------+        +-------------------+        +------------------+
                                                                                                                |
                                                                                                                |
                                                                                                       +------------------+
                                                                                                       | AWS QuickSight   |
                                                                                                       | (Visualization)  |
                                                                                                       +------------------+
```

---

## ✅ Key Steps

1. Uploaded raw E-commerce data CSV to S3 using a Python script.
2. Read the data from S3 into Databricks using `spark.read.csv()`.
3. Cleaned and transformed the data using PySpark DataFrame operations.
4. Saved the transformed data back into a different S3 bucket/folder.
5. Connected Amazon QuickSight to the transformed data in S3.
6. Created visualizations and a dashboard to analyze sales trends.

---

## 📊 Key Learnings

- Gained hands-on experience in real-world ETL using Databricks and Spark.
- Understood AWS data flow with S3, QuickSight, and IAM integration.
- Practiced data transformation logic and PySpark syntax.
- Built meaningful visualizations on cleaned data to derive business insights.

---

## 📁 Example Python Upload Script

```python
import boto3

s3 = boto3.client('s3')

with open("sales_data.csv", "rb") as f:
    s3.upload_fileobj(f, "your-bucket-name", "raw/sales_data.csv")
```

---

## 📘 Sample PySpark Code in Databricks

```python
df = spark.read.csv("s3a://your-bucket-name/raw/sales_data.csv", header=True, inferSchema=True)

# Cleaning and transformation
df_clean = df.dropna().withColumnRenamed("Order Date", "order_date")

# Write cleaned data back to S3
df_clean.write.mode("overwrite").csv("s3a://your-bucket-name/clean/sales_data/")
```

---

## 📈 Sample QuickSight Views

- Total Sales by Country
- Monthly Sales Trends
- Category-wise Revenue Share
- Top Performing Products

---
