import numpy as np

def k_means_pp(X,seed, n_samples):
    if seed is not None:
        np.random.seed(seed)
    n_samples, n_features = X.shape

    centroids = np.zeros(n_samples)

    first_idx = np.random.randint(n_features)
    centroids[0] = first_idx

    for i in range(n_samples):
        print(n_samples, n_features)
        print(centroids)

#print(np.random.randint(42))
k_means_pp(np.array([[1,2], [3,4]]), 42, 3)