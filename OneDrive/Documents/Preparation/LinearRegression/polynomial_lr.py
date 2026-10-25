import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline

# generate the data that we will use later

X=6*np.random.rand(200,1)-3
y=0.8 * X**2 +0.9*X+2+np.random.randn(200,1) #degree 2 polynomial + some random noise

# whats our need that we have to find the coefficients and the intercept okay

plt.plot(X,y,"b.")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()

# first we will use the normal one linear regession

# split the data
X_train,X_test,y_train,y_test=train_test_split(
X,y,
test_size=0.2,
random_state=2
)
# train the model

lr=LinearRegression()
lr.fit(X_train,y_train)

# now predict
y_predict=lr.predict(X_test)
r2=r2_score(y_test,y_predict)

print(r2)

plt.plot(X_train,lr.predict(X_train),color="r")
plt.plot(X,y,"b.")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()

# now we will apply polynomial first we will transform our features than train them
poly=PolynomialFeatures(degree=2) # we will have 3 columns x0,,x1,x2

X_train_trans=poly.fit_transform(X_train)
X_test_trans=poly.fit_transform(X_test)

# now see the original and transform one

print(X_train[0])
print(X_train_trans[0])

# now train the transformed features

tlr=LinearRegression()
tlr.fit(X_train_trans,y_train)

# predict 

y_predict=tlr.predict(X_test_trans)
r2_s=r2_score(y_test,y_predict)
print("here is the r2",r2_s)

# here are the coefficients
print(tlr.coef_)
print(tlr.intercept_)


# lets see on the graph
X_new=np.linspace(-3, 3, 200).reshape(200, 1)
X_new_poly = poly.transform(X_new)
y_new = tlr.predict(X_new_poly)

plt.plot(X_new, y_new, "r-", linewidth=2, label="Predictions")
plt.plot(X_train, y_train, "b.",label='Training points')
plt.plot(X_test, y_test, "g.",label='Testing points')
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# if the no. of degrees is increasing then the it go towards the overfitting (memorzing training ones like )
# we have the model to be generalized model not the memorized


