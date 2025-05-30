# **Day 21 - Zomato Star Schema Queries**
**Date:** May 30, 2025

## 📝 Summary
Today’s session was a continuation of the previous day’s work on the Zomato dataset using the Star Schema design. We performed several analytical SQL queries on the Snowflake database to extract meaningful insights from the dataset.

---

## 📊 Queries Performed on Star Schema

### 🔹 Top Rated Restaurants in a City

```sql
SELECT 
    r.name AS restaurant_name,
    l.city,
    f.rate
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
WHERE l.city = 'Electronic City'  
ORDER BY f.rate DESC NULLS LAST
LIMIT 10;
```

---

### 🔹 Top Cuisine of a Restaurant as per Votes

```sql
SELECT 
    r.name AS restaurant_name,
    c.cuisine,
    f.votes
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
JOIN regexdb2.public.cuisine_dim c ON f.cuisine_id = c.cuisine_id
WHERE f.votes = (
    SELECT MAX(f2.votes)
    FROM regexdb2.public.restaurant_facts f2
    WHERE f2.r_id = f.r_id
);
```

---

### 🔹 Cuisine in Demand City-Wise

```sql
SELECT 
    city,
    cuisine,
    total_votes
FROM (
    SELECT 
        l.city,
        c.cuisine,
        SUM(f.votes) AS total_votes
    FROM regexdb2.public.restaurant_facts f
    JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
    JOIN regexdb2.public.cuisine_dim c ON f.cuisine_id = c.cuisine_id
    GROUP BY l.city, c.cuisine
) AS city_cuisine_votes
WHERE (city, total_votes) IN (
    SELECT 
        city,
        MAX(total_votes)
    FROM (
        SELECT 
            l.city,
            c.cuisine,
            SUM(f.votes) AS total_votes
        FROM regexdb2.public.restaurant_facts f
        JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
        JOIN regexdb2.public.cuisine_dim c ON f.cuisine_id = c.cuisine_id
        GROUP BY l.city, c.cuisine
    ) AS sub
    GROUP BY city
);
```

---

### 🔹 Number of Cloud Kitchens in Each City

```sql
SELECT 
    l.city,
    COUNT(DISTINCT r.r_id) AS cloud_kitchen_count
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
JOIN regexdb2.public.book_status_dim b ON f.book_status_id = b.book_status_id
WHERE b.offline = FALSE
GROUP BY l.city
ORDER BY cloud_kitchen_count DESC;
```

---

### 🔹 Top 5 Restaurants Based on Ratings and Cost

```sql
SELECT
    r.name AS restaurant_name,
    MAX(f.cost) AS max_order_value,
    AVG(f.cost) AS avg_order_value,
    MAX(f.rate) AS max_rating
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
GROUP BY r.name
ORDER BY max_rating DESC NULLS LAST
LIMIT 5;
```

---

### 🔹 Bottom 3 Cities Based on Online Delivery

```sql
SELECT 
    l.city,
    COUNT(*) AS online_delivery_restaurant_count
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
JOIN regexdb2.public.book_status_dim b ON f.book_status_id = b.book_status_id
WHERE b.online = TRUE
GROUP BY l.city
ORDER BY online_delivery_restaurant_count ASC
LIMIT 3;
```

---

### 🔹 Restaurant with Minimum Cost but High Rating

```sql
SELECT 
    r.name AS restaurant_name,
    l.city,
    f.rate AS rating
FROM regexdb2.public.restaurant_facts f
JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
JOIN regexdb2.public.location_dim l ON f.location_id = l.location_id
WHERE l.city = 'Electronic City'
  AND f.rate > 3.5
ORDER BY f.cost ASC
LIMIT 1;
```

---

### 🔹 Restaurants Selling Only North Indian or Only South Indian Cuisine

```sql
WITH restaurant_cuisines AS (
    SELECT 
        r.r_id,
        LOWER(c.cuisine) AS cuisine
    FROM regexdb2.public.restaurant_facts f
    JOIN regexdb2.public.restaurant_dim r ON f.r_id = r.r_id
    JOIN regexdb2.public.cuisine_dim c ON f.cuisine_id = c.cuisine_id
    GROUP BY r.r_id, LOWER(c.cuisine)
),
north_only AS (
    SELECT DISTINCT rni.r_id, 'North Indian Only' AS category
    FROM restaurant_cuisines rni
    LEFT JOIN restaurant_cuisines rsi 
        ON rni.r_id = rsi.r_id AND rsi.cuisine LIKE '%south indian%'
    WHERE rni.cuisine LIKE '%north indian%'
      AND rsi.r_id IS NULL
),
south_only AS (
    SELECT DISTINCT rsi.r_id, 'South Indian Only' AS category
    FROM restaurant_cuisines rsi
    LEFT JOIN restaurant_cuisines rni 
        ON rsi.r_id = rni.r_id AND rni.cuisine LIKE '%north indian%'
    WHERE rsi.cuisine LIKE '%south indian%'
      AND rni.r_id IS NULL
)

SELECT 
    category,
    COUNT(*) AS restaurant_count
FROM (
    SELECT * FROM north_only
    UNION ALL
    SELECT * FROM south_only
) combined
GROUP BY category;
```

---

## ✅ Conclusion
These queries helped us explore and analyze key insights from the restaurant data stored in our Star Schema model. We leveraged joins, filtering, aggregation, subqueries, and CTEs to gain business intelligence from structured data.

