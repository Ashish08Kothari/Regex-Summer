
# Day 22 - Data Engineering Internship at Regex Software Services

## 📅 Date: 2025-06-02

---

## 🧠 Topics Covered

### 1. OLTP vs OLAP

| Feature            | OLTP (Online Transaction Processing)         | OLAP (Online Analytical Processing)           |
|--------------------|-----------------------------------------------|-----------------------------------------------|
| Purpose            | Day-to-day operations                         | Data analysis and decision making             |
| Operations         | Insert, Update, Delete                        | Complex Queries, Aggregations                 |
| Data Size          | Smaller, operational data                     | Larger, historical data                       |
| Users              | Clerks, DBAs, Database Professionals          | Analysts, Business Executives                 |
| Design             | Normalized                                     | De-normalized                                 |
| Example            | Bank transactions                             | Business reports                              |

---

### 2. Batch Processing

- **Definition:** Processing of data in large blocks or batches at scheduled intervals.
- **Tools:** Hadoop, Apache Spark.
- **Use Case:** Payroll systems, bank transactions processing.

---

### 3. Introduction to Apache Spark

#### ➤ **Apache Spark**: Open-source distributed computing system optimized for large-scale data processing.

#### ✳️ Spark Components:
- **Spark Core**: Base engine for general execution.
- **Spark SQL**: SQL queries on structured data.
- **Spark MLlib**: Machine Learning library.
- **Spark GraphX**: Graph computation engine.

#### ✅ Advantages of Spark:
- In-memory computation
- Fault tolerance
- Lazy evaluation
- High-level APIs
- Supports multiple languages (Scala, Python, Java, R)

---

### 4. Introduction to PySpark

- PySpark is the Python API for Spark.
- Enables parallel data processing with simple Python syntax.

---

### 5. Introduction to Databricks

- Unified data analytics platform built on Apache Spark.
- Supports collaborative notebooks and ML pipelines.

---

### 6. RDD (Resilient Distributed Dataset)

- **Immutable distributed collection** of objects.
- **Lazily evaluated**, meaning transformation operations are not executed until an action is called.

#### ✳️ RDD Actions & Transformations

| Transformation       | Description                                     |
|----------------------|-------------------------------------------------|
| `map()`              | Applies function to each element                |
| `filter()`           | Filters based on a condition                    |

| Action               | Description                                     |
|----------------------|-------------------------------------------------|
| `collect()`          | Returns all elements to driver                  |
| `count()`            | Counts number of elements                       |
| `take(n)`            | Returns first n elements                        |

---

## 🔍 Hands-on PySpark Commands and Explanation

```python
# Creating an RDD from a text file
rdd1 = sc.textFile("dbfs:/FileStore/shared_uploads/ashish258kothari@gmail.com/airports.txt")
type(rdd1)  # Check the type of RDD

# Take first row from RDD
x = rdd1.take(1)

# Split each line by commas
rdd1.map(lambda x: x.split(',')).take(1)

# Parallelize data
rdd = sc.parallelize([10,20,30])

# Filter value 20
rdd.filter(lambda x: x == 20).take(3)

# Collect all data
rdd1.collect()
```

---

## ✈️ Airport Data Specific Tasks

```python
# Get airport with ID = 28
rdd1.filter(lambda x: x.split(',')[0] == '28').collect()

# Get 3 airports in Canada
rdd1.filter(lambda x: x.split(',')[3] == '"Canada"').take(3)

# Airport ID, Name, Country for Germany
rdd1.filter(lambda x: x.split(',')[3] == '"Germany"')    .map(lambda x: (x.split(',')[0], x.split(',')[1], x.split(',')[3]))    .collect()

# Airports in Finland with latitude > 60
rdd1.filter(lambda x: x.split(',')[3] == '"Finland"' and float(x.split(',')[6]) > 60)    .collect()

# Count of airports in United Kingdom
rdd1.filter(lambda x: x.split(',')[3] == '"United Kingdom"').count()
```

---

## 🧾 Visual Representation

### 🔄 Spark Architecture Diagram

```plaintext
                    +-----------------------+
                    |  Driver Program       |
                    +----------+------------+
                               |
                         SparkContext
                               |
              +-------------------------------+
              |          Cluster Manager       |
              +---------------+---------------+
                              |
       +----------------------+-------------------------+
       |                      |                         |
   Worker Node 1         Worker Node 2            Worker Node 3
       |                      |                         |
+---------------+   +----------------+       +------------------+
|   Executor    |   |   Executor     |       |   Executor       |
|  Task 1, 2... |   |  Task 3, 4...  |       |  Task 5, 6...     |
+---------------+   +----------------+       +------------------+
```

---

## ✅ Summary

Today’s session gave a clear understanding of how **big data processing** works using tools like **Spark and Databricks**. You also practiced PySpark commands involving **RDD transformations and actions**, particularly focusing on **airport datasets**.

---
