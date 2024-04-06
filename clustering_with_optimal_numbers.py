from sklearn.cluster import KMeans
from sklearn import metrics
import random

from clustering import kmeans2, df_train, df_test
from new_preprocessing import df

kmeansBestInertia = KMeans(n_clusters=6, random_state=42, n_init=10)
kmeansBestInertia.fit(df_train)
kmeansBestSilhouette = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeansBestSilhouette.fit(df_train)

instances_clusters = list(kmeans2.predict(df_train))
ground_truth_clusters = list(df_test["stroke"])
random_clusters = [random.randint(0, 1) for i in range(df_test.shape[0])]

myCluster = metrics.rand_score(instances_clusters, ground_truth_clusters)
print(myCluster)
randomCluster = metrics.rand_score(random_clusters, ground_truth_clusters)
print(randomCluster)
