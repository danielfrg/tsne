# encoding: utf-8
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys
import platform

DESCRIPTION = 'TSNE implementations for python'
MAVERICKS_VERSION = '10.9'
YOSEMITE_VERSION = '10.10'

if sys.platform == 'darwin':
    # Get OSX version number as string
    v = platform.mac_ver()[0]
    if v.startswith(MAVERICKS_VERSION) or v.startswith(YOSEMITE_VERSION):
      blas_location = ('-I/System/Library/Frameworks/Accelerate.framework/Versions/Current/Frameworks' +
                       '/vecLib.framework/Versions/Current/Headers/')
    else:
      blas_location = '-I/System/Library/Frameworks/vecLib.framework/Headers'

    ext_modules = [Extension(
                   name='bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                   extra_compile_args=[blas_location],
                   extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lcblas'],
                   language='c++')]
else:
    ext_modules = [Extension(
                   name='bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                   library_dirs=['/usr/local/lib'],
                   extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
                   extra_link_args=['-lcblas'],
                   language='c++')]

setup(
    name='tsne',
    version='0.1',
    maintainer='Daniel Rodriguez',
    maintainer_email='df.rodriguez143@gmail.com',
    url='https://github.com/danielfrg/py_tsne',
    packages=['tsne'],
    ext_modules=ext_modules,
    description=DESCRIPTION,
    license='see LICENCE.txt',
    cmdclass={'build_ext': build_ext},
    long_description=open('README.txt').read(),
    install_requires=[
        'Cython>=0.19.1',
        'numpy>=1.7.1',
        'scipy>=0.12.0'
    ],
)

