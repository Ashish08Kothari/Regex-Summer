# **Day 9 - RegEx Software Services Internship**

---

## **Overview of the Day**

Today marked the ninth day of my Data Engineering Internship at RegEx Software Services. I spent the day learning about **dictionaries** and **functions** in Python. I explored various dictionary methods, how to manipulate key-value pairs, and how dictionary and list comprehensions work. Later, I was introduced to defining and calling functions, including parameterized functions, functions with return values, and pattern-based logic inside functions.

---

## **Dictionaries in Python**

### 🔹 Key Points:
- A dictionary is a collection of key-value pairs.
- Dictionaries are unordered, mutable, and indexed.
- Keys must be unique and immutable.
- Common dictionary methods include `.get()`, `.pop()`, `.popitem()`, `.keys()`, `.values()`.

### 🔹 Code Examples:

```python
a = {
    10:'Tushar',
    20:'Yash'
}
print(a)
```
**Output:**
```
{10: 'Tushar', 20: 'Yash'}
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
print(a[10])
```
**Output:**
```
Tushar
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
print(a.get(10))
```
**Output:**
```
Tushar
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
a[10] = 'Ishaan'
print(a)
```
**Output:**
```
{10: 'Ishaan', 20: 'Yash'}
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
a['Amount'] = 1000
print(a)
```
**Output:**
```
{10: 'Tushar', 20: 'Yash', 'Amount': 1000}
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
a.pop(20)
print(a)
```
**Output:**
```
{10: 'Tushar'}
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
a.popitem()
print(a)
```
**Output:**
```
{10: 'Tushar'}
```

---

```python
a = {
    10:'Tushar',
    20:'Yash'
}
print(help(a))
```
**Output:**
_(Displays dictionary method documentation)_

---

```python
a = {10: 'Tushar', 20: 'Yash', 'Amount': 1000}
a.values()
```
**Output:**
```
dict_values(['Tushar', 'Yash', 1000])
```

---

```python
{10: 'Tushar', 20: 'Yash', 'Amount': 1000}
a.keys()
```
**Output:**
```
dict_keys([10, 20, 'Amount'])
```

---

```python
data = 'hey'
d = {'Total' : len(data)}
print(d)
```
**Output:**
```
{'Total': 3}
```

---

```python
data = 'user'
d = {}
for char in data:
  d[char] = 1
print(d)
```
**Output:**
```
{'u': 1, 's': 1, 'e': 1, 'r': 1}
```

---

```python
data = "hey isha"
d = {}
for char in data:
  if(char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u'):
    d[char] = 1
print(d)
```
**Output:**
```
{'e': 1, 'i': 1, 'a': 1}
```

---

```python
data = "hey ishaeea"
d = {}
for char in data:
  if char in 'aeiou':
    if char not in d:
      d[char] = 1
    else:
      d[char] = d[char] + 1
print(d)
```
**Output:**
```
{'e': 3, 'i': 1, 'a': 2}
```

---

```python
[i+5 for i in [10,20,30,40]]
```
**Output:**
```
[15, 25, 35, 45]
```

---

```python
{char : 1 for char in 'hey'}
```
**Output:**
```
{'h': 1, 'e': 1, 'y': 1}
```

---

## **Functions in Python**

### 🔹 Key Points:
- Functions are blocks of reusable code.
- Defined using the `def` keyword.
- Can take parameters and return values.
- Help organize and modularize code.

### 🔹 Code Examples:

```python
def test():
  print('Hola !')
```
**Output (when called):**
```
Hola !
```

---

```python
a = 100  # global
def test():
  z = 19
  print(f'Hola {z} {a}')

test()
print(a)
```
**Output:**
```
Hola 19 100
100
```

---

```python
def msg(user):
  print(f'Hola {user}')

msg('Ashish')
msg('Tushar')
msg('Virat')
```
**Output:**
```
Hola Ashish
Hola Tushar
Hola Virat
```

---

```python
def sum(num):
    total = 0
    for i in range(1,num+1):
      total += i
    print(f'Total is {total}')

sum(10)
sum(5)
```
**Output:**
```
Total is 55
Total is 15
```

---

```python
def pattern(n):
  for i in range(1,n+1):
    for j in range(1,i):
      print('-',end = "")
    for k in range(1,n-i+2):
      print(k,end = "")
    print()

pattern(4)
print()
pattern(6)
```
**Output:**
```
1234
-123
--12
---1

123456
-12345
--1234
---123
----12
-----1
```

---

```python
def lcm(num1,num2):
  s = max(num1,num2)
  while(num1 % s != 0 and num2 % s != 0):
    s += 1
  print(f'LCM of {num1} and {num2} is {s}')

lcm(2,4)
```
**Output:**
```
LCM of 2 and 4 is 4
```

---

```python
def check(num):
  numstr = str(num)
  length = len(numstr)
  newnumber = 0
  for i in numstr:
    intnum = int(i)
    newnumber += pow(intnum,length)
  print('Yes' if newnumber == num else 'No')

check(153)
```
**Output:**
```
Yes
```

---

```python
def palindrome(num):
  newnum = 0
  temp = num
  while(temp != 0):
    newnum *= 10
    newnum += temp % 10
    temp //= 10
  print('Yes' if num == newnum else 'No')

palindrome(11)
palindrome(121)
palindrome(10)
```
**Output:**
```
Yes
Yes
No
```

---

```python
# func(10,20) Position argument
# func(a = 10, b = 20) Keyword Argument
```
**Note:**
- Positional arguments pass values in order.
- Keyword arguments specify which parameter gets which value.

---

_End of Day 9 Log._
