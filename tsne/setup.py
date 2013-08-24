# encoding: utf-8
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys


if sys.platform == 'darwin':
    ext_modules = [Extension(
                   name="bh_sne",
                   sources=["bh_sne_src/quadtree.cpp", "bh_sne_src/tsne.cpp", "bh_sne.pyx"],
                   include_dirs=[numpy.get_include(), "bh_sne_src/"],
                   extra_compile_args=['-I/System/Library/Frameworks/vecLib.framework/Headers'],
                   extra_link_args=["-Wl,-framework", "-Wl,Accelerate", "-lcblas"],
                   language="c++")]
else:
    ext_modules = [Extension(
                   name="bh_sne",
                   sources=["bh_sne_src/quadtree.cpp", "bh_sne_src/tsne.cpp", "bh_sne.pyx"],
                   include_dirs=[numpy.get_include(), "/usr/local/include", "bh_sne_src/"],
                   library_dirs=["/usr/local/lib"],
                   extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
                   extra_link_args=["-lopenblas"],
                   language="c++")]

setup(
    name="bh_sne",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)
