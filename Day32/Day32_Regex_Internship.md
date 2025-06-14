# Day 32 - Regex Internship

**Date:** 2025-06-14  
**Topic:** Apache Kafka - Zookeeper, Producer & Consumer (with Python)

---

## 🧠 Topics Covered

Today, we learned and worked on the following:

- Setting up **Zookeeper** to manage and coordinate Kafka brokers.
- Creating and configuring **Kafka Server**.
- Running **Kafka Producer** and **Consumer** using terminal.
- Writing a **Python script for Producer** to send messages to Kafka topic.
- Keeping **Consumer on terminal** to receive the messages.
- Later, we also created the **Kafka Consumer using Python** and tested both.

---

## ⚙️ Zookeeper Setup

```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## ⚙️ Kafka Server Setup

```bash
# Start Kafka broker
bin/kafka-server-start.sh config/server.properties
```

## 🎯 Kafka Topic Creation

```bash
# Create topic named 'test-topic'
bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

## 📤 Kafka Producer via Terminal

```bash
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
```

## 📥 Kafka Consumer via Terminal

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```

---

## 🐍 Kafka Python Producer Script

```python
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'test-topic'

for i in range(5):
    msg = f'Message {i}'
    producer.send(topic, msg.encode('utf-8'))
    print(f'Sent: {msg}')

producer.close()
```

## 🐍 Kafka Python Consumer Script

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
```

---

## ✅ Conclusion

Today’s session strengthened our understanding of Kafka's architecture, including Zookeeper, Kafka Broker, Producer, and Consumer. It also helped us integrate Python for real-time message production and consumption in Kafka.

