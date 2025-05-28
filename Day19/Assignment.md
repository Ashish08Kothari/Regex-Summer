# **Day 20 - Regex Internship**

## **Zomato Dataset Loading using Snowflake**

Today’s task was focused on loading structured data into a Snowflake table using AWS S3 and the `COPY INTO` command. Here's a detailed walkthrough of what was done.

---

## **Step 1: Create Table in Snowflake**

We first created a table in the Snowflake database to store Zomato data. The table structure is defined based on the columns from the CSV file.

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

## ✅ Explanation:

We use CREATE OR REPLACE to ensure the table is newly created or overwritten if it already exists.

All fields are of type STRING because the dataset primarily consists of textual and numerical data stored as strings.

## **Step 2: Load Data Using COPY INTO**

Once the table is ready, the next step is to load data from a CSV file stored in an AWS S3 bucket. We use an external stage already configured in Snowflake for accessing the bucket.


```sql
COPY INTO regexdb2.public.zomato_data
FROM (
    SELECT 
        $1::STRING AS url,
        $2::STRING AS address,
        $3::STRING AS name,
        $4::STRING AS online_order,
        $5::STRING AS book_table,
        $6::STRING AS rate,
        $7::STRING AS votes,
        $8::STRING AS phone,
        $9::STRING AS location,
        $10::STRING AS rest_type,
        $11::STRING AS dish_liked,
        $12::STRING AS cuisines,
        $13::STRING AS approx_cost_for_two_people,
        $14::STRING AS reviews_list,
        $15::STRING AS menu_item,
        $16::STRING AS listed_in_type,
        $17::STRING AS listed_in_city
    FROM @manage_db2.external_stages.aws_stage/zomato.csv
)
FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1);

```

## ✅ Explanation:
$1, $2, etc. are positional references to columns in the CSV file.

We explicitly cast each field to STRING.

The file is accessed from a Snowflake external stage that points to an S3 location.

FILE_FORMAT tells Snowflake how to interpret the file (CSV format, commas as delimiters, and skipping the header row).



## **Step 3: Verify the Data Load**
After the data is copied, we run a simple SELECT query to ensure everything was loaded correctly:

```sql
SELECT * FROM regexdb2.public.zomato_data;
```

## ✅ Explanation:

This query fetches all records from the zomato_data table.

We use this to visually verify that the file was loaded as expected.


## Summary of Learnings

✔️ Created a structured table in Snowflake matching the CSV schema.

✔️ Used Snowflake external stages to access data in an S3 bucket.

✔️ Loaded data efficiently using the COPY INTO command.

✔️ Verified data through querying the target table.

This task helped reinforce how Snowflake integrates with cloud storage like AWS S3 and handles large-scale data ingestion seamlessly.