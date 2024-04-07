#Inertia
from yellowbrick.cluster import KElbowVisualizer

import new_preprocessing
from clustering import kmeans_tune, df_train

visualizer = KElbowVisualizer(kmeans_tune,  k=(2,20), metric="distortion")
visualizer.fit(df_train)
visualizer.show()
