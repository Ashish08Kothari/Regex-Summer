-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS zomato_db;
USE zomato_db;

-- Drop the table if it already exists
DROP TABLE IF EXISTS zomato_table;

-- Create the Zomato table
CREATE TABLE zomato_table (
    url TEXT,
    address TEXT,
    name VARCHAR(255),
    online_order VARCHAR(10),
    book_table VARCHAR(10),
    rate VARCHAR(10),
    votes INT,
    phone VARCHAR(50),
    location VARCHAR(100),
    rest_type TEXT,
    dish_liked TEXT,
    cuisines TEXT,
    approx_cost VARCHAR(50),
    reviews_list TEXT,
    menu_item TEXT,
    listed_in_type VARCHAR(100),
    listed_in_city VARCHAR(100)
);
