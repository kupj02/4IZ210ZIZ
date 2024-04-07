from sklearn.cluster import AgglomerativeClustering

from new_preprocessing import train_df

hierarchical_clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
hierarchical_clustering.fit(train_df)