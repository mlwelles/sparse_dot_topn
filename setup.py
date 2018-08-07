# Terrible hack, but not sure how else to make sure cython is installed
# prior to the requirement beeing needed, since it install_requires and
# setup_requires can't be now be parsed to specify the dependency prior to
# it being used
try:
    from Cython.Build import cythonize
except:
    import subprocess
    subprocess.run(('pip3', 'install', 'cython', 'numpy'))
import numpy
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup, Extension
from sparse_dot_topn import __version__

ext_utils = Extension('sparse_dot_topn.sparse_dot_topn',
                      sources=['./sparse_dot_topn/sparse_dot_topn.pyx', './sparse_dot_topn/sparse_dot_topn_source.cpp'],
                      include_dirs=[numpy.get_include()],
                      #libraries=[],
                      extra_compile_args=['-std=c++0x', '-Os'],
                      language='c++',
                     )

setup(name='sparse_dot_topn',
      version=__version__,
      setup_requires=[
          # Setuptools 18.0 properly handles Cython extensions.
          'setuptools>=18.0',
          'cython',
      ],
       install_requires=[
           'numpy',
           'cython',
      ],
      packages=['sparse_dot_topn'],
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize([ext_utils]),
     )
