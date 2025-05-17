# **Day 11 – Regex Internship**

## 📝 Overview

Today I learned about Object-Oriented Programming (OOP) in Python. The session included an introduction to OOP concepts, their practical use cases, and implementation through Python classes. Here's a summary of what was covered:

---

## 📌 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data in the form of fields (attributes) and code in the form of methods (functions).

### Key Concepts Covered:

### ✅ Class:
A class is a blueprint for creating objects. It defines attributes and methods that its objects will have.

### ✅ Object:
An object is an instance of a class. It holds real data and functionalities defined in the class.

### ✅ Instance:
Each object created from a class is called an instance of that class.

### ✅ Constructor:
A special method `__init__()` used to initialize newly created objects.

### ✅ Inheritance:
Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.

---

## 🧪 Code Examples and Outputs

### 📘 Class and Object Example
```python
class HouseDesign:
  color = "Yellow"

h1 = HouseDesign()
print(h1.color)
```
**Output:**
```
Yellow
```

```python
h2 = HouseDesign()
h2.color = "white"
print(h2.color)
```
**Output:**
```
white
```

---

### 🏗 Constructor Usage
```python
class HouseDesign:
  def __init__(self):
    print("Mistri")
  color = "Yellow"

h1 = HouseDesign()
```
**Output:**
```
Mistri
```

```python
class HouseDesign:
  def __init__(self):
    print("Mistri",self)

h1 = HouseDesign()
print(h1)
```
**Output:**
```
Mistri <__main__.HouseDesign object at MEMORY_ADDRESS>
<__main__.HouseDesign object at MEMORY_ADDRESS>
```

---

### 🎨 Constructor with Arguments
```python
class HouseDesign:
  def __init__(self,color):
    self.color = color

h1 = HouseDesign("Green")
h2 = HouseDesign("Pink")
print("h1: ",h1.color)
print("h2: ",h2.color)
```
**Output:**
```
h1:  Green
h2:  Pink
```

---

### 👪 Inheritance Example
```python
class Parent:
  amount = 50000

class Child:
  salary = 10000

c1 = Child()
print(c1.salary)
```
**Output:**
```
10000
```

```python
class Parent:
  amount = 50000

class Child(Parent):
  salary = 10000

c1 = Child()
print(c1.salary + c1.amount)
```
**Output:**
```
60000
```

---

### 🚗 Driver Class
```python
class driver:
  def __init__(self,id,name,email):
    self.id = id
    self.name = name
    self.email = email

d1 = driver(1,'Suresh','suresh@gmail.com')
print(d1.id,d1.name,d1.email)

d2 = driver(2,"Mukesh","mukesh@gmail.com")
print(d2.id,d2.name,d2.email)
```
**Output:**
```
1 Suresh suresh@gmail.com
2 Mukesh mukesh@gmail.com
```

---

### 🧍 Customer Class
```python
class customer:
  def __init__(self,id,name,email,wallet):
    self.id = id
    self.name = name
    self.email = email
    self.wallet = wallet

c1 = customer(101,"Ashish","ashish@gmail.com",250)
print(c1.id,c1.name,c1.email,c1.wallet)
```
**Output:**
```
101 Ashish ashish@gmail.com 250
```

---

### 🧬 Inheritance with super()
```python
class driver:
  def __init__(self,id,name,email):
    self.id = id
    self.name = name
    self.email = email

class customer(driver):
  def __init__(self,id,name,email,wallet):
    super().__init__(id,name,email)
    self.wallet = wallet

c1 = customer(101,"Ashish","ashish@gmail.com",250)
print(c1.id,c1.name,c1.email,c1.wallet)
```
**Output:**
```
101 Ashish ashish@gmail.com 250
```

---

### 🧑‍💼 Employee Class with Methods
```python
class employee:
  def __init__(self,id,name,email,anual_salary):
    self.id = id
    self.name = name
    self.email = email
    self.anual_salary = anual_salary

  def monthly_salary(self):
    print(self.anual_salary / 12)

  def domain(self):
    x = self.email.split('@')
    print(x[1])

e1 = employee(1,"Ashish","ashish@gmail.com",90000)
print(e1.name,e1.id,e1.email,e1.anual_salary)
e1.monthly_salary()
e1.domain()
```
**Output:**
```
Ashish 1 ashish@gmail.com 90000
7500.0
gmail.com
```
