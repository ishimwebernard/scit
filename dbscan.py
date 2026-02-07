import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt 

data = pd.read_csv('DBScanExample.csv').dropna()
db = DBSCAN(eps=1.3, min_samples=5).fit(data)
labels = db.labels_

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print("The number of clusters", n_clusters)
print("The number of noise", n_noise)
plt.scatter(data['X'], data['Y'], c=labels)
plt.show()
