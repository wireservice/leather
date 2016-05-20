#!/usr/bin/env python

from collections import Iterable, Sequence, Mapping

import six

from leather.data_types import DataType
from leather.shapes import Bars
from leather.utils import DIMENSIONS, X, Y


class Series(Iterable):
    """
    A series of data and its associated metadata.

    Series object does not modify or consume the data it is passed.

    :param data:
        A sequence (rows) of sequences (columns), a.k.a. :func:`csv.reader`
        format. If the :code:`x` and :code:`y` are not specified then the first
        column is used as the X values and the second column is used for Y.

        Or, a sequence of (rows) of dicts (columns), a.k.a.
        :class:`csv.DictReader` format. If this format is used then :code:`x`
        and :code:`y` arguments must specify the columns to be charted.

        Or, a custom data format, in which case :code:`x` and :code:`y` must
        specify :func:`.key_function`.
    :param shape:
        An instance of :class:`.Shape` to use to render this data.
    :param x:
        If using sequence row data, then this may be either an integer index
        identifying the X column, or a :func:`.key_function`.

        If using dict row data, then this may be either a key name identifying
        the X column, or a :func:`.key_function`.

        If using a custom data format, then this must be a
        :func:`.key_function`.`
    :param y:
        See :code:`x`.
    :param name:
        An optional name to be used in labeling this series.
    """
    def __init__(self, data, shape, x=None, y=None, name=None):
        self._data = data
        self._shape = shape
        self._name = name

        # Bars should display top-down
        if isinstance(self._shape, Bars):
            self._data = tuple(reversed(self._data))

        self._keys = [
            self._make_key(x if x is not None else X),
            self._make_key(y if y is not None else Y)
        ]

        self._types = [None, None]

        for i in DIMENSIONS:
            self._types[i] = self._infer_type(i)

    def __iter__(self):
        """
        Iterate over this data series. Yields :code:`(x, y, row)`.
        """
        x = self._keys[X]
        y = self._keys[Y]

        for i, row in enumerate(self._data):
            yield (x(row, i), y(row, i), row)

    def _make_key(self, key):
        """
        Process a user-specified data key and convert to a function if needed.
        """
        if callable(key):
            return key
        elif isinstance(self._data[0], Sequence) and not isinstance(key, int):
            raise TypeError('You must specify an integer index when using sequence data.')
        elif isinstance(self._data[0], Mapping) and not isinstance(key, six.string_types):
            raise TypeError('You must specify a string index when using dict data.')
        else:
            return lambda row, index: row[key]

    def _infer_type(self, dimension):
        """
        Infer the datatype of this column by sampling the data.
        """
        key = self._keys[dimension]
        i = 0

        while key(self._data[i], i) is None:
            i += 1

        if i == len(self._data):
            raise ValueError('Entire value column was null.')

        return DataType.infer(key(self._data[i], i))

    def values(self, dimension):
        """
        Get a flattened list of values for a given dimension of the data.
        """
        key = self._keys[dimension]

        return [key(row, i) for i, row in enumerate(self._data)]

    def min(self, dimension):
        """
        Compute the minimum value of a given dimension.
        """
        return min(v for v in self.values(dimension) if v is not None)

    def max(self, dimension):
        """
        Compute the minimum value of a given dimension.
        """
        return max(v for v in self.values(dimension) if v is not None)

    def to_svg(self, width, height, x_scale, y_scale):
        """
        Render this series to SVG elements using it's assigned shape.
        """
        return self._shape.to_svg(width, height, x_scale, y_scale, self)


def key_function(row, index):
    """
    This example shows how to define a function to extract X and Y values
    from custom data.

    :param row:
        The function will be called with the row data, in whatever format it
        was provided to the :class:`.Series`.
    :param index:
        The row index in the series data will also be provided.
    :returns:
        The function must return a chartable value.
    """
    pass
