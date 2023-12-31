import pandas as pd
import numpy as np
import quandl
import math
import datetime
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
#Preprocessing can be used to scale the data for calculation
#model_selection can used to suffle and seperate the data // Earlier used cross-validatio which was decrypted
#svm for regression 

style.use('ggplot')

df=quandl.get('WIKI/TSLA')

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100
df['PTC_Change']=(df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']*100

df=df[['Adj. Close','HL_PCT','PTC_Change','Adj. Volume']]

forcast_col='Adj. Close'
df.fillna(-9999,inplace=True) #Fillna is fill not applicable
forcast_out=int(math.ceil(0.01*len(df))) 
df['label']=df[forcast_col].shift(-forcast_out) #Shifting one percent of the day
#X = np.array(df.drop(['label'], 1))

#We define featues as X and Label as y
# Correct the line where you drop the 'label' column
X = np.array(df.drop(['label'], axis=1))
X = preprocessing.scale(X)
X_lately=X[-forcast_out:] #This is the stuff that we are going to predict against
X=X[:-forcast_out]

df.dropna(inplace=True) #dropna is used to fill missing values
y = np.array(df['label'])
y = np.array(df['label'])


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #20% of the data

clf=LinearRegression() #Classifier
clf.fit(X_train,y_train) #Fit associated with train
accuracy=clf.score(X_test,y_test) #Score associated with test
#print(accuracy)

forcast_set=clf.predict(X_lately,)
print(forcast_set,accuracy,forcast_out)
df['Forcast']=np.nan #This specifies that entire column if full of not a number data

last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400 #Second
next_unix=last_unix+one_day

for i in forcast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]

print(df.head())

df['Adj. Close'].plot()
df['Forcast'].plot()
plt.legend(loc=4) 
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
