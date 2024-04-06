#Silhouette
from yellowbrick.cluster import KElbowVisualizer

import new_preprocessing
from clustering import kmeans_tune

visualizer = KElbowVisualizer(kmeans_tune,  k=(2,20), metric="silhouette")
visualizer.fit(new_preprocessing.train_df)
visualizer.show()