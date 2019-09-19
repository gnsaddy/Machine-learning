# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:07:23 2019

@author: Aditya Raj
"""

import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"]) #indications
plt.show()


sample_data = pd.read_csv('sample_data.csv')
sample_data

type(sample_data)

sample_data.column_c.iloc[0]  # fetching 3rd column 0 index element
sample_data.column_c.iloc[2]  # fetching 3rd column 2 index element
sample_data.column_b.iloc[2]  # fetching 2nd column 2 index element
sample_data.column_c   # fetching 3rd column all element
sample_data.iloc[:,:].values



plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()


print("Loading countries data set")

data = pd.read_csv('countries.csv')
data
allD =data.iloc[:,:].values


# Compare the population growth in the US and China

data[data.country == 'United States'] # fetching data of US
us = data[data.country == 'United States']
us
china = data[data.country == 'China']
china

# note- number's are so big to show in graph 
plt.plot(us.year,us.population)
# so divide population by 10 to power 6 i.e 1 million
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# percentage growth of population pe year
us.population
us.population / us.population.iloc[0] * 100


plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.show()

