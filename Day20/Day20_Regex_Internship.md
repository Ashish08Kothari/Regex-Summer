
# 📘 Day 20 – Data Modeling, ER Modeling, Star Schema & Snowflake Schema

---

## 🔶 Data Modeling

**Data modeling** is the process of creating a visual representation of either a whole information system or parts of it to communicate connections between data points and structures.

### Key Points:
- Helps in structuring and organizing data.
- Defines how data is connected and processed.
- Foundation of a well-designed database system.

---

## 🧩 ER (Entity-Relationship) Modeling

ER modeling is a high-level conceptual data model diagram. It is a visual representation of different entities within a system and how they relate to each other.

### Components of ER Model:
- **Entity**: Object or thing (e.g., Student, Course).
- **Attribute**: Properties of an entity (e.g., name, age).
- **Relationship**: Association between entities (e.g., student "enrolls" in course).

### ER Diagram Example:

```
[STUDENT] -----<enrolls>----- [COURSE]
   |                             |
  Name                         Title
  RollNo                       Credits
```

---

## ⭐ Star Schema

Star schema is a type of database schema used in data warehousing. It consists of one **fact table** in the center and multiple **dimension tables** surrounding it, forming a star-like shape.

### Characteristics:
- Simpler and denormalized structure.
- Optimized for read-heavy operations and queries.

### Diagram:
```
         [Time]
            |
[Product] - [Sales Fact] - [Customer]
            |
         [Store]
```

### Advantages:
- Fast query performance.
- Easy to understand.

---

## ❄️ Snowflake Schema

Snowflake Schema is a more complex version of Star Schema with normalized dimension tables.

### Characteristics:
- Normalized structure (data redundancy is minimized).
- More joins are required to query data.

### Diagram:
```
       [Time]
          |
[Product]--[Category]
     |         |
[Sales Fact]  [Customer]--[Region]
```

### Advantages:
- Better storage efficiency.
- Maintains data integrity.

---

## 🔁 Star Schema vs Snowflake Schema

| Feature              | Star Schema                   | Snowflake Schema               |
|----------------------|-------------------------------|-------------------------------|
| Structure            | Denormalized                  | Normalized                    |
| Query Performance    | Faster                        | Slightly slower               |
| Storage              | More storage due to redundancy| Less storage                  |
| Simplicity           | Simple and intuitive          | Complex                       |
| Joins Required       | Fewer                         | More                          |

---

## ✅ Summary

- **Data Modeling** defines the structure of data storage.
- **ER Modeling** helps visualize entities and their relationships.
- **Star Schema** is preferred for fast querying in analytics.
- **Snowflake Schema** is used when normalization is required for storage optimization.

---

Feel free to add diagrams in your notes or tools like dbdiagram.io or Lucidchart for visual clarity.
