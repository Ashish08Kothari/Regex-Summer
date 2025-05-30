
```sql
SHOW STAGES IN SCHEMA manage_db2.external_stages;
list @manage_db2.external_stages.aws_stage;







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




CREATE OR REPLACE TABLE regexdb2.public.location_dim AS
SELECT 
    ROW_NUMBER() OVER (ORDER BY city) AS location_id,
    city
FROM (
    SELECT DISTINCT listed_in_city AS city
    FROM regexdb2.public.zomato_data
);






CREATE OR REPLACE TABLE regexdb2.public.restaurant_facts AS
SELECT
    TRY_TO_NUMBER(z.approx_cost_for_two_people) AS cost,
    TRY_TO_NUMBER(SPLIT_PART(z.rate, '/', 1)) AS rate,
    TRY_TO_NUMBER(z.votes) AS votes,
    r.r_id,
    l.location_id,
    b.book_status_id
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
) z
JOIN regexdb2.public.restaurant_dim r ON z.name = r.name
JOIN (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY city) AS location_id,
        city
    FROM (
        SELECT DISTINCT listed_in_city AS city
        FROM regexdb2.public.zomato_data
    )
) l ON z.listed_in_city = l.city
JOIN (
    SELECT 
        *,
        ROW_NUMBER() OVER (ORDER BY online, offline) AS book_status_id
    FROM (
        SELECT DISTINCT
            CASE WHEN LOWER(online_order) = 'yes' THEN TRUE ELSE FALSE END AS online,
            CASE WHEN LOWER(book_table) = 'yes' THEN TRUE ELSE FALSE END AS offline
        FROM regexdb2.public.zomato_data
    )
) b ON 
    b.online = CASE WHEN LOWER(z.online_order) = 'yes' THEN TRUE ELSE FALSE END AND
    b.offline = CASE WHEN LOWER(z.book_table) = 'yes' THEN TRUE ELSE FALSE END
WHERE z.rn = 1;










select * from regexdb2.public.restaurant_dim;
select * from regexdb2.public.book_status_dim;
select * from regexdb2.public.location_dim;
select * from regexdb2.public.restaurant_facts;













```