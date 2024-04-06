import new_preprocessing
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

kmeans2 = KMeans(n_clusters=2, random_state=123, n_init=10)
kmeans2.fit(new_preprocessing.train_df)

kmeans_tune = KMeans(random_state=123, n_init=3, max_iter=50)
