import numpy as np
def k_means_pp(X: np.ndarray, k:int, seed: int = None) -> np.ndarr:
    if seed is not None:
        np.random.seed(seed)
    n_samples, n_features = X.shape
    centroids = np.zeros((k, n_features))
    first_idx = np.random.randint(n_samples)
    centroids[0] = X[first_idx]
    for i in range(1, k):
        distances = np.min(
            np.sum((X[:, np.newaxis, :] - centroids[:i])**2, axis=2), 
        axis=1
        )
        probabilities = distances / np.sum(distances)

        next_idx = np.random.choice(n_samples, p=probabilities)
        centroids[i] = X[next_idx]
        return centroids

X = np.array([[0.0, 0.0], [10.0, 0.0], [0.0, 10.0], [10.0, 10.0]])
result = k_means_pp(X, 2, seed=42)
print(result.tolist())