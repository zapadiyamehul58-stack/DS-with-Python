from sklearn.cluster import KMeans
import numpy as np

data = np.array([[1], [2], [3], [4], [5]])

kmeans = KMeans(n_clusters=3, random_state=5)
kmeans.fit(data)

print("Centers:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
