Summary
=======

A python wrapper for [Barnes-Hut t-SNE](http://homepage.tudelft.nl/19j49/t-SNE.html). The wrapper was successfully tested on OSX (10.6), Ubuntu (11.04) and Arch Linux.

The modifications to the original [C++ source](http://homepage.tudelft.nl/19j49/t-SNE_files/bh_tsne.tar.gz) are minimal: See the diff for the second overall commit.

Differently to an already existing [wrapper](https://github.com/ninjin/barnes-hut-sne), I use [cython](cython.org).

Requirements
------------

* [numpy](numpy.scipy.org)
* [cython](cython.org)
* [openblas](https://github.com/xianyi/OpenBLAS). Tested version is v0.2.5 and v0.2.6 (not necessary for OSX).


Building
--------
In the subdirectory(!) ```py_bh-tsne/```, run ```make```. Make sure that your openblas library is available. (Or any other BLAS library, but then changes in ```py_bh-tsne/setup.py``` are necessary.)  If necessary, change ```include_dirs``` and/or ```library_dirs``` in ```py_bh-tsne/setup.py```.


Testing
-------
For testing the algorithm run ```python test.py``` after a successful build. Note that the file ```mnist.pkl.gz``` has to be in the main directory. You can download it from [here](http://deeplearning.net/data/mnist/mnist.pkl.gz).


More Information
----------------
See *Barnes-Hut-SNE*, L.J.P. van der Maaten. It is available on [arxiv](http://arxiv.org/abs/1301.3342).
