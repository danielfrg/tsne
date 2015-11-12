Python-TSNE
===========

[![travis-ci](https://api.travis-ci.org/danielfrg/tsne.svg)](https://travis-ci.org/danielfrg/tsne)

Python library containing T-SNE algorithms.

**Note:** [Scikit-learn v0.17](http://scikit-learn.org/stable/whats_new.html#version-0-17)
includes TSNE algorithms and you should probably be using them instead of this.

Algorithms
----------

### Barnes-Hut-SNE

A python ([cython](http://www.cython.org)) wrapper for [Barnes-Hut-SNE](http://homepage.tudelft.nl/19j49/t-SNE.html) aka fast-tsne.

I basically took [osdf's code](https://github.com/osdf/py_bh_tsne) and made it pip compliant.

Requirements
------------

* [numpy](numpy.scipy.org) > =1.7.1
* [scipy](http://www.scipy.org/) >= 0.12.0
* [cython](cython.org) >= 0.19.1
* [cblas](http://www.netlib.org/blas/) or [openblas](https://github.com/xianyi/OpenBLAS). Tested version is v0.2.5 and v0.2.6 (not necessary for OSX).

[Anaconda](http://continuum.io/downloads) is recommended.

Installation
------------

You can install the package from [PyPI](https://pypi.python.org/pypi):

```
pip install tsne
```

Or directly from the Github repository:

```
pip install git+https://github.com/danielfrg/tsne.git
```

Or using docker (could be useful for testing):

```
$ docker build -t tsne .
$ docker run -it -v /Users/drodriguez/workspace/tsne/:/tsne tsn

# Inside Docker:
$ python setup.py install
```

Usage
-----

Basic usage:

```
from tsne import bh_sne
X_2d = bh_sne(X)
```

### Examples

* [Iris](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/iris.ipynb)
* [MNIST](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/mnist.ipynb)
* [word2vec on presidential speeches](https://github.com/prateekpg2455/U.S-Presidential-Speeches) via [@prateekpg2455](https://github.com/prateekpg2455)

More Information
----------------

See *Barnes-Hut-SNE* (2013), L.J.P. van der Maaten. It is available on [arxiv](http://arxiv.org/abs/1301.3342).
