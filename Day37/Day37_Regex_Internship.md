
# Day 37 - Regex Software Services Internship

## 📅 Date: [Your Date Here]

## 📌 Topics Covered

Today, we were assigned a **group project** involving the development of an **ETL pipeline using Apache Airflow**. The project focuses on automating the extraction, transformation, and loading of **stock market data** from an API into an **RDS database** and **S3 bucket**, followed by analysis using **Athena or Redshift**, and finally visualization using **Power BI**.

---

## 🛠️ Project: Stock Market Data ETL Pipeline using Apache Airflow

### 🔄 Flow Diagram

```
[API] --> [Airflow Scheduler] --> [ETL Pipeline]
                                |--> [RDS (PostgreSQL)]
                                |--> [S3 Bucket]
                                       |
                                       V
                              [Athena / Redshift] --> [Power BI Dashboard]
```

---

## 🧠 Concepts Learned

### 1. **Apache Airflow**
- Open-source tool to programmatically author, schedule, and monitor workflows.
- Uses **Directed Acyclic Graphs (DAGs)** to manage task dependencies.

### 2. **ETL Workflow with Airflow**
- **Extract:** Fetch stock market data from an external API at regular intervals.
- **Transform:** Clean or format the data as needed.
- **Load:** Store the transformed data in both **AWS RDS** and **AWS S3**.

### 3. **AWS RDS (Relational Database Service)**
- Managed relational database (PostgreSQL used in this case).
- Stores structured, transformed data for querying.

### 4. **AWS S3**
- Object storage used to save raw and cleaned CSV files.

### 5. **Amazon Athena / Redshift**
- Athena allows querying data directly from S3 using SQL.
- Redshift is a scalable data warehouse for more complex analytics.

### 6. **Power BI**
- Microsoft’s data visualization tool.
- Used for building dashboards and deriving insights.

---

## 🔍 Next Steps

- Read and understand **Airflow's DAG architecture**, task dependencies, and operators.
- Set up a local Airflow environment or use **MWAA (Managed Workflows for Apache Airflow)**.
- Begin writing a DAG to automate data extraction and storage.

---

## ✅ Summary

Today laid the foundation for a hands-on project to practice real-world ETL pipelines. We understood the role of **Airflow** in workflow management, how to connect to **AWS RDS and S3**, and how **Athena or Redshift** can be used to analyze data before finally visualizing it using **Power BI**.

---

**Prepared by:** Ashish Kothari  
**Internship at:** Regex Software Services
