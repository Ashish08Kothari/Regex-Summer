# Zomato Data Analysis Project

## Project Overview

This project involves transforming and analyzing the [Zomato Restaurant Dataset](https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset). The goal is to design a dimensional model from the raw data, load it into a Snowflake data warehouse, and derive business insights through analytical SQL queries.

---

## Data Source

Dataset Link: [🍽️ Zomato Restaurant Dataset on Kaggle](https://www.kaggle.com/datasets/rajeshrampure/zomato-dataset)

Results Link: [📦 Queries Result on Google Drive](https://drive.google.com/drive/folders/1dwh30MHqCpzRNHII0WgmOQnRLDmE4DG2?usp=sharing)

---

## Data Loading and Staging

### Table Creation

```sql
CREATE OR REPLACE TABLE zomato_data (
    url STRING,
    address STRING,
    name STRING,
    online_order STRING,
    book_table STRING,
    rate STRING,
    votes STRING,
    phone STRING,
    location STRING,
    rest_type STRING,
    dish_liked STRING,
    cuisines STRING,
    approx_cost_for_two_people STRING,
    reviews_list STRING,
    menu_item STRING,
    listed_in_type STRING,
    listed_in_city STRING
);
```

### Copying Data into Table

```sql
COPY INTO regexdb2.public.zomato_data
FROM @manage_db2.external_stages.aws_stage/zomato.csv
FILE_FORMAT = (
    TYPE = 'CSV',
    FIELD_DELIMITER = ',',
    SKIP_HEADER = 1,
    FIELD_OPTIONALLY_ENCLOSED_BY = '"',
    TRIM_SPACE = TRUE
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1c3CHHeT5IqxZyMKyVzbpvNyVvj6xS-ob/view?usp=sharing)


---

## Dimensional Modeling

### Restaurant Dimension

```sql
CREATE OR REPLACE TABLE regexdb2.public.restaurant_dim AS
SELECT
    name,
    ROW_NUMBER() OVER (ORDER BY name) AS r_id,
    url,
    phone
FROM (
    SELECT name, url, phone,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
)
WHERE rn = 1;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1LN5B9Kt6L5F4vi3-dTheg4-5O7fBgk-R/view?usp=drive_link)

### Book Status Dimension

```sql
CREATE OR REPLACE TABLE regexdb2.public.book_status_dim AS
SELECT
    ROW_NUMBER() OVER (ORDER BY online, offline) AS book_status_id,
    online,
    offline
FROM (
    SELECT DISTINCT
        CASE WHEN LOWER(online_order) = 'yes' THEN TRUE ELSE FALSE END AS online,
        CASE WHEN LOWER(book_table) = 'yes' THEN TRUE ELSE FALSE END AS offline
    FROM regexdb2.public.zomato_data
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/17rNjW0r0czBErMIbv9wxxOzVHrUNBvmg/view?usp=drive_link)

### Location Dimension

```sql
CREATE OR REPLACE TABLE regexdb2.public.location_dim AS
SELECT
    ROW_NUMBER() OVER (ORDER BY city) AS location_id,
    city
FROM (
    SELECT DISTINCT listed_in_city AS city
    FROM regexdb2.public.zomato_data
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/10lNR7hRBig4lM4yuSGJxzCTAWbwHdQfF/view?usp=drive_link)

### Cuisine Dimension

```sql
CREATE OR REPLACE TABLE regexdb2.public.cuisine_dim AS
SELECT
    ROW_NUMBER() OVER (ORDER BY cuisine) AS cuisine_id,
    cuisine
FROM (
    SELECT DISTINCT cuisines AS cuisine
    FROM regexdb2.public.zomato_data
    WHERE cuisines IS NOT NULL
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1TjQl-SgIVcJ34uhmYsynxqW9PQ2p-nAj/view?usp=drive_link)

### Fact Table

```sql
CREATE OR REPLACE TABLE regexdb2.public.restaurant_facts AS
SELECT
    TRY_TO_NUMBER(z.approx_cost_for_two_people) AS cost,
    TRY_TO_NUMBER(SPLIT_PART(z.rate, '/', 1)) AS rate,
    TRY_TO_NUMBER(z.votes) AS votes,
    r.r_id,
    l.location_id,
    b.book_status_id,
    c.cuisine_id
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
) z
JOIN regexdb2.public.restaurant_dim r ON z.name = r.name
JOIN regexdb2.public.location_dim l ON z.listed_in_city = l.city
JOIN regexdb2.public.book_status_dim b ON
    b.online = CASE WHEN LOWER(z.online_order) = 'yes' THEN TRUE ELSE FALSE END AND
    b.offline = CASE WHEN LOWER(z.book_table) = 'yes' THEN TRUE ELSE FALSE END
