# Lets train the model hurry
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class MyLR:
    def __init__(self):
        self.m=None
        self.b=None
    # function to train the model
    def fit(self,X_train,y_train):
       num=0
       den=0
       for i in range(X_train.shape[0]): # loop will run 160 times
          num=num + ((X_train[i]-X_train.mean())*(y_train[i]-y_train.mean()))
          den=den + ((X_train[i]-X_train.mean())*(X_train[i]-X_train.mean()))
       self.m=num/den
       self.b=y_train.mean()-(self.m * X_train.mean())
       print(self.m)
       print(self.b)

    # prediction function
    def predict(self,X_test):
      #mx+b
      return self.m * X_test+self.b

# data fetching 
data=pd.read_csv("placement.csv")
data.head()
X=data.iloc[:,0].values
y=data.iloc[:,1].values
X_train,X_test,y_train,y_test=train_test_split(
X,y,
test_size=0.2,
random_state=2
)
# print(X_train.shape)
# lets create an object of class MyLr
lr=MyLR()
lr.fit(X_train,y_train) 
# same m and b as the scikit learn bcz scikit learn use the same formula 
# now predict using the function we created

print(lr.predict(X_test[0])) #same as we predict using the predefined one

# conclusion that this one works for only simple linear regression
# but the scikit one works for multiple one as well









