#!/usr/bin/env python


class Shape(object):
    """
    Base class for shapes that can be used to render data :class:`.Series`.
    """
    def validate_series(self, series):
        """
        Verify this shape can be used to render a given series.
        """
        raise NotImplementedError


def style_function(datum):
    """
    This example shows how to define a function to specify style values for
    individual data points.

    :param datum:
        A :class:`.Datum` instance for the data row.
    """
    pass
