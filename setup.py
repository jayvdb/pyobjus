from distutils.core import setup, Extension
from os import environ
from os.path import dirname, join
import sys

libraries = []
library_dirs = []
extra_compile_args = []
extra_link_args = ["-framework AppKit", "-lobjc"]
include_dirs = []

# detect cython
try:
    from Cython.Distutils import build_ext
    have_cython = True
    ext = 'pyx'
except ImportError:
    from distutils.command.build_ext import build_ext
    have_cython = False
    ext = 'c'


# create the extension
setup(name='pyobjus',
      version='1.0',
      cmdclass={'build_ext': build_ext},
      packages=['pyobjus'],
      ext_package='pyobjus',
      ext_modules=[
          Extension(
              'pyobjus', ['pyobjus/pyobjus.' + ext],
              libraries=libraries,
              library_dirs=library_dirs,
              include_dirs=include_dirs,
              extra_link_args=extra_link_args)
          ]
      )



