from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        Extension(
            "rect",                 # the extenstion name
            sources=[
                "rect.pyx",         # our Cython source
                "Rectangle.cpp"     # additional source file(s)
            ],
            language="c++"          # generate C++ code
        )
    )
)
