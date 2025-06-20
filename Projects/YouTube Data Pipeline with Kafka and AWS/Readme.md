# 📺 YouTube Data Pipeline with Kafka and AWS

A real-time data engineering project that extracts video data from the **YouTube Data API** for 7 Indian food channels, streams it using **Apache Kafka**, stores it in **MySQL RDS** and **AWS S3**, and visualizes insights using **Tableau** via **AWS Athena**.

---

## 🧩 Architecture Diagram

```text
       +--------------------+
       | YouTube Data API   |
       +--------------------+
                 |
                 v
       +------------------------+
       | Kafka Producer (Python)|
       +------------------------+
                 |
                 v
         +------------------+
         |   Kafka Topic    |
         +------------------+
                 |
                 v
       +---------------------------+
       | Kafka Consumer (Python)   |
       +---------------------------+
           |             |
           v             v
+------------------+   +-----------------------+
|    MySQL RDS     |   | AWS S3 (Raw + Clean) |
+------------------+   +-----------------------+
                             |
                             v
                    +------------------+
                    | AWS Athena Table |
                    +------------------+
                             |
                             v
                        🎨 Tableau Dashboard
```

---

#### 3. **Project Structure**
```markdown
## 📁 Project Structure

```bash
youtube-kafka-pipeline/
│
├── producer/
│   └── youtube_kafka_producer.ipynb       # Fetches video data from YouTube API and sends to Kafka
│
├── consumer/
│   └── kafka_consumer_mysql_s3.ipynb      # Consumes from Kafka, inserts into MySQL, uploads to S3
│
├── data/
│   └── channels.json                    # List of YouTube channel IDs
│   └── processed/                      # Final CSV/JSON files pushed to S3
│
├── sql/
│   └── youtube_schema.sql              # MySQL table structure
│   └── athena_create_table.sql         # Athena DDL to read from S3
│
├── visualization/
│   └── dashboard.pptx          # Final Tableau dashboard
│
└── README.md                           # This file 📄
```


---


##  🛠️ Technologies Used

- 🐍 Python (Producer/Consumer)
- 🔄 Apache Kafka (Real-time stream)
- 🎥 YouTube Data API (Video metadata)
- 🐘 MySQL RDS (Structured storage)
- ☁️ AWS S3 (Raw + Processed data lake)
- 🔍 AWS Athena (SQL query on S3)
- 📊 Tableau (Data Visualization)
- 📦 Boto3 (AWS SDK for Python)
- 🔗 kafka-python (Kafka client)
## 🔧 How It Works

1. **Kafka Producer**:
   - Reads YouTube channel IDs from a local JSON file
   - Uses the **YouTube Data API** to fetch video metadata (excluding Shorts)
   - Streams each video as a Kafka message

2. **Kafka Consumer**:
   - Listens to the Kafka topic
   - Writes clean records to **MySQL RDS**
   - Also stores the data as CSV/JSON in **AWS S3**

3. **Athena + Tableau**:
   - **AWS Athena** queries the S3 data using external tables
   - **Tableau** connects to Athena and builds dashboards (views, likes, upload trends)


## 🧪 Sample Data Format

```json
{
  "video_id": "abc123",
  "title": "Best Biryani Recipe",
  "channel_title": "Indian Food Hub",
  "published_at": "2025-06-01T10:00:00Z",
  "view_count": 105000,
  "like_count": 5100
}
```


---


## ✅ Features

- ⏱ Real-time streaming with Kafka
- 🎯 Focused on Indian food YouTube channels
- 📥 Dual storage: MySQL for structure, S3 for scale
- 🔍 Athena integration for cost-effective querying
- 📈 Insightful visualizations using Tableau


## 🚀 Future Enhancements

- Add sentiment analysis on video comments
- Trigger Lambda function on new upload
- Support for multi-language channel data
- Use Apache Airflow for orchestration

## 👤 Author

**Ashish Kothari**  
_Data Engineering Intern at Regex Software Services_  
🗓️ **June 2025**
