# Day 31 - Regex Internship


## 🧑‍💻 Activities Covered:

Today, I learned how to work with **Apache Kafka** on an **AWS EC2 instance**. Here's a summary of what was done step-by-step:

---

## 🔧 Step 1: Create and Connect EC2 Instance

- Created an **EC2 instance** with **Ubuntu** as the operating system.
- Allowed ports 22 (SSH), 9092 (Kafka), and 2181 (Zookeeper) in the security group.
- Connected to the instance using SSH from local terminal:

```bash
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip
```
---

# ☕ Step 2: Install Java (required for Kafka and Zookeeper)

```
sudo apt update
sudo apt install default-jdk -y
java -version
```
---

# 🐘 Step 3: Download and Setup Kafka
```
wget https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz
tar -xvzf kafka_2.13-3.6.0.tgz
cd kafka_2.13-3.6.0
```
---

# 🦓 Step 4: Start Zookeeper
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
---

# 🛰️ Step 5: Start Kafka Server
```
bin/kafka-server-start.sh config/server.properties
```
---

# 🧵 Step 6: Create Kafka Topic
```
bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
---

# 🗣️ Step 7: Start Kafka Producer
```
bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
```
---

# 👂 Step 8: Start Kafka Consumer
```
bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```
---

### 🧠 What I Learned
* How to set up and connect to an EC2 instance.

* Installed Java and Kafka.

* Started Zookeeper and Kafka services.

* Created a topic, and understood the producer-consumer flow in Kafka.

### 📌 Notes
* Keep each service running in its own terminal session.

* Kafka listens on port 9092 and Zookeeper on 2181.

* Make sure firewall settings (security groups) allow incoming connections if needed.