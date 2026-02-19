import numpy as np

def k_means_pp(X,seed, n_samples):
    if seed is not None:
        np.random.randint(seed)
    n_samples, n_features = X.shape

    centroids = np.zeros(n_samples)
    print(n_samples, n_features)
    print(centroids)

#print(np.random.randint(42))
k_means_pp(np.array([[1,2], [3,4]]), 42, 3)