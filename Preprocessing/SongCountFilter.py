
import pandas as pd

df = pd.read_csv('sl2.csv')
for i in(5,10,15):
    df=df[df['count'] >= i]
    print('count',i,'>=',df.shape)
    df = df[df['count'] > i]
    print('count',i,'>=',df.shape)