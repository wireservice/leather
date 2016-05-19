#!/usr/bin/env python

from collections import namedtuple

try:
    __IPYTHON__
    from IPython.display import SVG as IPythonSVG
except (NameError, ImportError):
    IPythonSVG = lambda x: x


#: X data dimension index
X = 0

#: Y data dimension index
Y = 1

#: List of all data dimensions
DIMENSIONS = [X, Y]

#: Data structure for representing margins or other CSS-edge like properties
Box = namedtuple('Box', ['top', 'right', 'bottom', 'left'])
