from stock1 import stock
import typedef
import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import sklearn.neighbors.typedefs 
import sklearn.neighbors.quad_tree 
import sklearn.tree._utils
company_ticker = input("Company Ticker:")
no_of_days = int(input("Enter the number of days:"))
data = stock(company_ticker)
#print(data)
data = data[['open','high','low','close']]
#print(data)
data['label'] = data['close'].shift(+no_of_days)
#print(data)
#'X' is set of features and 'y' represents labels
X = np.array(data.drop(['close','label'],axis = 1))
#print(X)
#print(X,X.shape)
X_lately = X[:no_of_days]
X = X[no_of_days:]

y = np.array(data['label'])
y = y[no_of_days:]
#print(y,y.shape)
X_train, X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2)
clf = LinearRegression()
#print(X_train.shape,X_test.shape)
#print(y_train.shape,y_test.shape)
clf.fit(X_train,y_train)
confidence = clf.score(X_test,y_test)
print('Confidence:',confidence)
forecast_set = clf.predict(X_lately)
print(forecast_set)

