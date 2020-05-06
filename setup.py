import os
import platform
import sys

import numpy
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import Extension, find_packages, setup

setup_dir = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(this_dir, filename)
    with open(filepath) as file:
        return file.read()


def parse_git(root, **kwargs):
    """
    Parse function for setuptools_scm
    """
    from setuptools_scm.git import parse

    kwargs["describe_command"] = "git describe --dirty --tags --long"
    return parse(root, **kwargs)


if sys.platform == "darwin":
    # Platform: Mac OS
    version, _, _ = platform.mac_ver()
    parts = version.split(".")
    major = int(parts[0])
    minor = int(parts[1])
    patch = int(parts[2]) if len(parts) == 3 else None

    if minor >= 15:
        # Greater than Mac OS: 10.15
        extra_compile_args = [
            "-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks/Accelerate.framework/Versions/Current/Frameworks/vecLib.framework/Headers/"
        ]
    elif minor >= 10:
        # Greater than Mac OS: 10.10
        extra_compile_args = [
            "-I/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/Current/Headers"
        ]
    else:
        extra_compile_args = ["-I/System/Library/Frameworks/vecLib.framework/Headers"]

    ext_modules = [
        Extension(
            name="bh_sne",
            sources=[
                "tsne/includes/bh_tsne/quadtree.cpp",
                "tsne/includes/bh_tsne/tsne.cpp",
                "tsne/bh_sne.pyx",
            ],
            include_dirs=[numpy.get_include(), "tsne/includes/bh_tsne/"],
            extra_compile_args=extra_compile_args,
            extra_link_args=["-Wl,-framework", "-Wl,Accelerate", "-lcblas"],
            language="c++",
        )
    ]
else:
    # Platform: Linux
    extra_link_args = ["-lcblas"]

    ext_modules = [
        Extension(
            name="bh_sne",
            sources=[
                "tsne/includes/bh_tsne/quadtree.cpp",
                "tsne/includes/bh_tsne/tsne.cpp",
                "tsne/bh_sne.pyx",
            ],
            include_dirs=[
                numpy.get_include(),
                "/usr/local/include",
                "tsne/includes/bh_tsne/",
            ],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-msse2", "-O3", "-fPIC", "-w"],
            extra_link_args=extra_link_args,
            language="c++",
        )
    ]


setup(
    name="tsne",
    packages=find_packages() + ["tsne.tests"],
    zip_safe=False,
    include_package_data=True,
    package_data={"tsne": ["includes/*"]},
    # data_files=data_files,
    ext_modules=cythonize(ext_modules),
    cmdclass={"build_ext": build_ext},
    # entry_points = {},
    use_scm_version={
        "root": setup_dir,
        "parse": parse_git,
        "write_to": os.path.join("tsne/_generated_version.py"),
    },
    test_suite="tsne/tests",
    setup_requires=["setuptools_scm"],
    install_requires=read_file("requirements.package.txt").splitlines(),
    tests_require=["pytest",],
    python_requires=">=3.6",
    description="",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    license="Apache License, Version 2.0",
    maintainer="Daniel Rodriguez",
    maintainer_email="daniel@danielfrg.com",
    url="https://github.com/danielfrg/tsne",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["TSNE", "algorithms", "numpy", "cython"],
)
