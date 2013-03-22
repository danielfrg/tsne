all:
	python setup.py build_ext --inplace
	python setup.py install

clean :
	rm -rf *.pyc *.so build/ py_bh_tsne.cpp
