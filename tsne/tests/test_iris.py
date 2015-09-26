
def test_iris():
    from tsne import bh_sne
    from sklearn.datasets import load_iris

    iris = load_iris()

    X = iris.data
    y = iris.target

    X_2d = bh_sne(X)
