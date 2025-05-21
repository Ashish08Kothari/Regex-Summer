
# 📅 Day 14 - Regex Internship (Exploratory Data Analysis, Pandas, Matplotlib, Seaborn)

## 🧠 Day Overview

Today, we focused on exploring and visualizing data using **Pandas**, **Matplotlib**, and **Seaborn**. We began by understanding the foundational steps in Data Science and Exploratory Data Analysis (EDA). We practiced data preprocessing using Pandas, handled missing values, performed group-based aggregation, and finally visualized the data using various types of plots.

---

## 📊 Data Science Flow

```
Data Science Problem => Data Acquire => Data Preprocess => Data Storage => Data Preparation => Data Analysis => Data Visualization => ML/AI Algorithms => Data Report
```

We used **Pandas** and **NumPy** to acquire and clean the data, and used **Matplotlib** and **Seaborn** for visualizing insights.

---

## 📦 Pandas Practice (titanic.csv)

### 🔍 Read and Inspect Data

```python
import pandas as pd

df = pd.read_csv("titanic.csv")
df.head()
```

**Output:**
```
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
```

```python
df.shape
```

**Output:**
```
(891, 12)
```

```python
df.columns
```

**Output:**
```
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
       'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')
```

---

### 🧹 Handling Null Values

```python
df.isnull().sum()
```

**Output:**
```
Age         177
Cabin       687
Embarked      2
dtype: int64
```

```python
df = df.drop(columns = ['Cabin'])
df['Fare'] = df['Fare'].fillna(5)
df['Age'] = df['Age'].fillna(10)
df.isnull().sum()
```

**Output:**
```
Survived      0
Pclass        0
Name          0
Sex           0
Updated_Age   0
Fare          0
Embarked      0
dtype: int64
```

---

### 🔁 Type Conversion and Renaming

```python
df['Fare'] = df['Fare'].astype(int)
df = df.rename(columns={'Age': 'Updated_Age'})
df.head(2)
```

**Output:**
```
   Survived  Pclass   Name     Sex  Updated_Age  Fare Embarked
0         0       3  Name1   male           10     7        S
1         1       1  Name2 female           38    71        C
```

---

## 🔍 Exploratory Data Analysis (EDA)

### 📈 Plots with Titanic Dataset

```python
sns.countplot(x = df['Survived'])
```

**Output:** Bar chart showing 0s and 1s (not displayable in markdown).

```python
df['Survived'].value_counts().plot(kind = 'pie', autopct = '%.1f')
```

**Output:** Pie chart of survival count (not displayable in markdown).

---

## 📂 Tips Dataset Practice (tips.csv)

```python
df = pd.read_csv("tips.csv")
df.head(3)
```

**Output:**
```
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
```

```python
df.groupby('sex').sum()['tip']
```

**Output:**
```
sex
Female     157.76
Male       485.07
Name: tip, dtype: float64
```

```python
df.groupby('sex').max()['tip']
```

**Output:**
```
sex
Female     6.5
Male      10.0
Name: tip, dtype: float64
```

---

## 🛠️ Function Descriptions

- `read_csv`: Reads a CSV file into a DataFrame.
- `head`, `tail`, `sample`: View rows of data.
- `dropna`, `fillna`: Handle missing values.
- `drop`, `astype`, `rename`: Modify DataFrame structure.
- `groupby`: Group and aggregate data.
- `plot`, `countplot`, `scatterplot`, `heatmap`: Visualize data.
- `value_counts`: Bar count of unique values.
- `crosstab`: 2D summary table for two categorical variables.

---
