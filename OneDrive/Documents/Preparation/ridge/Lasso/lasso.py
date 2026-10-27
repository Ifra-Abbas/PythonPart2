import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
X,y= make_regression(n_samples=100, n_features=1, noise=20, n_informative=1, random_state=13, n_targets=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
plt.scatter(X, y)

reg=LinearRegression()
reg.fit(X_train,y_train)
print(f"Linear_Coefficient:{reg.coef_}")
print(f"Linear_intercept:{reg.intercept_}")

alpha=[0,1,5,10,30]
plt.figure(figsize=(12,6))
plt.scatter(X, y)
for i in alpha:
    L=Lasso(alpha=i)
    L.fit(X_train,y_train)
    plt.plot(X_test,L.predict(X_test),label="alpha={}".format(i))
plt.legend
plt.show()