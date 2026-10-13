import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state

    def fit(self, X):
        if self.random_state is not None:
            np.random.seed(self.random_state)

        # TODO: Implement the KMeans clustering algorithm.
        # Note: You should have attributes `cluster_centers_` and `labels_` after fitting.
        # =================================================================

        # =================================================================
        return self

    def predict(self, X):
        # Compute distances and assign cluster labels
        distances = np.linalg.norm(
            X[:, None] - self.cluster_centers_[None, :], axis=2
        )
        return np.argmin(distances, axis=1)

    def fit_predict(self, X):
        self.fit(X)
        return self.labels_


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.decomposition import PCA

    # Load Iris dataset
    iris = load_iris()
    X = iris.data

    # Reduce to 2D using PCA for visualization
    pca = PCA(n_components=2)
    X_2d = pca.fit_transform(X)

    # Apply custom KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_2d)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    print("\nCluster Centers:\n", centers)

    # Create a mesh grid for decision boundary visualization
    x_min, x_max = X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1
    y_min, y_max = X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                         np.linspace(y_min, y_max, 500))

    # Predict cluster labels for all grid points
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot decision boundary
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap="viridis", alpha=0.4)

    # Plot data points
    plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap="viridis", s=30)

    # Plot cluster centers
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)

    plt.title("KMeans Decision Boundary on Iris (PCA 2D)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()

