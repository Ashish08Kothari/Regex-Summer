# Day 36 – YouTube API Project with Kafka, MySQL, S3 & Tableau

## 📌 Project Title:  
**YouTube API Data Engineering Project – Indian Food Channels**

---

## 🎯 Objective:
To build a data pipeline that extracts data from the YouTube Data API for 7 Indian food channels, streams it using Kafka, stores it in MySQL and S3, and then visualizes it using Tableau via AWS Athena.

---

## 🛠️ Tools & Technologies Used:
- **YouTube Data API**: For extracting metadata of videos
- **Apache Kafka**: Used for real-time data streaming between producer and consumer
- **MySQL (RDS)**: For storing structured video data
- **Amazon S3**: For storing raw/cleaned CSV data
- **AWS Glue**: Crawler to infer schema from S3 and create metadata catalog
- **AWS Athena**: For querying S3-stored data
- **Tableau**: For creating interactive dashboards and visualizing insights

---

## 🔗 API Used:
**YouTube Data API v3**  
URL: [https://console.developers.google.com](https://console.developers.google.com)  
Purpose: Fetch video metadata such as `title`, `views`, `likes`, `published date`, `channel title`, etc.

---

## 📦 Data Flow Architecture:

YouTube API → Kafka Producer → Kafka Topic → Kafka Consumer →
→ MySQL RDS & S3 Bucket → AWS Glue Crawler → AWS Athena → Tableau


---

## 🧱 Step-by-Step Implementation:

### 1. **Kafka Producer:**
- Used the YouTube Data API to fetch video details from 7 Indian food channels (excluding Shorts).
- Parsed and structured video metadata.
- Sent data to Kafka Topic.

### 2. **Kafka Consumer:**
- Consumed real-time video data from Kafka Topic.
- Wrote the video data **row-by-row** to:
  - **MySQL RDS instance** (structured storage)
  - **AWS S3** (raw/archival storage as `.csv`)

### 3. **S3 + Glue Integration:**
- Created a bucket (e.g., `youtube-indian-food-data`)
- Used AWS Glue Crawler:
  - Pointed it to the S3 bucket
  - Auto-generated schema and metadata table

### 4. **Athena Setup:**
- Verified the data using Athena queries
- Ensured data consistency and schema correctness

### 5. **Tableau Dashboard:**
- Connected Tableau to Athena
- Created interactive visualizations such as:
  - Top viewed videos
  - Video uploads per channel
  - Likes and comments comparison
  - Daily uploads trend

---

## 📝 Key Learnings:
- Practical hands-on with **Kafka pipeline**
- Usage of **YouTube Data API**
- Real-time data ingestion
- Working with **MySQL and S3** together
- Schema inference via **AWS Glue**
- Visualization with **Tableau connected to Athena**

---

## ✅ Final Outcome:
- Successfully built an **end-to-end ETL pipeline** for streaming, storing, and visualizing YouTube video analytics.
- Delivered real-time, queryable insights using **Athena + Tableau**.
