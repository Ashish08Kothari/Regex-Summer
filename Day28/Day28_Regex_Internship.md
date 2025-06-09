# Day 28 - AWS RDS, PostgreSQL, DMS & CDC

## 📌 Topics Covered

### 1. ✅ AWS RDS Setup
- Created a **Relational Database Service (RDS)** instance using **PostgreSQL**.
- Learned to configure DB instance (username, password, port, security group, etc.)
- Configured public accessibility to connect it with local system.

### 2. 💻 PostgreSQL & pgAdmin
- Installed **PostgreSQL** locally on machine.
- Installed and configured **pgAdmin** to manage PostgreSQL DB instances.
- Connected **AWS RDS PostgreSQL** instance with **pgAdmin** via endpoint and credentials.

### 3. 🔁 AWS DMS (Database Migration Service)
- Introduction to **AWS DMS** and its use in **data replication** and **migration**.
- Understood the concept of **Source Endpoint** and **Target Endpoint**.
- Setup replication instance and learned how to create and test endpoints.
- Learned how DMS helps replicate data from RDS to other targets like **S3**.

### 4. 🔄 CDC (Change Data Capture)
- Learned about **CDC**: a method to capture changes in database tables (INSERT, UPDATE, DELETE).
- Understood how **DMS + CDC** allows continuous data replication.
- Real-time data syncing from RDS to targets using CDC.

---

## 🔗 Workflow Diagram (Conceptual)

```plaintext
+-------------+       +--------------+       +------------+       +-------------+
|  AWS RDS    | --->  |  AWS DMS     | --->  |  S3 Bucket  | --->  |  Glue Catalog|
| PostgreSQL  |       |  (CDC Mode)  |       | (Target)    |       |   (Optional) |
+-------------+       +--------------+       +------------+       +-------------+

        ↑
        |
   pgAdmin (Local Machine)
   connects to AWS RDS instance
```

---

## ✅ Summary

- Successfully set up RDS and accessed it using local tools.
- Explored AWS DMS, created migration tasks.
- Learned how to capture real-time data changes using CDC.
- Understood the flow from RDS ➝ DMS ➝ S3 ➝ Glue Catalog.
