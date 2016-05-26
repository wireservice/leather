#!/usr/bin/env python

from collections import namedtuple, Sequence
import six

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

def issequence(obj):
    """
    Returns :code:`True` if the given object is an instance of
    :class:`.Sequence` that is not also a string.
    """
    return isinstance(obj, Sequence) and not isinstance(obj, six.string_types)
