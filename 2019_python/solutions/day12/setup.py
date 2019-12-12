from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("./update.pyx", include_path=[numpy.get_include()])
)