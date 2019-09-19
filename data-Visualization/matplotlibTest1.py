# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:06:55 2019

@author: Aditya Raj
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sklearn.datasets as dt

#iris = dt.load_iris()
#print(iris)
data=pd.read_csv('Iris.csv')
print(data.head(10))
data.describe()
data.info() 

#histogram
#1: Histogram for Sepal Length
plt.figure(figsize = (10, 7)) 
x = data["SepalLengthCm"] 
plt.hist(x, bins = 30, color = "green") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count") 

#2: Histogram for Sepal Width
plt.figure(figsize = (10, 7)) 
x = data.SepalWidthCm 

plt.hist(x, bins = 30, color = "green") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count") 

plt.show() 

#3: Histogram for Petal Length
plt.figure(figsize = (10, 7)) 
x = data.PetalLengthCm 

plt.hist(x, bins = 20, color = "green") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count") 

plt.show() 

#4: Histogram for Petal Width
plt.figure(figsize = (10, 7)) 
x = data.PetalWidthCm 

plt.hist(x, bins = 20, color = "green") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_Width_cm") 
plt.ylabel("Count") 

plt.show() 


#5: Data preparation for Box Plot
# removing Id column 
new_data = data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] 
print(new_data.head()) 

plt.figure(figsize = (10, 7)) 
new_data.boxplot() 

# other details
dataset=data
#findout unique classification/type of iris flower.
data['Species'].unique()

#findout no of rows for each Species.
print(data.groupby('Species').size())

#Create 3 DataFrame for each Species
setosa=dataset[dataset['Species']=='Iris-setosa']
versicolor =dataset[dataset['Species']=='Iris-versicolor']
virginica =dataset[dataset['Species']=='Iris-virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

print(dataset.describe())
#count tells that all the 4 features have 150 rows
#in general ,From Mean we can say that sepal is larger than petal.

#Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width
#warnings.simplefilter("ignore")#Supress any warning
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
dataset.plot(x="SepalLengthCm",y="SepalWidthCm",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
dataset.plot(x="PetalLengthCm",y="PetalWidthCm",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
# plt.close()
# we can see that  there are some petals which are smaller than rest of petal.

#for each Species ,let's check what is petal and sepal distibutuon
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

setosa.plot(x="SepalLengthCm", y="SepalWidthCm", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="SepalLengthCm",y="SepalWidthCm",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="SepalLengthCm", y="SepalWidthCm", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="PetalLengthCm", y="PetalWidthCm", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="PetalLengthCm",y="PetalWidthCm",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="PetalLengthCm", y="PetalWidthCm", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
# plt.show()
# plt.close()

#satosa   - satosa Petal are relatively smaller than rest of species .can be easily separable from rest of Species 
#versicolor & virginica are also separable in Petal comprasion
#satoa sepal are smallest in length and largest in Width than other species


###############################Histogram# Plot all feature for all species###########################################################################
plt.figure()

fig,ax=plt.subplots(4,3,figsize=(17, 8))
setosa["SepalLengthCm"].plot(kind="hist", ax=ax[0][0],label="setosa",color ='r',fontsize=10)
versicolor["SepalLengthCm"].plot(kind="hist", ax=ax[0][1],label="versicolor",color='b',fontsize=10)
virginica["SepalLengthCm"].plot( kind="hist",ax=ax[0][2],label="virginica",color='g',fontsize=10)

setosa["SepalWidthCm"].plot(kind="hist", ax=ax[1][0],label="setosa",color ='r',fontsize=10)
versicolor["SepalWidthCm"].plot(kind="hist", ax=ax[1][1],label="versicolor",color='b',fontsize=10)
virginica["SepalWidthCm"].plot( kind="hist",ax=ax[1][2],label="virginica",color='g',fontsize=10)

setosa["PetalLengthCm"].plot(kind="hist", ax=ax[2][0],label="setosa",color ='r',fontsize=10)
versicolor["PetalLengthCm"].plot(kind="hist", ax=ax[2][1],label="versicolor",color='b',fontsize=10)
virginica["PetalLengthCm"].plot( kind="hist",ax=ax[2][2],label="virginica",color='g',fontsize=10)


setosa["PetalWidthCm"].plot(kind="hist", ax=ax[3][0],label="setosa",color ='r',fontsize=10)
versicolor["PetalWidthCm"].plot(kind="hist", ax=ax[3][1],label="versicolor",color='b',fontsize=10)
virginica["PetalWidthCm"].plot( kind="hist",ax=ax[3][2],label="virginica",color='g',fontsize=10)

plt.rcParams.update({'font.size': 10})
plt.tight_layout()

ax[0][0].set(title='SepalLengthCm')
ax[0][1].set(title='SepalLengthCm')
ax[0][2].set(title='SepalLengthCm')
ax[1][0].set(title='SepalWidthCm ')
ax[1][1].set(title='SepalWidthCm ')
ax[1][2].set(title='SepalWidthCm ')
ax[2][0].set(title='PetalLengthCm')
ax[2][1].set(title='PetalLengthCm ')
ax[2][2].set(title='PetalLengthCm')
ax[3][0].set(title='PetalWidthCm')
ax[3][1].set(title='PetalWidthCm')
ax[3][2].set(title='PetalWidthCm')

ax[0][0].legend()
ax[0][1].legend()
ax[0][2].legend()
ax[1][0].legend()
ax[1][1].legend()
ax[1][2].legend()
ax[2][0].legend()
ax[2][1].legend()
ax[2][2].legend()
ax[3][0].legend()
ax[3][1].legend()
ax[3][2].legend()


plt.show()
plt.close()



