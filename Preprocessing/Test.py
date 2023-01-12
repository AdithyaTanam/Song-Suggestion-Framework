import pandas as pd
import sklearn
import numpy  as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
dataset=pd.read_csv('UIMatrix2.csv')
df = pd.DataFrame(dataset)
#df.drop('user')
#print(df)
#mat = dataset.as_matrix()
#print(mat)
# Using sklearn
km = sklearn.cluster.KMeans(n_clusters=5)
km.fit(df)

# Get cluster assignment labels
labels = km.predict(df)
print(labels)
# Format results as a DataFrame
results = pd.DataFrame([dataset.index,labels]).T
#print(results)

# Set the size of the plot
'''plt.figure(figsize=(100,100))

# Create a colormap
colormap = np.array(['red', 'lime', 'black','blue','pink'])

plt.subplot(5,100,500)
plt.scatter(5,100,c = colormap[km.labels_])
plt.title('K Mean Classification')
plt.show()'''
