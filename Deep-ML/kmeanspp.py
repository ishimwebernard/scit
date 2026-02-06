import numpy as np
def kmeans_plus_plus_init(X: np.ndarray, k: int, seed: int = None) -> np.ndarray:
    # Step 0: set seed if provided
    if seed is not None:
        np.random.seed(seed)

    n_samples, n_features = X.shape

    # Array to store centroids
    centroids = np.zeros((k, n_features))

    # Step 1: choose first centroid uniformly at random
    first_idx = np.random.randint(n_samples)
    centroids[0] = X[first_idx]

    # Step 2: choose remaining centroids
    for i in range(1, k):
        # Compute squared distance to nearest centroid
        distances = np.min(
            np.sum((X[:, np.newaxis, :] - centroids[:i]) ** 2, axis=2),
            axis=1
        )

        # Convert distances to probabilities
        probabilities = distances / np.sum(distances)

        # Choose next centroid based on probabilities
        next_idx = np.random.choice(n_samples, p=probabilities)
        centroids[i] = X[next_idx]

    return centroids


X = np.array([[0.0, 0.0], [10.0, 0.0], [0.0, 10.0], [10.0, 10.0]])
result = kmeans_plus_plus_init(X, 2, seed=42)
print(result.tolist())