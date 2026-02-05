# Import libraries
import pandas as pd ## for dataset management
import matplotlib.pyplot as plt ## for data visualization
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Read data
data = pd.read_csv('FungusLocations.csv').dropna()
# Build K-means model with 3 clusters
km = KMeans(n_clusters=3, n_init='auto')
km.fit(data)
# Calculate silhouette score
silhouette_avg = silhouette_score(data, km.labels_)
print("Silhouette Score:", round(silhouette_avg,2))
# Visualize the result of k-Means clustering using matplotlib
plt.scatter(data['East'], data['North'], c=km.labels_, cmap='viridis')
plt.xlabel('East')
plt.ylabel('North')
plt.title('k-Means Clustering Result')
plt.show()