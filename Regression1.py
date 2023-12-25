import pandas as py
import quandl

df=quandl.get('WIKI/TSLA')
# print(df.head())

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
print(df)
