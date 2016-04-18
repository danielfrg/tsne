
def test_seed():
    from tsne import bh_sne
    from sklearn.datasets import load_iris
    import numpy as np

    iris = load_iris()

    X = iris.data
    y = iris.target

    t1 = bh_sne(X, random_state=np.random.RandomState(0), copy_data=True)
    t2 = bh_sne(X, random_state=np.random.RandomState(0), copy_data=True)
    assert np.all(t1 == t2)
