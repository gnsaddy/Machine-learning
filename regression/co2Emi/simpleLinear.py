from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd
import pylab as pl
import numpy as np


df = pd.read_csv("co2Emi/fuelCon2018.csv")


# take a look at the dataset
df.head()

# summarize the data
df.describe()

# Lets select some features to explore more.
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2Emissions']]
cdf.head(9)

# cdf1 = df[['C']]
# cdf1.head()

viz = cdf[['CYLINDERS', 'ENGINESIZE', 'FUELCONSUMPTION_COMB', 'CO2Emissions']]
viz.hist()
plt.show()


# Now, lets plot each of these features vs the Emission, to see how linear is their relation:
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2Emissions,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()


plt.scatter(cdf.ENGINESIZE, cdf.CO2Emissions,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

plt.scatter(train.ENGINESIZE, train.CO2Emissions,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2Emissions']])
regr.fit(train_x, train_y)
# The coefficients
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)


# Asmentionedbefore, Coefficient and Intercept in thesimplelinearregression, aretheparametersofthefitline.
# Giventhatit is asimplelinearregression, with only2parameters, and knowingthattheparameters
# aretheintercept and slopeoftheline, sklearncanestimatethemdirectly from ourdata.
#  Notice that all of the data must be available to traverse and calculate the parameters.


plt.scatter(train.ENGINESIZE, train.CO2Emissions,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2Emissions']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_, test_y))
