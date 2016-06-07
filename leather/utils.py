#!/usr/bin/env python

from collections import namedtuple
from decimal import Decimal
import math
import sys

try:
    __IPYTHON__
    from IPython.display import SVG as IPythonSVG
except (NameError, ImportError):
    IPythonSVG = lambda x: x


# Shorthand
ZERO = Decimal('0')
NINE_PLACES = Decimal('1e-9')

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


# In Python 3.5 use builtin C implementation of `isclose`
if sys.version_info >= (3, 5):
    from math import isclose
else:
    def isclose(a, b, rel_tol=NINE_PLACES, abs_tol=ZERO):
        """
        Test if two floating points numbers are close enough to be considered
        equal.

        Via: https://github.com/PythonCHB/close_pep/blob/master/isclose.py

        Verified against final CPython 3.5 implemenation.

        :param a:
            The first number to check.
        :param b:
            The second number to check.
        :param rel_tol:
            Relative tolerance. The amount of error allowed, relative to the larger
            input value. Defaults to nine decimal places of accuracy.
        :param abs_tol:
            Absolute minimum tolerance. Disabled by default.
        """
        if a == b:
            return True

        if rel_tol < ZERO or abs_tol < ZERO:
            raise ValueError('Tolerances must be non-negative')

        if math.isinf(abs(a)) or math.isinf(abs(b)):
            return False

        diff = abs(b - a)

        return (((diff <= abs(rel_tol * b)) or
                (diff <= abs(rel_tol * a))) or
                (diff <= abs_tol))
