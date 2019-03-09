import sklearn 
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import tree
data=pd.read_csv("bank-additional-full_update.csv")
x=data.iloc[:,0:20].values
y=data.iloc[:,20].values
# print(y)

x_train= x[:40400]
y_train = y[:40400]
x_test = x[38000:]
y_test = y[38000:]	


reg=tree.DecisionTreeClassifier()
#reg=RandomForestClassifier()
plt.plot(x_train,y_train,'o')

train=reg.fit(x_train,y_train)
result=reg.predict(x_test)
plt.plot(x_test,result,'r--')

rmsc=np.sqrt(mean_squared_error(y_test,result)) # average error
print(rmsc)
print(y_test,result)
from sklearn import metrics
print(100*(metrics.accuracy_score(y_test, result)))


plt.show()
