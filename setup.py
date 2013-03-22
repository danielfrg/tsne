import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys


if sys.platform == 'darwin':
    ext_modules = [Extension(
        name="py_bh_tsne",
        sources=["fasttsne/quadtree.cpp", "fasttsne/tsne.cpp", "fasttsne/py_bh_tsne.pyx"],
        include_dirs = [numpy.get_include()],
        extra_compile_args=['-faltivec', '-I/System/Library/Frameworks/vecLib.framework/Headers'],
        extra_link_args=["-Wl,-framework", "-Wl,Accelerate", "-lcblas"],
        language="c++"
        )]
else:
    ext_modules = [Extension(
        name="py_bh_tsne",
        sources=["fasttsne/quadtree.cpp", "fasttsne/tsne.cpp", "fasttsne/py_bh_tsne.pyx"],
        include_dirs = [numpy.get_include(), "/usr/local/include"],
        library_dirs = ["/usr/local/lib"],
        extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
        extra_link_args=["-lopenblas"],
        language="c++"
        )]

setup(
    name = "py_bh_tsne",
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules,
    packages=['fasttsne'],
    )
