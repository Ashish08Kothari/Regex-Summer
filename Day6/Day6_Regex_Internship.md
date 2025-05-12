# **Day 6 - Regex Software Services Internship**

## **Day Overview:**
On the sixth day of my internship, I learned about basic looping constructs in Python such as for loops, while loops, and the control statements break and continue. Using these concepts, we performed simple calculations and number-based logic like summation, checking factors, and identifying prime numbers. These are fundamental building blocks in data processing and are very important for a Data Engineer. Each concept was explained through small coding exercises, which made the learning process very helpful.

---

## **1. For Loop with Decrement**

```python
for i in range(8, 2, -1):
    print(i, end=" ")
```

---

## **2. Summation Using For Loop**

```python
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
```

---

## **3. Count Numbers from 80 to 57**

```python
cnt = 0
for i in range(80, 56, -1):
    cnt += 1
print(cnt)
```

---

## **4. Numbers Divisible by 2 and 6 Between 20 and 55**

```python
for i in range(20, 56):
    if(i % 2 == 0 and i % 6 == 0):
        print(i)
```

---

## **5. Factors of 10**

```python
for i in range(1, 11):
    if(10 % i == 0):
        print(i)
```

---

## **6. Count the Number of Factors of 45**

```python
cnt = 0
for i in range(1, 46):
    if(45 % i == 0):
        cnt += 1
print(cnt)
```

---

## **7. Prime Number Check**

```python
num = 14
cnt = 0
for i in range(1, num+1):
    if(num % i == 0):
        cnt += 1
if(cnt > 2):
    print(f"{num} is not a prime")
else:
    print(f"{num} is a prime")
```

---

## **8. Break Statement Example**

```python
for i in range(1, 9):
    if(i == 4):
        break
    else:
        print(i, end=" ")
```

---

## **9. Continue Statement Example**

```python
for i in range(1, 9):
    if(i == 4):
        continue
    print(i, end=" ")
```

---

## **10. While Loop Example**

```python
i = 1
while(i < 10):
    print(f'{i} Hello')
    i += 1
```
