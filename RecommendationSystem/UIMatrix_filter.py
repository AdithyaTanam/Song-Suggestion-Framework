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
dfm = pd.read_csv('UIMatrix_sc10.csv')
pdf=dfm[dfm.columns.intersection(sidlist)]

print(pdf)
pdf.to_csv('UIMatrix_selectedcolumns.csv')