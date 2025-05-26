
# **Day 17 - Regex Data Engineering Internship**
**Date:** 2025-05-26

---

## 🧠 **Topics Covered**

### 🔴 Hadoop Disadvantages
1. **Slow Processing Speed**  
   Hadoop relies on disk-based storage and processing, which makes it slower compared to in-memory systems like Apache Spark.

2. **No Real-Time Processing**  
   Hadoop is designed for batch processing and does not handle real-time data processing tasks effectively.

---

### 🔵 AWS Glue and Crawlers
- **Crawler** is used to scan and classify data stored in AWS (e.g., in S3 buckets) and populate the AWS Glue Data Catalog.
- **Pipeline** in AWS Glue is a visual ETL job authoring tool used to define, manage, and monitor data workflows.
- **Glue** is an ETL (Extract, Transform, Load) service used to prepare and transform data for analytics and machine learning.

---

### 🔁 ETL vs ELT

| Feature | ETL (Extract → Transform → Load) | ELT (Extract → Load → Transform) |
|--------|----------------------------------|----------------------------------|
| Processing | Outside the data warehouse | Inside the data warehouse |
| Transformation | Happens before loading | Happens after loading |
| Speed | Slower | Faster with modern cloud systems |
| Use Case | Traditional systems | Big data & cloud data lakes |

---

### 🔗 Practical Session

1. **Created an AWS S3 Bucket**
   - Uploaded a `.csv` and `.json` file into the bucket.

2. **Created a Crawler in AWS Glue**
   - Connected the crawler to the S3 bucket to fetch metadata.
   - Ran the crawler to populate the AWS Glue Data Catalog.

3. **Analyzed data using the Glue Console**
   - Verified tables and schemas detected by the crawler.
   - Discussed how this integrates into ETL/ELT pipelines.

---

Let me know if you'd like to include code snippets, screenshots, or a workflow diagram.
