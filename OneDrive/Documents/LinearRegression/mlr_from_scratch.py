import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# From scratch
X,y=load_diabetes(return_X_y=True)
print(X.shape)
print(y.shape)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
print(X_train,y_train)

class myMLR:
    def __init__(self):
        self.coef_=None
        self.intercept_=None

    def fit(self,X_train,y_train):
        # we have to add 1 column in the X for beta not for that we will use function insert from numpy
        X_train=np.insert(X_train,0,1,axis=1)
        # calculate the coefficients
        betas=np.linalg.inv(np.dot(X_train.T,X_train)).dot(X_train.T).dot(y_train)
        self.intercept_=betas[0]
        self.coef_=betas[1:]
        print(betas)
        print(self.intercept_)
    def predict(self,X_test):
        y_pred=np.dot(X_test,self.coef_)+self.intercept_
        print(y_pred)

# creating object of the class
mlr=myMLR()
mlr.fit(X_train,y_train)
y_predict=mlr.predict(X_test)
betas=mlr.coef_
print(betas)
intercept=mlr.intercept_
print(intercept)

# exactly same as the build in
#its a general works for higher and lower bith dimensions ---( dimension means the number of input features)