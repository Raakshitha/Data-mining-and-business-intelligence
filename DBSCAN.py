
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

db = DBSCAN(eps=0.3, min_samples=5)
clusters = db.fit_predict(X_scaled)

data = pd.DataFrame(X_scaled, columns=["Feature1", "Feature2"])
data["Cluster"] = clusters

plt.figure(figsize=(8, 6))
plt.scatter(data["Feature1"], data["Feature2"], c=data["Cluster"], cmap='rainbow', s=40, edgecolors='k')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("DBSCAN Clustering")
plt.grid(True)
plt.show()

print("Number of clusters:", len(set(clusters)) - (1 if -1 in clusters else 0))
