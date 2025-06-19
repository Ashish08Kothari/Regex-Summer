# Day 34 - Regex Software Services Internship

## 📅 Date  
**Day 34**

## 📝 Summary  
Today, we continued working on our **Kafka + AWS + MySQL + Tableau ETL pipeline project**. The goal of the project is to extract data from a CSV file stored in an AWS S3 bucket, send it through a Kafka producer, consume it using a Kafka consumer, and insert the data into **both MySQL RDS** and **S3**, row by row. We then use **AWS Glue Crawler** to create metadata tables, query the data with **Athena**, and finally visualize the results in **Tableau**.

---

## ✅ Tasks Completed Today

- Resumed work on the ETL pipeline project.
- Fixed existing issues in the Kafka producer and consumer scripts.
- Ensured the producer correctly reads the CSV file from the S3 bucket.
- Updated the consumer to:
  - Insert records into the MySQL RDS.
  - Save rows individually to the S3 bucket.
- Validated correct data entry into RDS and S3.
- Reconfigured and re-ran the **AWS Glue Crawler** to update the metadata.
- Verified updated tables via **AWS Athena**.
- Ensured successful connectivity of **Tableau** with Athena for real-time visualization.
- Optimized error handling and logging in the Python scripts.

---

## 🔄 Project Architecture

```mermaid
flowchart LR
    A[CSV File in S3] --> B[Kafka Producer (Python)]
    B --> C[Kafka Topic]
    C --> D[Kafka Consumer (Python)]
    D --> E[MySQL RDS]
    D --> F[S3 (Cleaned Data)]
    F --> G[AWS Glue Crawler]
    G --> H[Athena (Querying)]
    H --> I[Tableau (Visualization)]
