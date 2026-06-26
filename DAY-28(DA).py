"""
#deep copy doesnt affect original array
#shallow copy affects the original array
#shallow copy
import numpy as np
a = np.array([10,20,30])
a_view = a.view()
a_view[0] = 40
print(a_view)
print(a)
#deep copy
a_copy = a.copy()
a_copy[0]=50
print(a_copy)
print(a)

Data Analysis

-->Data Analysis is the process of inspecting ,cleaning,transforming,modeling data to
   discover useful insights,support decision making.

Types:
- Descriptive Analysis -> Summarizing Data
- Diagnostic Analysis -> Understanding Causes such as sales drop
- Predictive Analysis -> Forecasting future outcomes
- Prescriptive Analysis -> Suggesting actions based on the data(Marketing)

Libraries:
o numpy:
-> provides support for multi dimensional arrays
-> ndaraay
-->Creating numpy arrays:
ex:
import numpy as np
a = np.array([1,2,3])
print(a) -->> 1-d array

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a) -->>2-d array

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a) -->> 3-d array

import numpy as np
a = np.arange(1,10)
print(a) --> generate a range of numbers between the given range

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
r = a.reshape(3,2)
print(r)

o pandas:
-> pandas is a powerful data manipulation and analysis library,built on top
of numpy
-> it provides data structures like series and dataframes for efficient
data handling

methods:
.mean()
.sum()
.max()
.min()
.head()
.tail()

o matplotlib

import pandas as pd
p = pd.Series([67,90,45,20],index=["apple","banana","curd","dal"])
print(p)

"""
import math
print(f"square: {math.sqrt(25)}")
    


