JOIN regexdb2.public.cuisine_dim c ON z.cuisines = c.cuisine
WHERE z.rn = 1;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1jBInLnC5alsEHRbcBbdDSzCbqDUM9cI5/view?usp=drive_link)

---

## ER Diagram

```mermaid
           +-----------------+
           | restaurant_dim   |
           |-----------------|
           | r_id (PK)       |
           | name            |
           | url             |
           | phone           |
           +-----------------+
                    |
        +-----------+-----------+
        |           |           |
+----------------+  |  +-----------------+     +----------------+
| book_status_dim|  |  | location_dim    |     | cuisine_dim    |
|----------------|  |  |-----------------|     |----------------|
| book_status_id |  |  | location_id (PK)|     | cuisine_id (PK)|
| online         |  |  | city            |     | cuisine        |
| offline        |  |  +-----------------+     +----------------+
+----------------+  |          
                    |          
                    |          
             +------------------+
             | restaurant_facts |
             |------------------|
             | r_id (FK)        |
             | location_id (FK) |
             | book_status_id(FK)|
             | cuisine_id (FK)  |
             | cost             |
             | rate             |
             | votes            |
             +------------------+

```

---

## Analytical Queries

### 1. Top Rated Restaurants in a City

```sql
SELECT r.name, l.city, f.rate
FROM restaurant_facts f
JOIN restaurant_dim r ON f.r_id = r.r_id
JOIN location_dim l ON f.location_id = l.location_id
WHERE l.city = 'Electronic City'
ORDER BY f.rate DESC
LIMIT 10;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1y0Ta-mqgB3TeW4IHDHL896DAwg0sJBQd/view?usp=drive_link)

### 2. Top Cuisine of a Restaurant Based on Votes

```sql
SELECT r.name, c.cuisine, f.votes
FROM restaurant_facts f
JOIN restaurant_dim r ON f.r_id = r.r_id
JOIN cuisine_dim c ON f.cuisine_id = c.cuisine_id
WHERE f.votes = (
    SELECT MAX(f2.votes)
    FROM restaurant_facts f2
    WHERE f2.r_id = f.r_id
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1j-8iBBYXjB0RRDgY6slzxR_29fiBVNn-/view?usp=drive_link)

### 3. Cuisine in Demand City-wise

```sql
SELECT city, cuisine, total_votes
FROM (
    SELECT l.city, c.cuisine, SUM(f.votes) AS total_votes
    FROM restaurant_facts f
    JOIN location_dim l ON f.location_id = l.location_id
    JOIN cuisine_dim c ON f.cuisine_id = c.cuisine_id
    GROUP BY l.city, c.cuisine
) city_cuisine_votes
WHERE (city, total_votes) IN (
    SELECT city, MAX(total_votes)
    FROM (
        SELECT l.city, c.cuisine, SUM(f.votes) AS total_votes
        FROM restaurant_facts f
        JOIN location_dim l ON f.location_id = l.location_id
        JOIN cuisine_dim c ON f.cuisine_id = c.cuisine_id
        GROUP BY l.city, c.cuisine
    ) sub
    GROUP BY city
);
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1HIvVmZtrbj5EJBK4rIrwXiCXmGrndWey/view?usp=drive_link)

### 4. Cloud Kitchens Count by City

```sql
SELECT l.city, COUNT(DISTINCT r.r_id) AS cloud_kitchen_count
FROM restaurant_facts f
JOIN restaurant_dim r ON f.r_id = r.r_id
JOIN location_dim l ON f.location_id = l.location_id
JOIN book_status_dim b ON f.book_status_id = b.book_status_id
WHERE b.offline = FALSE
GROUP BY l.city
ORDER BY cloud_kitchen_count DESC;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1arBirHRGYOxSvuQvMLK7KTRX0d8OHFig/view?usp=drive_link)

