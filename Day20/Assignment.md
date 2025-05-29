
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
    r.r_id,
    z.name,
    CASE WHEN LOWER(z.online_order) = 'yes' THEN TRUE ELSE FALSE END AS online,
    CASE WHEN LOWER(z.book_table) = 'yes' THEN TRUE ELSE FALSE END AS offline
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
) z
JOIN regexdb2.public.restaurant_dim r
  ON z.name = r.name
WHERE z.rn = 1;







CREATE OR REPLACE TABLE regexdb2.public.location_dim AS
SELECT 
    address,
    listed_in_city AS city,
    r.r_id
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
) z
JOIN regexdb2.public.restaurant_dim r
  ON z.name = r.name
WHERE z.rn = 1;








CREATE OR REPLACE TABLE regexdb2.public.restaurant_facts AS
SELECT
    TRY_TO_NUMBER(z.approx_cost_for_two_people) AS cost,
    TRY_TO_NUMBER(SPLIT_PART(z.rate, '/', 1)) AS rate,
    TRY_TO_NUMBER(z.votes) AS votes,
    r.r_id
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY name ORDER BY name) AS rn
    FROM regexdb2.public.zomato_data
) z
JOIN regexdb2.public.restaurant_dim r
  ON z.name = r.name
WHERE z.rn = 1;









select * from regexdb2.public.restaurant_dim;
select * from regexdb2.public.book_status_dim;
select * from regexdb2.public.location_dim;
select * from regexdb2.public.restaurant_facts;







```