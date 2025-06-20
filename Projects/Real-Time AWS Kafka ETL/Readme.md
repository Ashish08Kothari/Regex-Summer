# 🌐 Real-Time AWS Kafka ETL Pipeline 🚀

A real-time data pipeline built using **Apache Kafka**, **AWS S3**, and **MySQL RDS**. This project demonstrates a complete ETL workflow that:
- 📥 **Extracts** data from an S3 bucket (CSV file)
- 🔄 **Transforms** the data via Kafka streaming
- 📤 **Loads** it into **MySQL RDS** and back into **S3** in a structured format

---

## 🧩 Architecture Diagram

```text
+------------------+           +----------------+           +---------------------+
|     AWS S3       |  --->     | Kafka Producer |  --->     |   Kafka Topic       |
|  (Input CSV)     |           |   (Python)     |           |  (Streamed Data)    |
+------------------+           +----------------+           +---------------------+
                                                                    |
                                                                    v
                                                           +------------------+
                                                           | Kafka Consumer   |
                                                           | (Python Script)  |
                                                           +--------+---------+
                                                                    |
                         +------------------------------------------+---------------------------------+
                         |                                                                                |
                         v                                                                                v
             +---------------------+                                                        +------------------------+
             |    MySQL RDS        |   <------ Structured insert ------>     |      AWS S3 (Processed Data) |
             +---------------------+                                                        +------------------------+
```
---

### 📁 Project Structure
```markdown
## 📁 Project Structure

```bash
real-time-aws-kafka-etl/
│
├── producer/
│   └── s3_kafka_producer.ipynb         # Reads CSV from S3 and sends to Kafka topic
│
├── consumer/
│   └── kafka_consumer_mysql_s3.ipynb   # Consumes data from Kafka and writes to MySQL and S3
│
├── sql/
│   └── schema.sql                   # MySQL table creation script
│
│
├── visualization/
│   └── dashboard.pptx               # Tableau dashboards
│   
│
└── README.md                        # This file 📄
```
---

### 🛠️ Technologies Used
```markdown
## 🛠️ Technologies Used

- 🐍 Python
- ☁️ AWS S3
- 🐘 MySQL RDS
- 🔄 Apache Kafka
- 🐳 Docker (for Kafka & Zookeeper)
- 📦 Boto3 (for AWS SDK)
- 🔗 Kafka-Python
```
## 🔧 How It Works

1. **Upload a CSV** to your S3 bucket
2. The **Kafka producer** reads the CSV and publishes each row to a **Kafka topic**
3. The **Kafka consumer**:
   - Parses each message
   - Inserts clean data into **MySQL RDS**
   - Uploads the same data as a structured CSV/JSON back to **S3**

## 🧪 Example CSV Format

```csv
video_id,title,channel,views,likes,timestamp
abc123,How to Cook,Chef Ashish,10000,500,2025-06-01T12:00:00Z
def456,Street Food India,FoodieFun,25000,1300,2025-06-02T14:30:00Z

```
---

### ✅ Features
```markdown
## ✅ Features

- Real-time stream processing 🌀
- Scalable producer-consumer model ⚙️
- Dual-output (RDS + S3) 🗃️
- AWS-native integration 🔐
- Clean ETL separation 🧼
```
## 🚀 Future Improvements

- Integrate **AWS Lambda** for event-based triggers
- Add **data validation** before load
- Support for **multiple file types** (JSON, Parquet)
- Implement **monitoring** via Prometheus + Grafana

## 👤 Author

**Ashish Kothari**  
_Data Engineering Intern at Regex Software Services_  
🗓️ **June 2025**
