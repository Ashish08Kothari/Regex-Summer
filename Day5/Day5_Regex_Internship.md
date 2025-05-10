# **Day5_Regex_Internship**

## **Overview**

On Day 5 of the Regex Internship, we started by understanding the difference between **Data Science** and **Data Engineering**, followed by a comprehensive introduction to **Python programming**. Topics covered included variables, printing techniques, string formatting, comments, operators, conditional statements, and string slicing/indexing.

---

## **Data Science vs Data Engineering**

**Data Science** is primarily focused on analyzing and interpreting complex data to support decision-making using statistics, machine learning, and data visualization.

**Data Engineering** focuses on building data pipelines and infrastructure to collect, store, and prepare data for analysis.

| Feature             | Data Science                     | Data Engineering                      |
|---------------------|----------------------------------|----------------------------------------|
| Focus               | Analysis & modeling              | Infrastructure & data pipelines       |
| Tools               | Python, R, Jupyter, Pandas       | SQL, Spark, Airflow, Kafka            |
| Output              | Reports, models, predictions     | Clean, structured, usable data        |
| Skills              | Statistics, ML, Visualization    | ETL, Database Systems, Programming    |

---

## **Python Basics**

### **Printing in Python**
```python
print("Hello World", end = "-")
print("Hello Ashish")
```

### **Variables and Data Types**
```python
x = '10'
print(type(x))
```

### **Concatenation and Print with Variables**
```python
y = 2025
company = "Regex Software"
print("My year is", y)
print("Company name is", company)
```

### **String Formatting using f-strings**
```python
y = 2025
company = "Regex Software"
print(f"My year is {y} and company is {company}")
```

### **Multiline Strings**
```python
x = '''bla bla bla bla
bla bla bla bla
bla bla bla '''
print(x)
```

---

## **Comments in Python**

### **Single-line Comment**
```python
# This is a comment
```

### **Multi-line Comment**
```python
''' 
Multiline Comment
Line 1
Line 2
Line 3
'''
```

---

## **String Example and Output Understanding**
```python
username = "Tushar"
message = f"Happy bd {username}"
print(message)

username = "Isha"
print(message)
```

---

## **Basic Arithmetic Operators**
```python
print(5 + 3)   # 8
print(10 - 4)  # 6
print(2 ** 3)  # 8
print(10 // 3) # 3
```

---

## **Comparison Operators**
```python
print(5 == 5)
print(5 != 3)
print(7 > 2)
```

---

## **Conditional Statements**

### **if-else**
```python
x = 10
if x > 5:
    print("Greater than 5")
else:
    print("Less or equal to 5")
```

### **if-elif-else**
```python
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

### **Nested if-else**
```python
x = 15
if x > 10:
    if x < 20:
        print("Between 10 and 20")
    else:
        print("Greater than or equal to 20")
else:
    print("10 or less")
```

---

## **String Indexing and Slicing**
```python
text = "RegexInternship"
print(text[0])      # R
print(text[-1])     # p
print(text[0:5])    # Regex
print(text[5:])     # Internship
print(text[:5])     # Regex
```