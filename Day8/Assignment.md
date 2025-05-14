# Assignment

## Program 1: Alphabet Pattern (Decreasing ASCII Start)
```python
from ast import Num
n = int(input('Enter no of rows: '))
num = 69
for i in range(1,n+1):
  temp = num
  for j in range(1,i+1):
    print(chr(temp),end=" ")
    temp += 1
  num -= 1
  print()
```
**Output (for n = 5):**
```
E 
D E 
C D E 
B C D E 
A B C D E 
```

## Program 2: Right-Aligned Rectangle of Stars
```python
n = int(input('Enter no of rows: '))
for i in range(1,n+1):
  for j in range(1,i):
    print(" ",end="")
  for k in range(1,5):
    print('*',end="")
  print()
```
**Output (for n = 5):**
```
****
 ****
  ****
   ****
    ****
```

## Program 3: Center-Aligned Rectangle of Stars
```python
n = int(input('Enter no of rows: '))
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end = "")
  for k in range(1,6):
    print('*',end = " ")
  print()
```
**Output (for n = 5):**
```
    * * * * * 
   * * * * * 
  * * * * * 
 * * * * * 
* * * * * 
```

## Program 4: Center-Aligned Numbers
```python
n = int(input('Enter no of rows: '))
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end = "")
  for k in range(1,6):
    print(k,end = " ")
  print()
```
**Output (for n = 5):**
```
    1 2 3 4 5 
   1 2 3 4 5 
  1 2 3 4 5 
 1 2 3 4 5 
1 2 3 4 5 
```

## Program 5: Center-Aligned Alphabets
```python
n = int(input('Enter no of rows: '))
for i in range(1,n+1):
  z = 65
  for j in range(1,n-i+1):
    print(" ",end = "")
  for k in range(1,6):
    print(chr(z),end = " ")
    z += 1
  print()
```
**Output (for n = 5):**
```
    A B C D E 
   A B C D E 
  A B C D E 
 A B C D E 
A B C D E 
```

## Program 6: Hollow Pyramid
```python
n = int(input('Enter no of rows: '))
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end = "")
  for k in range(1,2*i):
    if i != n:
      if(k == 1 or k == 2*i - 1):
        print('*',end = "")
      else:
        print(" ",end = "")
    else:
      print('*',end = "")
  print()
```
**Output (for n = 5):**
```
    *
   * *
  *   *
 *     *
*********
```

## Program 7: Diamond Star Pattern
```python
n = int(input('Enter no of rows: '))
for i in range(1, n+1):
  for j in range(1, i+1):
    print('*',end="")
  print()
for k in range(1,n):
  for z in range(k,n):
    print('*',end = "")
  print()
```
**Output (for n = 5):**
```
*
**
***
****
*****
****
***
**
*
```
