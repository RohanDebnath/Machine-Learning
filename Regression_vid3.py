import pandas as py
import quandl
import math

df=quandl.get('WIKI/TSLA')
# print(df.head())

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100
df['PTC_Change']=(df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']*100

df=df[['Adj. Close','HL_PCT','PTC_Change','Adj. Volume']]

forcast_col='Adj. Close'
df.fillna(-9999,inplace=True) #Fillna is fill not applicable
forcast_out=int(math.ceil(0.01*len(df)))

df['label']=df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True) #dropna is used to fill missing values
print(df.head())

