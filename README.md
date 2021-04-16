# Python-TSNE

[![pypi](https://badge.fury.io/py/tsne.svg)](https://pypi.org/project/tsne/)
[![build](https://github.com/danielfrg/tsne/workflows/test/badge.svg)](https://github.com/danielfrg/tsne/actions/workflows/test.yml)
[![coverage](https://codecov.io/gh/danielfrg/tsne/branch/master/graph/badge.svg)](https://codecov.io/gh/danielfrg/tsne?branch=master)
[![license](https://img.shields.io/:license-Apache%202-blue.svg)](http://github.com/danielfrg/tsne/blob/master/LICENSE.txt)

Python library containing T-SNE algorithms.

**Note:** [Scikit-learn v0.17](http://scikit-learn.org/stable/whats_new.html#version-0-17)
includes TSNE algorithms and you should probably be using that instead.

## Installation

## Requirements

- [cblas](http://www.netlib.org/blas/) or [openblas](https://github.com/xianyi/OpenBLAS).
Tested version is v0.2.5 and v0.2.6 (not necessary for OSX).

From PyPI:

```
pip install tsne
```

From conda:

```
conda install -c maxibor tsne
```

## Usage

Basic usage:

```python
from tsne import bh_sne
X_2d = bh_sne(X)
```

### Examples

- [Iris](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/iris.ipynb)
- [MNIST](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/mnist.ipynb)
- [word2vec on presidential speeches](https://github.com/prateekpg2455/U.S-Presidential-Speeches) via [@prateekpg2455](https://github.com/prateekpg2455)

## Algorithms

### Barnes-Hut-SNE

A python ([cython](http://www.cython.org)) wrapper for [Barnes-Hut-SNE](http://homepage.tudelft.nl/19j49/t-SNE.html) aka fast-tsne.

I basically took [osdf's code](https://github.com/osdf/py_bh_tsne) and made it pip compliant.

## Additional resources

- See *Barnes-Hut-SNE* (2013), L.J.P. van der Maaten. It is available on [arxiv](http://arxiv.org/abs/1301.3342).
