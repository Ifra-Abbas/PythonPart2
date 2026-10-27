import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
X,y= make_regression(n_samples=100, n_features=1, noise=20, n_informative=1, random_state=13, n_targets=1)
plt.scatter(X, y)

# first apply linear regression
lr=LinearRegression()
lr.fit(X,y)
# now we will se the coeffiecints and the intercept
m_lr=lr.coef_
b_lr=lr.intercept_

print(f"Linear_Coefficient:{m_lr}")
print(f"Linear_intercept:{b_lr}")

# now well apply the ridge okay
# for value of alpha 10
rg1=Ridge(alpha=10) # alpha is the hyper parameter okay the lamda
rg1.fit(X,y)
# now we will se the coeffiecints and the intercept
mr=rg1.coef_
br=rg1.intercept_

print(f"Ridge_Coefficient:{mr}")
print(f"Ridge_intercept:{br}")

# for value of alpha 100

rg2=Ridge(alpha=100) # alpha is the hyper parameter okay the lamda
rg2.fit(X,y)
# now we will se the coeffiecints and the intercept
mr=rg2.coef_
br=rg2.intercept_

print(f"Ridge_Coefficient:{mr}")
print(f"Ridge_intercept:{br}")


# Now plot these three to see the difference

plt.plot(X,y,"b.")
plt.plot(X,lr.predict(X),color="red",label="alpha=0")
plt.plot(X,rg1.predict(X),color="green",label="alpha=10")
plt.plot(X,rg2.predict(X),color="orange",label="alpha=100")
plt.legend()
# plt.show()



#Now we will create from scratch

class MyRidge:
    
    def __init__(self,alpha=0.1):
        self.m=None
        self.b=None
        self.alpha=alpha
    def fit(self,X_train,y_train):

        num=0
        den=0
        for i in range(X_train.shape[0]):
            num=num+((y_train[i]-y_train.mean())*(X_train[i]-X_train.mean()))
            den=den+((X_train[i]-X_train.mean())*(X_train[i]-X_train.mean()))

        den=den+self.alpha
        self.m=num/den
        self.b=(y_train.mean()-(self.m*X_train.mean()))
        print(self.m,self.b)

    def prdict(X_test):
        pass

reg=MyRidge(alpha=10)
reg.fit(X,y)

reg=MyRidge(alpha=100)
reg.fit(X,y)



    


