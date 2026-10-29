# simple linear regression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

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

# evaluate the model

y_predict=lr.predict(X_test)
print("MAE:",mean_absolute_error(y_test,y_predict))
print("MSE:",mean_squared_error(y_test,y_predict))
print("RMSE:",np.sqrt(mean_squared_error(y_test,y_predict)))
print("R2 Score:",r2_score(y_test,y_predict))
r2=r2_score(y_test,y_predict)
#adjusted r2 score
adjusted_r2=1-(1-r2)*(40-1)/(40-1-2)
print("Adjusted R2 Score:",adjusted_r2)

# lets a random column then see the r2 and adjusted r2 score that is irrelevant to the model
new_data=data.copy()
new_data["random"]=np.random.random(200)
new_data=new_data[["cgpa","random","package"]]
print(new_data.head())
X=new_data.iloc[:,0:2]
y=new_data.iloc[:,-1]
# split the data into train data and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
#now train the data
lr=LinearRegression()
lr.fit(X_train,y_train)
y_predict=lr.predict(X_test)
print("MAE:",mean_absolute_error(y_test,y_predict))
print("MSE:",mean_squared_error(y_test,y_predict))
print("RMSE:",np.sqrt(mean_squared_error(y_test,y_predict)))
print("R2 Score:",r2_score(y_test,y_predict))
r2=r2_score(y_test,y_predict)
#adjusted r2 score
adjusted_r2=1-(1-r2)*(40-1)/(40-1-2)
print("Adjusted R2 Score:",adjusted_r2)



# lets a random column then see the r2 and adjusted r2 score that is relevant to the model
new_data1=data.copy()
new_data1["iq"]=new_data1["package"]*np.random.randint(-12,12,200)/10
new_data1=new_data1[["cgpa","iq","package"]]
print(new_data1.head())
X=new_data1.iloc[:,0:2]
y=new_data1.iloc[:,-1]
# split the data into train data and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
#now train the data
lr=LinearRegression()
lr.fit(X_train,y_train)
y_predict=lr.predict(X_test)
print("MAE:",mean_absolute_error(y_test,y_predict))
print("MSE:",mean_squared_error(y_test,y_predict))
print("RMSE:",np.sqrt(mean_squared_error(y_test,y_predict)))
print("R2 Score:",r2_score(y_test,y_predict))
r2=r2_score(y_test,y_predict)
#adjusted r2 score

adjusted_r2=1-(1-r2)*(40-1)/(40-1-2)
print("Adjusted R2 Score:",adjusted_r2)