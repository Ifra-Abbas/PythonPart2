from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report , confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.dummy import DummyClassifier

#collect the data
data= load_breast_cancer()
print(data.data.shape)
print(data.target.shape)

X=data.data #features
y=data.target #target labels 

#split the data 
X_train,X_test, y_train,y_test=train_test_split(
X,y,
test_size=0.2,
random_state=42,
stratify=y
)

# lets check them
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Now preprocess the training data
model=make_pipeline(
StandardScaler(),
LogisticRegression(max_iter=10000)
)
 #train the model
model.fit(X_train,y_train) # fit makes the model learns patterns also  weights and bias

# now make some prediction after learning on test data 
pred =model.predict(X_test)
print(pred)

#Now compare the actual ones with predicted
print("Predicted:",pred[:10])
print("Actual: ", y_test[:10])


# Evaluate the model
accuracy=accuracy_score(y_test,pred)
print("Accuracy:",accuracy)
print("Accuracy:",accuracy*100, "%")

#precision Recall and the Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=data.target_names))

# cross validation to test on different slips rather then one
cv_scores=cross_val_score(
model,
X_train,
y_train,
cv=5,
scoring="accuracy"
)# cv=5 divide the traing data into 5 folds means 5 splits 

print("Score:",cv_scores)# scores of 5 folds
print("Mean Accuracy:",cv_scores.mean())
print("Mean accuracy percentage:", cv_scores.mean() * 100, "%")


#lets use a different classifer to see that how the logistic regression works better or not
baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)

baseline_pred = baseline.predict(X_test)
baseline_accuracy = accuracy_score(y_test, baseline_pred)

print("Baseline accuracy:", baseline_accuracy)
print("Logistic Regression accuracy:", accuracy_score(y_test, pred))

# so the logistic has better predictions