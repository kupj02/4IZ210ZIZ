from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from clustering import df_train
from clustering_with_optimal_numbers import kmeansBestInertia


def plot_clusters(data, clusters):
    for cluster_num in range(clusters.n_clusters):
        cluster_mask = (clusters.labels_ == cluster_num)
        cluster_data = data[cluster_mask]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f"Cluster {cluster_num}")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title("K-Means Clusters (PCA-reduced data)")
    plt.legend()
    plt.show()


pca = PCA(n_components=2, random_state=42)
plot_clusters(pca.fit_transform(df_train), kmeansBestInertia)
