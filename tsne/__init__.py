# encoding: utf-8
from __future__ import division
import numpy as np
import scipy.linalg as la
import sys
from bh_sne import BH_SNE

def bh_sne(data, pca_d=None, d=2, perplexity=30., theta=0.5,
           random_state=None, copy_data=False):
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

    @param random_state A numpy RandomState object; if None, use
                        the numpy.random singleton. Init the RandomState
                        with a fixed seed to obtain consistent results
                        from run to run.

    @param copy_data    Copy the data to prevent it from being modified
                        by the C code
    """
    N, _ = data.shape

    if pca_d is None:
        if copy_data:
            X = np.copy(data)
        else:
            X = data
    else:
        # do PCA
        data -= data.mean(axis=0)

        # working with covariance + (svd on cov.) is
        # much faster than svd on data directly.
        cov = np.dot(data.T, data) / N
        u, s, v = la.svd(cov, full_matrices=False)
        u = u[:, 0:pca_d]
        X = np.dot(data, u)

    if random_state is None:
        seed = np.random.randint(2**32-1)
    else:
        seed = random_state.randint(2**32-1)

    tsne = BH_SNE()
    Y = tsne.run(X, N, X.shape[1], d, perplexity, theta, seed)
    return Y

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
