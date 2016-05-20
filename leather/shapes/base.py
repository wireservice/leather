#!/usr/bin/env python


class Shape(object):
    """
    Base class for shapes that can be used to render data :class:`.Series`.
    """
    pass


def style_function(x, y, row, index):
    """
    This example shows how to define a function to specify style values for
    individual data points.

    :param x:
        The function will be called with the X and Y values from the data.
    :param y:
        See :code:`x`.
    :param row:
        The entire data row will also be passed in, allowing styling based on
        non-coordinate attributes.
    :param index:
        The row index in the series data will also be provided.
    :returns:
        An appropriate value for the attribute being styled.
    """
    pass
