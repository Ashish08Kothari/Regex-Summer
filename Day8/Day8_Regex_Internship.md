# **Day 8 - Regex Software Services Internship**

## **Overview**
Today was Day 8 of my Data Engineering Internship at Regex Software Services. We explored the concept of **tuples** in Python and learned how to work with various **pattern printing problems** using nested loops. Tuples are immutable data structures in Python, and pattern printing helps build logic using loops. Below are the examples and code snippets we practiced today.
## **Tuple Access**
```python
a = (10, 20, 30, 40)
print(a[0])
```

**Output:**
```
10
```

## **Tuple Count Method**
```python
a = (10, 20, 30, 40)
print(a.count(10))
```

**Output:**
```
1
```

## **Right-Angled Triangle Pattern**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end = " ")
    print()
```

**Output:**
```
* 
* * 
* * * 
* * * *
```

## **Student Subject Pattern**
```python
for i in range(1, 4):
    print('Student', i)
    for j in range(1, 5 - i):
        print("Sub:", j, end = " ")
    print()
```

**Output:**
```
Student 1
Sub: 1 Sub: 2 Sub: 3 
Student 2
Sub: 1 Sub: 2 
Student 3
Sub: 1
```

## **Fixed Columns of Stars**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, 5):
        print('*', end = " ")
    print()
```

**Output:**
```
* * * * 
* * * * 
* * * * 
* * * *
```

## **Decreasing Stars Pattern**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print('*', end = " ")
    print()
```

**Output:**
```
* * * 
* * 
*
```

## **Row Number Pattern**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, 5):
        print(i, end = " ")
    print()
```

**Output:**
```
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4
```

## **Incrementing Even Number Rows**
```python
n = int(input('Enter no of rows: '))
num = 4
for i in range(1, n + 1):
    for j in range(1, 5):
        print(num, end=" ")
    num += 2
    print()
```

**Output:**
```
4 4 4 4 
6 6 6 6 
8 8 8 8 
10 10 10 10
```

## **Column Number Pattern**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, 5):
        print(j, end = " ")
    print()
```

**Output:**
```
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4
```

## **Fixed Range Numbers**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(4, 8):
        print(j, end=" ")
    print()
```

**Output:**
```
4 5 6 7 
4 5 6 7 
4 5 6 7 
4 5 6 7
```

## **Alphabet Pattern with chr()**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(65, 68):
        print(chr(j), end = " ")
    print()
```

**Output:**
```
A B C 
A B C 
A B C 
A B C
```

## **Continuous Number Pattern**
```python
num = 1
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(num, num + 4):
        print(num, end = "")
        num += 1
    print()
```

**Output:**
```
1234
5678
9101112
13141516
```

## **Row-wise Increasing Numbers**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
```

**Output:**
```
1 
1 2 
1 2 3 
1 2 3 4
```

## **Row-wise Increasing from 4**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(4, 4 + i):
        print(j, end=" ")
    print()
```

**Output:**
```
4 
4 5 
4 5 6 
4 5 6 7
```

## **Cumulative Number Triangle**
```python
num = 1
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end = "")
        num += 1
    print()
```

**Output:**
```
1
23
456
78910
```

## **Alphabetic Triangle**
```python
num = 65
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(num), end="")
        num += 1
    print()
```

**Output:**
```
A
BC
DEF
GHIJ
```

## **Increasing Series in Rows**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(i, i + i):
        print(j, end="")
    print()
```

**Output:**
```
1
23
345
4567
```

## **Left-aligned Pyramid with Dashes**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, 4 - i + 1):
        print('-', end=" ")
    for k in range(1, i + 1):
        print('*', end=" ")
    print()
```

**Output:**
```
- - - * 
- - * * 
- * * * 
* * * *
```

## **Right-aligned Decreasing Stars**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    for j in range(1, i):
        print('-', end = "")
    for k in range(1, n - i + 2):
        print('*' , end = "")
    print()
```

**Output:**
```
****
-***
--**
---*
```

## **Alternating 1 and 0 Pattern**
```python
n = int(input('Enter no of rows: '))
for i in range(1, n + 1):
    if i % 2 != 0:
        num = True
    else:
        num = False
    for j in range(1, i + 1):
        print(1 if num else 0, end = "")
        num = not num
    print()
```

**Output:**
```
1
01
101
0101
```