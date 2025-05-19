# Assignments

## Q1. Count how many movies and TV shows are present in this dataset

```python
import pandas as pd

df = pd.read_csv("data.csv")
q1_counts = df['type'].value_counts()
print(q1_counts)
```

**Answer:**
```
movie    16462
tv        5325
```

---

## Q2. Count how many movies are releasing each year

```python
df_movies = df[df['type'] == 'movie']
q2_movies_per_year = df_movies['releaseYear'].dropna().astype(int).value_counts().sort_index()
print(q2_movies_per_year)
```

**Answer:**
```
1913       1
1917       1
1918       1
1919       2
1920       2
1921       1
1923       2
1926       1
1928       3
1929       5
1930       1
1931       2
1932       4
1933       2
1934       5
1935       5
1936       5
1937       8
1938       5
1939       7
1940       4
1941       2
1942       7
1943      11
1944       2
1945       9
1946      11
1947      13
1948      13
1949      12
1950      20
1951      20
1952      26
1953      26
1954      29
1955      17
1956      30
1957      28
1958      32
1959      28
1960      22
1961      32
1962      21
1963      32
1964      21
1965      22
1966      29
1967      20
1968      25
1969      21
1970      33
1971      34
1972      28
1973      42
1974      30
1975      28
1976      36
1977      32
1978      21
1979      31
1980      35
1981      40
1982      35
1983      48
1984      54
1985      42
1986      49
1987      53
1988      51
1989      52
1990      51
1991      66
1992      54
1993      66
1994      69
1995      75
1996      67
1997      94
1998      86
1999     103
2000     125
2001     150
2002     161
2003     195
2004     213
2005     226
2006     253
2007     249
2008     263
2009     295
2010     313
2011     347
2012     368
2013     470
2014     531
2015     641
2016     731
2017     879
2018    1081
2019    1074
2020     925
2021    1052
2022    1367
2023    1296
2024     956
2025     146
```

---

## Q3. From Sep to Oct how many action movies are released

*The dataset does not contain month-level release date information, so this cannot be determined from the given data.*

---

## Q4. Find out the number of movies and TV shows released each year

```python
df_year_type = df.dropna(subset=['releaseYear'])
df_year_type['releaseYear'] = df_year_type['releaseYear'].astype(int)
q4_year_type_counts = df_year_type.groupby(['releaseYear', 'type']).size().unstack(fill_value=0)
print(q4_year_type_counts)
```

**Answer:**
```
type         movie   tv
releaseYear            
1913             1    0
1917             1    0
1918             1    0
1919             2    0
1920             2    0
1921             1    0
1923             2    0
1926             1    0
1928             3    0
1929             5    0
1930             1    0
1931             2    0
1932             4    0
1933             2    0
1934             5    0
1935             5    0
1936             5    0
1937             8    0
1938             5    0
1939             7    0
1940             4    0
1941             2    0
1942             7    0
1943            11    0
1944             2    0
1945             9    0
1946            11    0
1947            13    0
1948            13    0
1949            12    0
1950            20    0
1951            20    0
1952            26    0
1953            26    0
1954            29    0
1955            17    0
1956            30    0
1957            28    0
1958            32    0
1959            28    0
1960            22    0
1961            32    0
1962            21    0
1963            32    0
1964            21    0
1965            22    0
1966            29    2
1967            20    0
1968            25    1
1969            21    1
1970            33    0
1971            34    2
1972            28    0
1973            42    1
1974            30    0
1975            28    1
1976            36    0
1977            32    0
1978            21    0
1979            31    4
1980            35    2
1981            40    3
1982            35    2
1983            48    3
1984            54    4
1985            42    1
1986            49    2
1987            53    8
1988            51    3
1989            52    3
1990            51    4
1991            66    7
1992            54    9
1993            66    7
1994            69    4
1995            75    7
1996            67    7
1997            94    8
1998            86   15
1999           103   14
2000           125   12
2001           150   23
2002           161   18
2003           195   25
2004           213   29
2005           226   38
2006           253   30
2007           249   41
2008           263   40
2009           295   44
2010           313   48
2011           347   63
2012           368   69
2013           470   71
2014           531  110
2015           641  133
2016           731  199
2017           879  272
2018          1081  379
2019          1074  417
2020           925  465
2021          1052  546
2022          1367  678
2023          1296  632
2024           956  593
2025           146  187
```
