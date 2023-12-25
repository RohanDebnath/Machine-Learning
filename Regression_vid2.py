import pandas as py
import quandl

df=quandl.get('WIKI/TSLA')
# print(df.head())

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100

df=df[['Adj. Close','HL_PCT']]
print(df.head())
