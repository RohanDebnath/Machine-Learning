import pandas as pd
import numpy as np
import quandl
import math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
#Preprocessing can be used to scale the data for calculation
#model_selection can used to suffle and seperate the data // Earlier used cross-validatio which was decrypted
#svm for regression 


df=quandl.get('WIKI/TSLA')

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100
df['PTC_Change']=(df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']*100

df=df[['Adj. Close','HL_PCT','PTC_Change','Adj. Volume']]

forcast_col='Adj. Close'
df.fillna(-9999,inplace=True) #Fillna is fill not applicable
forcast_out=int(math.ceil(0.01*len(df))) 
print(forcast_out) #days in advanced 
df['label']=df[forcast_col].shift(-forcast_out) #Shifting one percent of the day
df.dropna(inplace=True) #dropna is used to fill missing values

#We define featues as X and Label as y

#X = np.array(df.drop(['label'], 1))
# Correct the line where you drop the 'label' column
X = np.array(df.drop(['label'], axis=1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])

print(len(X),len(y))

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #20% of the data

clf=LinearRegression() #Classifier
clf.fit(X_train,y_train) #Fit associated with train
accuracy=clf.score(X_test,y_test) #Score associated with test
print(accuracy)
