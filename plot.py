import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

data = pd.read_csv('FungusLocations.csv').dropna()

kmeans = KMeans(n_clusters=3, n_init='auto')
kmeans.fit(data)

silhouette_avg = silhouette_score(data, kmeans.labels_)
print('Silhouette score', round(silhouette_avg, 2))

plt.scatter(data['East'], data['North'], c=kmeans.labels_, cmap='viridis')
plt.xlabel('East')
plt.ylabel('North')
plt.title('KMeans Clustering Results')
plt.show()
