import pandas as pd
import numpy as np
df=pd.read_csv('UIMatrix_sc10.csv')
sdf=pd.read_csv('postmatriclistsc10.csv')
sdf=sdf.sort_values(by=['count'],ascending = False)
columns = eval(input("enter columns"))
sdf=sdf.head(columns)
#print(sdf)
sidlist=sdf['songid'].tolist()
print(sidlist)
df1 = pd.read_csv('UIMatrix_sc10.csv', usecols=lambda x: x in sidlist, index_col=0)
df1=df1.T
print(df1)
df1.to_csv('IUMatrix_selectedcolumns.csv')