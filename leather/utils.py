#!/usr/bin/env python

from collections import namedtuple

X = 0
Y = 1
DIMENSIONS = [X, Y]

Box = namedtuple('Box', ['top', 'right', 'bottom', 'left'])
