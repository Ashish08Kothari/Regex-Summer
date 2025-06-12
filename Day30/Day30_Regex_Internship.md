# Day 30 - Regex Software Services Internship

## Topics Covered

### ✅ Advanced SQL in MySQL

We started by creating a database and table, then performed multiple SQL operations including **window functions**, **CTEs (Common Table Expressions)**, and **aggregations**.

---

### 🔸 SQL Table Creation

```sql
CREATE DATABASE user1;
USE user1;

CREATE TABLE EmployeeSales (
    EmployeeID INT,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    SaleDate DATE,
    SaleAmount DECIMAL(10, 2)
);
```

---

### 🔸 Sample Data Insert

```sql
INSERT INTO EmployeeSales (EmployeeID, EmployeeName, Department, SaleDate, SaleAmount) VALUES
(1, 'Alice', 'Sales', '2025-06-01', 1200.00),
(1, 'Alice', 'Sales', '2025-06-03', 1800.00),
(1, 'Alice', 'Sales', '2025-06-07', 1500.00),
...
(10, 'Jake', 'IT', '2025-06-10', 3100.00);
```

---

### 🔸 Queries Executed

- **View all records**
```sql
SELECT * FROM EmployeeSales;
```

- **Total sale amount using window function**
```sql
SELECT *, SUM(SaleAmount) OVER() FROM EmployeeSales;
```

- **Partition by Department**
```sql
SELECT *, SUM(SaleAmount) OVER(PARTITION BY Department) FROM EmployeeSales;
```

- **Partition by Employee**
```sql
SELECT *, SUM(SaleAmount) OVER(PARTITION BY EmployeeName) FROM EmployeeSales;
```

- **Running sum by SaleAmount**
```sql
SELECT *, SUM(SaleAmount) OVER(ORDER BY SaleAmount) FROM EmployeeSales;
```

- **Running sum by EmployeeName**
```sql
SELECT *, SUM(SaleAmount) OVER(ORDER BY EmployeeName) FROM EmployeeSales;
```

- **Using CTE to filter**
```sql
WITH abc AS (
    SELECT *, SUM(SaleAmount) OVER(PARTITION BY EmployeeName) AS TotalSales
    FROM EmployeeSales
)
SELECT * FROM abc WHERE TotalSales - SaleAmount > 1000;
```

---

## 🔁 AWS DMS (Data Migration Service) + CDC (Change Data Capture)

We started a CDC-based project using AWS services. Here’s what we implemented:

1. **Created a replication instance**
2. **Configured two endpoints**:  
   - Source: RDS PostgreSQL instance  
   - Target: S3 Bucket
3. **Created a replication task**:
   - It captures changes (INSERT/UPDATE/DELETE) from the RDS source
   - Pushes them to the S3 target bucket in real time

---

## 🔄 Workflow Overview

```
+-------------+       +----------------------+        +-----------+
| Local RDS   | --->  | AWS DMS (Replication)| --->   |  S3 Bucket|
+-------------+       | Source & Target Endpt|        +-----------+
                      +----------------------+
```

---

## Summary

Today's session strengthened our understanding of:

- Advanced SQL window functions
- Common Table Expressions (CTEs)
- AWS DMS configuration
- Real-time change capture using CDC
