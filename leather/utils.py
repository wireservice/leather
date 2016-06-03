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

#: Z data dimension index
Z = 2

#: Data structure for representing margins or other CSS-edge like properties
Box = namedtuple('Box', ['top', 'right', 'bottom', 'left'])

#: Data structure for a single series data point
Datum = namedtuple('Datum', ['i', 'x', 'y', 'z', 'row'])

#: Dummy object used in place of a series when rendering legends for categories
DummySeries = namedtuple('DummySeries', ['name'])
