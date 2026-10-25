import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# using Build in
X,y=load_diabetes(return_X_y=True)
print(X.shape)
print(y.shape)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
print(X_train.shape,X_test.shape)
# making an object of the class
mlr=LinearRegression()
# train the model
mlr.fit(X_train,y_train)
#now prediction
y_pred=mlr.predict(X_test)
print("Here is the predicted data: ",y_pred)
# beta values 10 input values so 10 betas
beta=mlr.coef_
print(beta)
# y intercept
y_intercept=mlr.intercept_
print(y_intercept)
