# **Day 10 - RegEx Software Services Internship**

---

## **Overview of the Day**

On Day 10 of my Data Engineering Internship at RegEx Software Services, I continued deepening my understanding of Python. The major topics covered were:

- Different types of function arguments
- Lambda (anonymous) functions
- `map()` and `filter()` functions for functional programming
- File handling operations: reading, writing, appending
- Using the `csv` module to read and write CSV files

---

## **Function Arguments in Python**

### 🔹 Key Points:
- **Positional arguments**: Values are passed in order.
- **Keyword arguments**: Arguments are passed by name.
- **Default arguments**: Default values are provided if not passed.

```python
def f(x,y,z):
  print(f'{x} {y} {z}')

f(10,20,30)  # Position Argument
f(x = 10, y = 20, z = 30)  # Keyword argument
```
**Output:**
```
10 20 30
10 20 30
```

---

```python
def f(x,y,z = 15):  # Default parameter
  print(f'{x} {y} {z}')

f(10,20)
```
**Output:**
```
10 20 15
```

---

## **Return Statement in Functions**

### 🔹 Key Points:
- `return` is used to return a value from a function for further use.

```python
def f(x):
  return x + 50

x = f(10)
print(x)
```
**Output:**
```
60
```

---

```python
def f(x):
  print(x + 50)

x = f(10)
print(x)
```
**Output:**
```
60
None
```

---

## **Lambda Functions**

### 🔹 Key Points:
- Anonymous, one-line functions.
- Created using the `lambda` keyword.

```python
x = lambda num : num + 5
print(x(5))
```
**Output:**
```
10
```

---

## **`map()` Function**

### 🔹 Key Points:
- Applies a function to all items in an iterable.
- Returns a map object (lazy evaluation).

```python
print(tuple(map(len, ['hey', 'hello'])))
print(list(map(len, ['hey', 'hello'])))
```
**Output:**
```
(3, 5)
[3, 5]
```

---

```python
list(map(lambda x : pow(x, 2), [10, 5, 4, 3]))
```
**Output:**
```
[100, 25, 16, 9]
```

---

## **`filter()` Function**

### 🔹 Key Points:
- Filters elements from iterable based on a function that returns boolean.

```python
list(filter(lambda x : x % 2 == 0, [10, 5, 4, 3]))
```
**Output:**
```
[10, 4]
```

---

## **File Handling in Python**

### 🔹 Key Points:
- Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'r+'` (read/write).
- Always close files using `close()` or use `with` statement for safety.

```python
f = open("/Users/ashish/Desktop/Python/user.txt", "r")
print(f.read())
f.close()
```
**Output:**
_(Contents of the file will be printed)_

---

```python
f = open("/Users/ashish/Desktop/Python/user.txt", "w")
print(f.write("Ishaan"))
f.close()
```
**Output:**
```
6
```

---

```python
f = open("/Users/ashish/Desktop/Python/abc.txt", "w")
print(f.write("aise he"))
f.close()
```
**Output:**
```
7
```

---

```python
f = open("/Users/ashish/Desktop/Python/abc.txt", "r+")
print(f.read())
f.write("japan")
f.close()
```
**Output:**
_(Reads file and then appends "japan" to it)_

---

```python
f = open("/Users/ashish/Desktop/Python/abc.txt", "a")
f.write("####")
f.close()
```
**Output:**
_Appends `####` at the end of file._

---

```python
f = open("abc.txt", "r")
for line in f:
  print(line.split(","))
```
**Output:**
_(Each line from file is split by commas and printed as list)_

---

## **CSV File Handling Using `csv` Module**

### 🔹 Key Points:
- The `csv` module provides functionality to read from and write to CSV files easily.

```python
import csv
with open('currency.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        for data in row:
            print(data, end="    ")
        print()
```
**Output:**
_Contents of `currency.csv` printed row by row._

---

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('currency.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```
**Output:**
_Creates/overwrites `currency.csv` with provided rows._

---

_End of Day 10 Log._
