import new_preprocessing
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
df_train = new_preprocessing.df.drop(columns=["stroke"])
df_test = new_preprocessing.df[["stroke"]]

kmeans2 = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans2.fit(df_train)

kmeans_tune = KMeans(random_state=42, n_init=3, max_iter=50)
