import pandas as pd
import numpy as np
df=pd.read_csv('songtimelist.csv')
fq=pd.DataFrame()
sq=pd.DataFrame()
tq=pd.DataFrame()
ftq=pd.DataFrame()
#for i in range (df.shape[0]):
#   int(df.iloc[i][5])
df[['hours']] = df[['hours']].apply(pd.to_numeric)
df = df.sort_values(['hours'],ascending=True)
print(df)
df.to_csv('hoursorted.csv')
fq=df[df['hours']<7]
sq=df[(df['hours']<13) & (df['hours']>6) ]
tq=df[(df['hours']<19) & (df['hours']>12) ]
ftq=df[(df['hours']<24) & (df['hours']>18) ]
fq.to_csv('FirstQuarter.csv')
sq.to_csv('SecondQuarter.csv')
tq.to_csv('ThirdQuarter.csv')
ftq.to_csv('FourthQuarter.csv')
print(ftq)
