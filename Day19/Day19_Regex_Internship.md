
# **Day 19 - Regex Internship**

## 📚 **Topics Covered**
- Difference between **Database**, **Data Warehouse**, and **DBMS**
- Introduction to **Snowflake** and its architecture
- Working with **Snowflake + AWS S3**
- Creating databases, schemas, stages, and tables
- Copying data from **S3** to **Snowflake**
- Using the `COPY INTO` command
- Renaming a column in a table

---

## 📘 **Theory**

### 🔹 **What is a Database?**
A **database** is an organized collection of structured information or data, typically stored electronically in a computer system. It allows for easy access, manipulation, and updating of data using a **Database Management System (DBMS)**.

### 🔹 **What is a DBMS (Database Management System)?**
A **DBMS** is software that interacts with end users, applications, and the database itself to capture and analyze data. Examples include MySQL, PostgreSQL, Oracle, etc. It helps in:
- Defining, creating, and maintaining the database
- Controlling access to data
- Managing data efficiently

### 🔹 **What is a Data Warehouse?**
A **data warehouse** is a centralized repository designed for storing large volumes of historical data from different sources. It supports **business intelligence (BI)** activities like reporting and data analysis. Key features:
- Optimized for **read-heavy** workloads
- Designed for **analytical processing (OLAP)**
- Supports complex queries and aggregations

### 🔹 **Difference between Database and Data Warehouse**
| Feature           | Database (DBMS)       | Data Warehouse            |
|------------------|-----------------------|---------------------------|
| Purpose          | Transactional (OLTP)  | Analytical (OLAP)         |
| Data Type        | Current, Real-time    | Historical, Aggregated    |
| Normalization    | Highly normalized     | Denormalized              |
| Operations       | Read and Write        | Mostly Read               |
| Examples         | MySQL, Oracle         | Snowflake, Redshift       |

---

## ❄️ **What is Snowflake?**
**Snowflake** is a modern **cloud-based data warehousing** solution that provides:
- Seamless data storage and processing
- High scalability and performance
- Support for semi-structured data (e.g., JSON, Parquet)
- Integration with cloud platforms (AWS, Azure, GCP)

### ✨ **Snowflake Architecture**
- **Databases**: Logical structure to hold schemas and tables
- **Schemas**: Logical grouping of related objects
- **Stages**: Temporary or permanent location to store files before loading
- **Virtual Warehouses**: Perform compute operations (queries, loading)

---

## 🧪 **Practical Snowflake Scripts**

### ✅ Create Database and Schema
```sql
create or replace database MANAGE_DB2;
create or replace schema external_stages;
```

### ✅ Create Stage to Access S3 Bucket
```sql
create or replace stage manage_db2.external_stages.aws_stage
        url=''
        credentials=(aws_key_id=''
        aws_secret_key='');
```

### 📄 Describe Stage
```sql
desc stage manage_db2.external_stages.aws_stage;
```

### 📂 List Files in Stage
```sql
list @manage_db2.external_stages.aws_stage;
```

## 📦 Loading Data Using `COPY INTO`

### 🔸 Create Target Table
```sql
create or replace database regexdb2;

create or replace table regexdb2.public.rating(
    userid int,
    movieid int,
    rarting int,
    timestamp int
);
```

### 🔍 View Data
```sql
select * from regexdb2.public.rating;
```

### 🟢 Copy Command - Load All Files
```sql
copy into regexdb2.public.rating
    from @manage_db2.external_stages.aws_stage
    file_format = (type = csv field_delimiter=',' skip_header=1);
```

### 🟢 Copy Specific File
```sql
copy into regexdb2.public.rating
    from @manage_db2.external_stages.aws_stage
    file_format = (type = csv field_delimiter=',' skip_header=1)
    files = ('ratings.csv');
```

## 📊 Create Another Table & Load Data via `SELECT`
```sql
create or replace table regexdb2.public.newtable(
    userid int,
    movieid int,
    rarting int
);

select * from regexdb2.public.newtable;
```

```sql
copy into regexdb2.public.newtable
    from (select 
            $1::INT AS userid,
            $2::INT AS movieid,
            $3::FLOAT AS rating 
            from @manage_db2.external_stages.aws_stage)
    file_format = (type = csv field_delimiter=',' skip_header=1)
    files = ('ratings.csv');
```

## 🛠️ Rename Column in Table
```sql
ALTER TABLE regexdb2.public.newtable
RENAME COLUMN rarting to rating;
```
