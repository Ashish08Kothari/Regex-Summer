
# **Day 7 - Regex Software Services Internship**

**Overview:**

Today was my Day 7 at Regex Software Services as a Data Engineering Intern. I practiced the `while` loop in Python and learned about Python Lists and their in-built functions. I also wrote several programs using lists including palindrome checks, maximum value detection, cumulative sums, and pair sums. Below are the scripts and snippets I worked on.

---

## **Finding LCM using While Loop**

```python
a = 5
b = 10
c = max(3, 7)
while True:
    if c % a == 0 and c % b == 0:
        break
    else:
        c += 1
print(c)
```

## **Palindrome Check using String Slicing**

```python
s = "SARAS"
z = s[::-1]
if s == z:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

## **Palindrome Check using While Loop**

```python
s = "SARAS"
start = 0
end = len(s) - 1

while start <= end:
    if s[start] != s[end]:
        break
    else:
        start += 1
        end -= 1

if start > end:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

## **Basic List Operations**

```python
a = [1, 20, 30, 'abc']
print(a[1])

a[0] = 'Tiger'
print(a)

a.append('Ashish')
print(a)

a.insert(1, 10000)
print(a)

a.pop()
print(a)

a.pop(1)
print(a)

a.remove(1)
print(a)

a.clear()
print(a)
```

## **Print Even Numbers from List**

```python
a = [1, 20, 30, 51]
size = len(a)
for i in range(0, size):
    if a[i] % 2 == 0:
        print(f"{a[i]} is a even number")
```

## **Find Maximum Number in List**

```python
a = [1, 20, 30, 51, 100, 345]
max = a[0]
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
print(f"Maximum number is {max}")
```

## **Cumulative Sum in List**

```python
a = [10, 20, 30, 51, 43]
ans = []
total = 0
for i in a:
    total += i
    ans.append(total)
print(ans)
```

## **Find Pairs with Target Sum**

```python
a = [-1, 0, 2, 5, 7, 11, 14]
target = 9
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])
```

## **Nested Loops Example**

```python
for i in range(1, 4):
    print(".....Student", i)
    for j in range(1, i + 1):
        print("Good Morning", j)
```

