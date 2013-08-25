# encoding: utf-8
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys

DESCRIPTION = 'TSNE implementations for python'


if sys.platform == 'darwin':
    ext_modules = [Extension(
                   name='bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                   extra_compile_args=['-I/System/Library/Frameworks/vecLib.framework/Headers'],
                   extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lcblas'],
                   language='c++')]
else:
    ext_modules = [Extension(
                   name='bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                   library_dirs=['/usr/local/lib'],
                   extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
                   extra_link_args=['-lopenblas'],
                   language='c++')]

setup(
    name='tsne',
    version='0.0.1',
    maintainer='Daniel Rodriguez',
    maintainer_email='df.rodriguez143@gmail.com',
    packages=['tsne'],
    ext_modules=ext_modules,
    description=DESCRIPTION,
    license='see LICENCE.txt',
    cmdclass={'build_ext': build_ext},
    long_description=open('README.txt').read(),
    url='https://github.com/danielfrg/py_tsne',
    install_requires=[
        'Cython==0.19.1',
        'numpy==1.7.1',
        'scipy==0.12.0'
    ],
)
