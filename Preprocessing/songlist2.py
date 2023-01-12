import csv
import pandas as pd
useridlist = []
songnamelist = []
songindex=[]
sid=0
'''change the below range from 6 to the number of last file+1'''


'''it is necessary all the split files are in encoding-utf-8,normally fies exist
in this format but once google how to convert csv files to encoding utf-8 '''
for i in range (1,6):
        if i==4 or i==5:
            with open('p%d.csv'%i, mode='r') as infile:
                    reader = csv.reader(infile)
                    for rows in reader:
                        useridlist.append(rows[0])
                        songnamelist.append(rows[5])
        else :
            with open('p%d.csv' % i, mode='r',encoding='utf-8') as infile:
                reader = csv.reader(infile)
                for rows in reader:
                    useridlist.append(rows[0])
                    songnamelist.append(rows[5])
print(i)
d=pd.DataFrame()
d['userid'] = useridlist
d['songname'] = songnamelist
print(d)
d=d.drop_duplicates(keep='first')
print(d)
print(d.groupby(['songname']).size().reset_index(name='count'))
print(d)
d.to_csv('s12.csv')
