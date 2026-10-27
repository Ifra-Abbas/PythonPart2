from sklearn.datasets import load_diabetes
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import numpy as np

X,y=load_diabetes(return_X_y=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
reg=Ridge(alpha=0.1,solver="cholesky") # cholesky means it uses the same function that we are using
reg.fit(X_train,y_train)
y_predict=reg.predict(X_test)
r2_score(y_test,y_predict)
print(f"R2_Score:{r2_score(y_test,y_predict)}")
print(reg.coef_)
print(reg.intercept_)


class myReg:
    def __init__(self,alpha=0.1):
        self.m=None
        self.b=None
        self.alpha=alpha
    def fit(self,X_train,y_train):
        #adding column of 1 to the X_train 
        X_train = np.insert(X_train,0,1,axis=1)
        #now we have to calculate the w
        I=np.identity(X_train.shape[1])
        I[0][0]=0
        result=np.linalg.inv((np.dot(X_train.T,X_train))+(self.alpha*(I))).dot((X_train.T).dot(y_train))     
        self.m=result[1:]
        self.b=result[0]

    def predict(self,X_test):
        return X_test.dot(self.m)+self.b


#Now use the one that we create from scratch
myreg=myReg(alpha=0.1)
myreg.fit(X_train,y_train)
y_predict_scratch=myreg.predict(X_test)
print(f"R2_Score (Scratch):{r2_score(y_test,y_predict_scratch)}")
print(myreg.m)
print(myreg.b)