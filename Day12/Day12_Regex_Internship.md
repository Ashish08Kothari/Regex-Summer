# **Day 12 - Regex Software Services Internship**

## **Overview**

On the twelfth day of my internship, I was introduced to Data Science and the Python libraries NumPy and Pandas, which are essential for data manipulation and analysis. I learned the typical flow of a Data Science problem which includes data acquisition, preprocessing, storage, preparation, analysis, visualization, machine learning, and reporting. NumPy, a scientific computing library, was used to handle numerical data efficiently, primarily in the form of n-dimensional arrays. Pandas, another powerful library, was used to work with labeled data through Series and DataFrame objects. Throughout the session, I practiced a variety of operations and functions from both libraries to understand their capabilities in data handling.

---

### Importing NumPy and checking type
```python
import numpy
type(numpy.arange(4))
```
**Explanation**: `numpy.arange()` returns an array with regularly spaced values within a given interval.

### Creating NumPy array using alias 'np'
```python
import numpy as np
arr1 = np.arange(5)
arr1
```
**Explanation**: `np.arange()` creates an array of integers from 0 up to (but not including) the given number.

### Creating a raw ndarray with shape
```python
import numpy as np
np.ndarray(3)
```
**Explanation**: `np.ndarray()` creates an uninitialized ndarray object of the specified shape.

### Checking size of 1D array
```python
arr1 = np.array([1,2,3])
arr1.size
```
**Explanation**: `.size` returns the total number of elements in the array.

### Checking size and shape of 2D array
```python
arr1 = np.array([[1,2],[2,3],[5,6]])
arr1.size
arr1.shape
```
**Explanation**: `.shape` returns the array's dimensions; `.size` gives total number of elements.

### Shape of 1D array
```python
arr2 = np.arange(3)
print(arr2.shape)
```
**Explanation**: `.shape` for 1D array returns a single integer tuple.

### Data type of array elements
```python
arr1 = np.array([[1,2],[2,3],[5,6]])
arr1.dtype
```
**Explanation**: `.dtype` gives the data type of array elements.

### Data type with float values
```python
arr1 = np.array([[1.0,2],[2,3],[5,6]])
arr1.dtype
```
**Explanation**: If any value is float, NumPy promotes entire array to `float`.

### Creating array of ones
```python
np.ones([3,4])
```
**Explanation**: `np.ones()` creates a matrix filled with ones.

### Creating array of zeros
```python
np.zeros([3,4])
```
**Explanation**: `np.zeros()` creates a matrix filled with zeros.

### Getting number of dimensions
```python
arr = np.ones([3,4])
arr.ndim
```
**Explanation**: `.ndim` returns number of array dimensions.

### Reshaping 1D to 2D
```python
arr = np.arange(9)
arr.reshape(3,3)
```
**Explanation**: `.reshape()` changes the shape of an array without changing its data.

### Transpose of 2D array
```python
a = np.array([[1,2],[3,4]])
print(a)
b = a.transpose()
print(b)
```
**Explanation**: `.transpose()` swaps rows with columns.

### 3D array shape and transpose
```python
a = np.array([[[1,2],[3,4],[5,6]]])
print(a.ndim)
print(a.shape)
print(a)
print(a.transpose())
```
**Explanation**: 3D arrays support transposing dimensions similarly.

### Creating basic Pandas Series
```python
import pandas
series1 = pandas.Series([10,2,34,4])
series1
```
**Explanation**: `pd.Series()` creates a labeled one-dimensional array.

### Accessing Series element by index
```python
print(series1[0])
```
**Explanation**: Series elements can be accessed by index like a list.

### Modifying Series element
```python
series1[0] = 90
series1
```
**Explanation**: Series values can be updated by index.

### Finding maximum value in Series
```python
series1.max()
```
**Explanation**: `.max()` returns the largest element in the Series.

### Finding index of minimum value
```python
print(series1.idxmin())
```
**Explanation**: `.idxmin()` returns index of the smallest value.

### Creating Series with custom index
```python
series1 = pandas.Series([10,2,34,4],index=['A','B','C','D'])
series1
```
**Explanation**: You can define custom indices for Series.

### Converting Series to dictionary
```python
series1.to_dict()
```
**Explanation**: `.to_dict()` converts Series to a Python dictionary.

### Creating Series from NumPy array
```python
arr1 = np.array([10,13,15,19,24])
series1 = pd.Series(arr1)
series1
```
**Explanation**: Pandas Series can be constructed from NumPy arrays.

### Counting unique values
```python
series1.value_counts()
```
**Explanation**: `.value_counts()` returns counts of unique values.

### Value counts in ascending order
```python
series1.value_counts(ascending=True)
```
**Explanation**: Set `ascending=True` to sort counts in increasing order.

### Check if values are unique
```python
series1.is_unique
```
**Explanation**: `is_unique` checks if all values are unique.

### Number of unique values
```python
series1.nunique()
```
**Explanation**: `nunique()` returns count of unique values.

### Sorting Series values
```python
series1.sort_values(ascending=False)
```
**Explanation**: `sort_values()` sorts values in descending order.

### Dropping duplicate values
```python
series1.drop_duplicates()
```
**Explanation**: `drop_duplicates()` removes duplicate values from Series.

### Drop duplicates with inplace
```python
series1.drop_duplicates(inplace=True)
series1
```
**Explanation**: Using `inplace=True` modifies Series directly.

### Creating Series from dictionary and multiple operations
```python
series1 = pd.Series(mydict)
print(series1.is_unique)
print(series1.nunique())
print(series1.value_counts())
print(series1.drop_duplicates())
print(series1.sort_values(ascending=False))
print(series1.drop_duplicates(inplace=True))
series1
```
**Explanation**: Combines several Series operations on dictionary-based data.

### Creating a DataFrame
```python
data = [[10,12,13], [13,14,15]]
pd.DataFrame(data)
```
**Explanation**: `.DataFrame()` creates 2D tabular structure from list.

### DataFrame with custom column names
```python
df = pd.DataFrame(data, columns=['Product 1','Product 2','Product 3'])
print(type(df))
print(type(df['Product 1']))
```
**Explanation**: You can access column type and individual columns as Series.

### Reading a CSV file
```python
pd.read_csv('movies.csv')
```
**Explanation**: `read_csv()` loads data from a CSV file into a DataFrame.

### Analyzing ratings from CSV
```python
df = pd.read_csv('ratings.csv')
print(df['rating'].value_counts().head(3))
print(df['rating'].nunique())
print(df['rating'].drop_duplicates())
print(df)
df['userId'] = df['userId'].astype(float)
print(df)
```
**Explanation**: Demonstrates CSV reading, column analysis, type conversion.

