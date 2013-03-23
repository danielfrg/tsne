import scipy.linalg as la
import numpy as np


from fasttsne import _TSNE as TSNE


def fast_tsne(data, pca_d=None, d=2, perplexity=30., theta=0.5):
    """
    Run Barnes-Hut T-SNE on _data_.

    @param data         The data.

    @param pca_d        The dimensionality of data is reduced via PCA
                        to this dimensionality.

    @param d            The embedding dimensionality. Must be fixed to
                        2.

    @param perplexity   The perplexity controls the effective number of
                        neighbors.

    @param theta        If set to 0, exact t-SNE is run, which takes
                        very long for dataset > 5000 samples.
    """
    N, _ = data.shape
    
    # inplace!!

    if pca_d is None:
        X = data
    else:
        # do PCA
        data -= data.mean(axis=0)
    
        # working with covariance + (svd on cov.) is 
        # much faster than svd on data directly.
        cov = np.dot(data.T, data)/N
        u, s, v = la.svd(cov, full_matrices=False)
        u = u[:,0:pca_d]
        X = np.dot(data, u)

    tsne = TSNE()
    Y = tsne.run(X, N, X.shape[1], d, perplexity, theta)
    return Y
