# 🚀 Real-Time Stock Price Analytics Pipeline using Airflow, Snowflake, dbt & Superset

## ✨ Why I Built This Project

With the stock market being fast-moving and volatile, I wanted to build a **real-time analytics pipeline** that could track and visualize patterns in stock prices. As someone passionate about both finance and data engineering, I chose this project to simulate how enterprise teams build **scalable ELT systems** that power BI dashboards and drive decision-making.

This pipeline takes **raw stock data** (NVDA, MSFT), ingests it automatically using **Apache Airflow**, models it with **dbt**, stores it in **Snowflake**, and visualizes it using **Superset dashboards**.

Through this project, I gained hands-on experience orchestrating automated workflows and managing data lifecycle from **API ingestion to insight delivery** — a vital skill set for roles in **Data Engineering** and **Analytics**.

---

## 🔧 Tech Stack

| Tool/Technology | Role |
|------------------|------|
| Python           | API requests, data handling |
| Apache Airflow   | Workflow orchestration (ETL scheduling) |
| Snowflake        | Cloud data warehouse |
| dbt              | Data modeling and transformation |
| Apache Superset  | Interactive BI dashboarding |
| Docker           | Containerized development and deployment |

---

## 🔄 Project Architecture

📌 This diagram shows the full flow from ingestion to visualization:


<img width="935" height="358" alt="image" src="https://github.com/user-attachments/assets/8fa363fe-422c-4571-a695-2b3a4a18c947" />


---

## 🔁 Workflow Overview

1. **Data Ingestion**
   - Real-time stock prices fetched every 10 minutes using Alpha Vantage API
   - Managed by **Airflow DAG 1**

2. **Data Loading**
   - Ingested into `STOCK_PRICE` table in **Snowflake**
   - Uses `MERGE` SQL for efficient upserts

3. **Data Transformation**
   - **Airflow DAG 2** runs dbt models:
     - Calculates 7-day and 30-day moving averages
     - Computes RSI (Relative Strength Index)
   - Output tables: `STOCK_ANALYTICS`, `MOVING_AVG`, `RSI_TABLE`

4. **Data Visualization**
   - Apache Superset connects to Snowflake
   - Dashboards visualize trends, RSI, and closing prices

---

##  Dashboards
### 1. Real-Time Stock Performance Overview

<img width="1158" height="460" alt="image" src="https://github.com/user-attachments/assets/78b58ca0-8540-499e-bb0b-f31632df943d" />


This interactive Superset dashboard visualizes real-time trends in **NVIDIA (NVDA)** and **Microsoft (MSFT)** stock performance using:

- **Closing Prices**
- **7 & 30-Day Moving Averages**
- **Relative Strength Index (RSI)**

### 👥 Designed For:
- 📈 **Investors & Traders** – to make informed buy/sell decisions based on momentum
- 📉 **Technical Analysts** – to spot reversal points using RSI
- 📊 **Financial Analysts** – to identify price stability and short-term trends

### 📂 Dataset Sources:
- Daily OHLC stock prices for NVDA and MSFT
- Calculated RSI and moving averages using dbt models

### 2. Filtered Stock Insights Dashboard

<img width="1031" height="424" alt="image" src="https://github.com/user-attachments/assets/fa91beef-cc42-467c-a98e-f8c196ad160f" />

This Superset dashboard delivers a focused view of recent stock trends for NVIDIA (NVDA) and Microsoft (MSFT), enabling quick analysis of short-term performance.

Daily Closing Price Trends (e.g., NVDA from September–November)

Side-by-Side Monthly Comparisons for NVDA & MSFT

7-Day Price History for rapid fluctuation tracking

👥 Designed For:
📈 Short-Term Investors – to monitor recent stock behavior before trading

🔎 Analysts – to compare specific date ranges across symbols

📊 Portfolio Managers – to assess short-term volatility patterns

📂 Dataset Sources:
Historical daily OHLC prices for NVDA and MSFT

RSI and moving averages computed via dbt transformations

## 📁 Folder Structure
├── airflow/ # DAGs, configs, Docker setup
├── dbt/ # dbt models and snapshots
├── superset/ # Superset configs
├── assets/ # Screenshots and architecture diagrams
├── README.md

## ✅ Key Learning Outcomes

- Orchestrating multi-stage ETL pipelines with Airflow
- Real-world data modeling using dbt in Snowflake
- Data quality checks and snapshots
- Building investor-facing dashboards with Superset
- Containerizing pipelines with Docker

---

## 🚀 Future Enhancements

- Support dynamic list of stock symbols
- Add Slack/Email alerts for failed DAG runs
- Migrate to fully cloud-native stack using GCP or AWS services

