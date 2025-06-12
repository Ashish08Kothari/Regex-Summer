
# Day 29 - Regex Internship

**Date:** 2025-06-04  
**Topic:** Introduction to MySQL and SQL Basics

---

## 🧠 Topics Covered

Today, I was introduced to **MySQL**, one of the most popular relational database management systems (RDBMS). Below are the main concepts covered during the session:

### ✅ What is MySQL?

MySQL is an open-source RDBMS that uses SQL (Structured Query Language) to manage and manipulate databases. It is widely used in web development and data management.

---

## 📘 Basic SQL Commands

### 1. Creating a Database

```sql
CREATE DATABASE School;
```

### 2. Creating a Table

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Grade CHAR(1)
);
```

### 3. Inserting Data

```sql
INSERT INTO Students (StudentID, FirstName, LastName, Age, Grade)
VALUES (1, 'John', 'Doe', 15, 'A');
```

### 4. Retrieving Data

```sql
SELECT * FROM Students;
```

### 5. Filtering Records

```sql
SELECT * FROM Students WHERE Age > 14;
```

### 6. Updating Records

```sql
UPDATE Students SET Grade = 'B' WHERE StudentID = 1;
```

### 7. Deleting Records

```sql
DELETE FROM Students WHERE StudentID = 1;
```

---

## 🧩 Additional SQL Concepts

- **Constraints** like PRIMARY KEY, NOT NULL, UNIQUE
- **Joins** (INNER, LEFT, RIGHT, FULL) for combining data from multiple tables
- **Aggregate Functions** (COUNT, AVG, SUM, MAX, MIN)
- **Group By and Having** for grouping results

---

## ✅ Summary

- Understood the structure and syntax of SQL.
- Practiced creating and manipulating databases and tables in MySQL.
- Learned essential SQL operations and their real-world applications.

---

> 📌 *This session laid a strong foundation in SQL and MySQL, which is crucial for any backend or data-related role.*
