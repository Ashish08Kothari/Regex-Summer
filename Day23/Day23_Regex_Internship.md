
# Day 23 – Internship Report at Regex Software Services

## 📅 Date: June 3, 2025  
## 🧑 Intern: Ashish Kothari  
## 🧑‍💻 Mentor: [Mentor Name]  

---

## 🧠 Topics Covered

### 1. Spark Context vs Spark Session
- **SparkContext** is the entry point to low-level Spark core features and is used to create RDDs.
- **SparkSession** is the unified entry point for all functionality in Spark 2.0 and later including Spark SQL, DataFrames, etc.

| Feature          | SparkContext                          | SparkSession                             |
|------------------|----------------------------------------|------------------------------------------|
| Introduced In    | Spark 1.x                              | Spark 2.x                                |
| Scope            | RDD APIs                               | DataFrames, SQL, Streaming, ML           |
| Entry Point      | sc = SparkContext()                    | spark = SparkSession.builder...          |
| Recommended      | ❌ (outdated for SQL/DataFrames)       | ✅ (recommended for most use cases)       |

---

## 💻 Practical – Spark RDD Operations

```python
data = [10, 20, 30, 40, 10, 10, 20]
rdd1 = sc.parallelize(data)
rdd1.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).collect()
```

**Explanation**:
- `parallelize`: Creates an RDD.
- `map`: Transforms each element into a key-value pair.
- `reduceByKey`: Aggregates by key.

---

## 💻 Practical – SparkSession and DataFrame Operations

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Hey").getOrCreate()

data = [("Shyam", 'Vanila', 'Ion', "", "M", 6339),
        ("Jack", "", "Smith", "36636", "M", 83000)]
columns = ["first_name", "middle_name", "last_name", "id", "gender", "salary"]

df = spark.createDataFrame(data, schema=columns)
df.show()
```

---

## 📁 Reading CSV using PySpark

```python
df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/ashish258kothari@gmail.com/ratings.csv")
df1.show()

df = spark.read.csv("dbfs:/FileStore/shared_uploads/ashish258kothari@gmail.com/ratings.csv", header=True, inferSchema=True)
df.show(3)
df.printSchema()
df.columns
df.describe().show()
```

### 📌 Column Selection & Filtering

```python
df.select("userId", "movieId").show(2)
df.filter(df['rating'] > 2).show()

from pyspark.sql.functions import col
df.filter((col('rating') > 3) & (col('userId') > 50)).show()
df.filter(col('userId') < 45).select('userId', 'movieId', 'rating').show()
```

### ➕ Adding & Renaming Columns

```python
df.withColumn("new_user", col("userId") * 10).show(2)
df.withColumnRenamed("userId", "new_user").show(2)
```

---

## 🕒 Unix Timestamp Transformation

### 🔁 Convert timestamp to human-readable date

```python
from pyspark.sql.functions import year, col, from_unixtime

df = df.withColumn("Timestamp", from_unixtime(col("timestamp")))
```

### 📆 Filter by Year

```python
df.filter(year(col("Timestamp")) == 2005).show(5)
```

### ✍ Rename & Add Columns

```python
df = df.withColumnRenamed("Timestamp", "Year_of_movie")
df = df.withColumn("New_movie_id", col("movieId") * 5)
df = df.withColumn("rating", col("rating").cast("int"))
df.show(5)
df.printSchema()
```

---

## 📊 Suggested Visuals

- **Diagram**: Spark architecture (Spark Core, Spark SQL, Spark Streaming, MLlib, GraphX)
- **Comparison Table**: SparkContext vs SparkSession
- **Chart**: Data transformation steps applied on the ratings.csv DataFrame

---

## ✅ Summary

Today’s session helped gain hands-on experience in:
- Understanding Spark components and API evolution.
- Mastering RDD and DataFrame operations.
- Handling CSV data in PySpark.
- Performing real-world transformations and queries.

---

📌 *End of Day 23 Report*
