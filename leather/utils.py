#!/usr/bin/env python

from collections import namedtuple

#: X data dimension index
X = 0

#: Y data dimension index
Y = 1

#: List of all data dimensions
DIMENSIONS = [X, Y]

#: Data structure for representing margins or other CSS-edge like properties
Box = namedtuple('Box', ['top', 'right', 'bottom', 'left'])

def svg_translate(x, y):
    return 'translate(%i %i)' % (x, y)