### 5. Top 5 Restaurants by Rating and Order Value

```sql
SELECT r.name, MAX(f.cost) AS max_order_value, AVG(f.cost) AS avg_order_value, MAX(f.rate) AS max_rating
FROM restaurant_facts f
JOIN restaurant_dim r ON f.r_id = r.r_id
GROUP BY r.name
ORDER BY max_rating DESC
LIMIT 5;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1J6ZgNzp6lVQzfC_Ws5DJ4QJKg8QZig0X/view?usp=drive_link)

### 6. Bottom 3 Cities by Online Delivery

```sql
SELECT l.city, COUNT(*) AS online_delivery_restaurant_count
FROM restaurant_facts f
JOIN location_dim l ON f.location_id = l.location_id
JOIN book_status_dim b ON f.book_status_id = b.book_status_id
WHERE b.online = TRUE
GROUP BY l.city
ORDER BY online_delivery_restaurant_count ASC
LIMIT 3;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1g0Q-KVjoM0sDLLFw3kx0NJUkWNS-1Lec/view?usp=drive_link)

### 7. Cheapest High-Rated Restaurant in a City

```sql
SELECT r.name, l.city, f.rate AS rating
FROM restaurant_facts f
JOIN restaurant_dim r ON f.r_id = r.r_id
JOIN location_dim l ON f.location_id = l.location_id
WHERE l.city = 'Electronic City' AND f.rate > 3.5
ORDER BY f.cost ASC
LIMIT 1;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1XGAqtO2ECIyk-K3XMi91vq-lIr5pWblL/view?usp=drive_link)

### 8. North Indian vs South Indian Exclusive Restaurants

```sql
WITH restaurant_cuisines AS (
    SELECT r.r_id, LOWER(c.cuisine) AS cuisine
    FROM restaurant_facts f
    JOIN restaurant_dim r ON f.r_id = r.r_id
    JOIN cuisine_dim c ON f.cuisine_id = c.cuisine_id
    GROUP BY r.r_id, LOWER(c.cuisine)
),
north_only AS (
    SELECT DISTINCT rni.r_id, 'North Indian Only' AS category
    FROM restaurant_cuisines rni
    LEFT JOIN restaurant_cuisines rsi ON rni.r_id = rsi.r_id AND rsi.cuisine LIKE '%south indian%'
    WHERE rni.cuisine LIKE '%north indian%' AND rsi.r_id IS NULL
),
south_only AS (
    SELECT DISTINCT rsi.r_id, 'South Indian Only' AS category
    FROM restaurant_cuisines rsi
    LEFT JOIN restaurant_cuisines rni ON rsi.r_id = rni.r_id AND rni.cuisine LIKE '%north indian%'
    WHERE rsi.cuisine LIKE '%south indian%' AND rni.r_id IS NULL
)
SELECT category, COUNT(*) AS restaurant_count
FROM (
    SELECT * FROM north_only
    UNION ALL
    SELECT * FROM south_only
) combined
GROUP BY category;
```
[🔗 See the result (Google Drive)](https://drive.google.com/file/d/1s822ICy0yJ9TojKHL2knNrq6jFaIt4IQ/view?usp=drive_link)

---



## Conclusion

This markdown captures the complete process of transforming raw Zomato data into an analytical model in Snowflake, designing dimensions, creating a fact table, and answering key business questions through SQL queries.