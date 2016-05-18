#!/usr/bin/env python

from leather.data_types import DataType
from leather.utils import DIMENSIONS


class Series(object):
    """
    A series of data and associated metadata.

    :param data:
        A sequence of 2-item sequences, where each pair contains :code:`(x, y)`
        values.
    :param name:
        An optional name to be used in labeling this series.
    """
    def __init__(self, data, name=None):
        self.data = data
        self.name = name

        self.types = [None, None]

        for i in DIMENSIONS:
            self.types[i] = self._infer_type(i)

    def _infer_type(self, dimension):
        i = 0

        while self.data[i][dimension] is None:
            i += 1

        return DataType.infer(self.data[i][dimension])

    def values(self, dimension):
        """
        Get a flattened list of values for a given dimension of the data.
        """
        return [d[dimension] for d in self.data]

    def min(self, dimension):
        """
        Compute the minimum value of a given dimension.
        """
        return min(self.values(dimension))

    def max(self, dimension):
        """
        Compute the minimum value of a given dimension.
        """
        return max(self.values(dimension))
