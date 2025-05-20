
# **Day 13 - Series, Dictionary to DataFrame, CSV Handling, and Web Scraping**

---

## 📘 **Overview**

Today’s session covered key concepts of Pandas for handling one-dimensional and two-dimensional data structures using Series and DataFrames. Additionally, we explored how to save data to CSV, read CSVs, and fetch live data using web scraping tools and browser extensions like Instant Data Scraper and Polymer AI.

---

## 📌 **1. Creating a Series**

A **Pandas Series** is a one-dimensional labeled array capable of holding any data type.

```python
import pandas as pd
series1 = pd.Series([10,20,30,40])
type(series1)
series1
```

**🖨️ Output:**

```
0    10
1    20
2    30
3    40
dtype: int64
```

- `pd.Series()` creates a one-dimensional array with labeled index.

---

## 📌 **2. Creating a DataFrame from Dictionary**

A **DataFrame** is a two-dimensional, size-mutable, and heterogeneous data structure.

```python
a = {
    'Name' : ['Ashish', 'Manan', 'Priyansh', 'Abhishek'],
    'Domain' : ['D.E.', 'Full Stack', 'D.s.', "Core Java"],
    'Duration' : [60, 45, 30, 15]
}

df = pd.DataFrame(a)
df
```

**🖨️ Output:**

```
       Name      Domain  Duration
0    Ashish         D.E.        60
1     Manan  Full Stack        45
2  Priyansh         D.s.        30
3  Abhishek    Core Java        15
```

- `pd.DataFrame()` converts a dictionary into a tabular format (rows and columns).

---

## 📌 **3. Saving DataFrame to CSV**

```python
df.to_csv('example.csv')
```

- `to_csv()` saves the DataFrame to a CSV file.

---

## 📌 **4. Reading Data from CSV Files**

```python
dine = pd.read_csv('Dine.csv')
dine
```

```python
flipkart = pd.read_csv('flipkart.csv')
flipkart
```

```python
pd.read_csv('makemytrip.csv')
```

```python
pd.read_csv('in.csv')
```

- `pd.read_csv()` reads data from a CSV file and returns a DataFrame.
- This is especially useful for loading live scraped data exported via Instant Data Scraper or Polymer AI.

---

## ✅ **Web Scraping Tools Introduced**

- **Instant Data Scraper**: A browser extension that can auto-detect and extract tabular data from web pages.
- **Polymer AI**: A no-code tool to analyze and export structured data from websites.

---

Let me know if you have more code or topics to include for Day 13 before I generate the final downloadable file.
