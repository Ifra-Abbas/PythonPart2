# simple linear regression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_csv('placement.csv')
data.head()
# lets plot on the graph
plt.scatter(data['cgpa'],data['package'])
plt.xlabel("CGPA")
plt.ylabel("Package")
# plt.show()
#create model to predict the package according to the input 
X=data.iloc[:,0:1]
y=data.iloc[:,-1]
# split the data into train data and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
#now train the data
lr=LinearRegression()
lr.fit(X_train,y_train)
pr=lr.predict(X_test.iloc[0].values.reshape(1,1))
print(pr)
pr=lr.predict(X_test.iloc[1].values.reshape(1,1))
# print(pr)
pr=lr.predict(X_test.iloc[2].values.reshape(1,1))
# print(pr)
# dram best fit line
plt.scatter(data['cgpa'],data['package'])
plt.scatter(X_train,lr.predict(X_train))
plt.xlabel("CGPA")
plt.ylabel("Package")
# plt.show()

# m and b value
m=lr.coef_
b=lr.intercept_
# print(m,b)
# lets see with these

y=m*8.58+b
print(y)

