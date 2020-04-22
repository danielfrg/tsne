import os
import sys
import platform

from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension

import versioneer
import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize



THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    filepath = os.path.join(THIS_DIR, filename)
    with open(filepath) as file:
        return file.read()


if sys.platform == 'darwin':
    # Platform: Mac OS
    version, _, _ = platform.mac_ver()
    parts = version.split('.')
    v1 = int(parts[0])
    v2 = int(parts[1])
    v3 = int(parts[2]) if len(parts) == 3 else None

    if v2 >= 10:
        # Greater than Mac OS: 10.10
        extra_compile_args = ['-I/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/Headers']
    else:
        extra_compile_args = ['-I/System/Library/Frameworks/vecLib.framework/Headers']

    ext_modules = [Extension(name='bh_sne',
                             sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                             include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                             extra_compile_args=extra_compile_args,
                             extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lcblas'],
                             language='c++')]
else:
    # Platform: Linux
    extra_link_args = ['-lcblas']

    ext_modules = [Extension(name='bh_sne',
                             sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                             include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                             library_dirs=['/usr/local/lib'],
                             extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
                             extra_link_args=extra_link_args,
                             language='c++')]

ext_modules = cythonize(ext_modules)

REQUIREMENTS = read_file("requirements.txt").splitlines()

cmdclass = versioneer.get_cmdclass()
cmdclass['build_ext'] = build_ext

setup(name='tsne',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Daniel Rodriguez',
      author_email='daniel@danielfrg.com',
      url='https://github.com/danielfrg/py_tsne',
      description='TSNE implementations for python',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      license='Apache License Version 2.0',
      packages=find_packages(),
      ext_modules=ext_modules,
      python_requires=">=2.7,>=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
      install_requires=REQUIREMENTS,
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
