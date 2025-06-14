# 🌀 Change Data Capture (CDC) Project

This project demonstrates a **Change Data Capture (CDC)** pipeline using AWS services. The primary objective is to track and capture changes from a PostgreSQL database hosted on Amazon RDS and reflect those changes in near-real time in Amazon S3 using AWS DMS (Database Migration Service). The data is then queried using Amazon Athena for analysis.

---

## ✅ Project Architecture

```mermaid
+---------------------+
| Amazon RDS |
| PostgreSQL 17 |
+---------+-----------+
|
v
+---------+-----------+
| AWS DMS |
| Replication |
| Instance |
+---------+-----------+
|
+------+------+
| |
v v
+------+ +----------------+
|Source| |Target Endpoint |
|EP: | |S3 Bucket |
|RDS | +----------------+
+------+ |
v
+-------------+
| S3 Bucket |
| (CDC Files) |
+-------------+
|
v
+-------------+
| Amazon |
| Athena |
| (Querying) |
+-------------+
```
---

## 🛠️ Tools and Services Used

### 1. **Amazon RDS (PostgreSQL)**
- A managed relational database service.
- Used to host the source database with PostgreSQL 17.

### 2. **pgAdmin / PostgreSQL IDE**
- GUI-based client to connect to and manage PostgreSQL instances.
- Used to connect to the RDS instance from local machine.

### 3. **AWS Database Migration Service (DMS)**
- Used to create a **replication instance** and configure:
  - **Source Endpoint**: PostgreSQL on AWS RDS.
  - **Target Endpoint**: Amazon S3.
  - **CDC Task**: Continuously captures and pushes change logs from source to S3.

### 4. **Amazon S3**
- Used to store the output files (CSV/Parquet) from the DMS replication task.

### 5. **Amazon Athena**
- Serverless query engine that allows SQL-based querying over the data stored in S3.
- Used to perform analysis on the CDC data.

---

## 🔄 Steps Followed

1. **Created an RDS instance**
   - PostgreSQL 17 used as the engine.
   - Enabled public access and created a database.

2. **Connected to RDS from pgAdmin**
   - Used endpoint and credentials to connect to RDS.

3. **Created a Replication Instance in AWS DMS**
   - Small instance size for CDC task.
   - Ensured proper VPC/subnet access to RDS and S3.

4. **Defined Endpoints**
   - **Source Endpoint**: Connected to PostgreSQL RDS.
   - **Target Endpoint**: Connected to S3 bucket (with IAM permissions).

5. **Created a DMS CDC Task**
   - Mode: **CDC only** or **Full load + CDC**.
   - Mapped the schema and tables for migration.
   - Task created and executed successfully.

6. **Captured changes**
   - As data was updated/inserted/deleted in RDS, files were generated in S3.

7. **Analyzed data using Athena**
   - Defined schema over the S3 data.
   - Queried the live captured data using SQL.

---

## 📊 Use Cases

- Real-time data warehousing.
- Data lake integrations.
- Audit and compliance tracking.
- Streaming data analysis.

---


