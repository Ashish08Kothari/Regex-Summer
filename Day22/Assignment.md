
# PySpark RDD Assignment

This assignment is based on PySpark and demonstrates how to work with Resilient Distributed Datasets (RDDs). Below are the questions and their solutions using RDD transformations and actions.

---

## Question 1

**Get the temperature for Jaipur city where the category is 'Max'.**

```python
rdd.filter(lambda x: x.split(',')[0] == 'Jaipur' and x.split(',')[1] == 'Max')     .map(lambda x: (x.split(',')[0], x.split(',')[2]))     .collect()
```

### Explanation:
- Filters the dataset where the first element (city) is "Jaipur" and the second element (category) is "Max".
- Maps the filtered records to a tuple of (city, temperature).
- Collects the result.

---

## Question 2

**Calculate the average temperature of each city for the category 'Max'.**

```python
# Step 1: Filter only "Max" category rows
max_rdd = rdd.filter(lambda x: x.split(',')[1] == 'Max')
```

```python
# Step 2: Map to (city, (temperature, 1)) for aggregation
city_temp_pair = max_rdd.map(lambda x: (x.split(',')[0], (float(x.split(',')[2]), 1)))
```

```python
# Step 3: Reduce by key to sum temperatures and counts
city_temp_sum_count = city_temp_pair.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
```

```python
# Step 4: Compute average temperature
city_avg_temp = city_temp_sum_count.mapValues(lambda x: x[0] / x[1])
```

```python
# Step 5: Collect results
result = city_avg_temp.collect()
result
```

### Explanation:
1. **Filter** only those records where category is "Max".
2. **Map** each record to a pair (city, (temperature, 1)).
3. **ReduceByKey** to sum up the temperatures and counts for each city.
4. **MapValues** to compute the average temperature.
5. **Collect** the results to view them.

---

These steps demonstrate filtering, mapping, reducing, and computing averages using RDDs.
