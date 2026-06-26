"""
Matplotlib:
->This provides various plots and customisations options 
ex:
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [10,20,30,40,50,60]
plt.plot(x,y)
plt.show()
Basic Structure:
1. Axis:
2. Title:
o Line plot:
-> it is used to display data points connected by straight lines.
ex:
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [3,19,7,2,15,9]
plt.xlabel("Overs")
plt.ylabel("Score")
plt.title("Overs vs Score")
plt.plot(x,y)
plt.show()

o Bar chart:
-> displays in bars
ex:

import matplotlib.pyplot as plt
marks = [15,20,10]
students = ["Sownya","Pavani","Indrani"]
plt.ylabel("Marks")
plt.xlabel("Students")
plt.title("Student Marks")
plt.bar(students,marks,color = "brown")
plt.show()

import matplotlib.pyplot as plt
years = [2021,2022,2023,2024,2025,2026]
sales = [20000,30000,35000,16000,76000,12000]
plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Car Sales")
plt.bar(years,sales,color = "brown")
plt.show()


o pie chart:
--> parts in whole 

import matplotlib.pyplot as plt
sub = ["Python","SQL","Flask"]
stud = [20,15,20]
plt.pie(stud,labels = sub)
plt.title("Subject vs Total students")
plt.legend(stud)
plt.show()

o histogram:
ex:
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data,color = "brown",alpha = 1,edgecolor = "black")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

o scatter plot:
ex:

import matplotlib.pyplot as plt
years = [2021,2022,2023,2024,2025,2026]
sales = [20000,30000,35000,16000,76000,12000]
plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Car Sales")
plt.scatter(years,sales,color = "brown")
plt.show()
"""

import matplotlib.pyplot as plt
years = [2021,2022,2023,2024,2025,2026]
sales = [20000,30000,35000,16000,76000,12000]
plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Car Sales")
plt.bar(years,sales,color = "brown")
plt.show()

















