#!/usr/bin/env python

from leather.data_types import Number, Text
from leather.shapes import Bars, Columns


class Scale(object):
    """
    Base class for various kinds of scale objects.
    """
    @classmethod
    def infer(cls, series_list, dimension, data_type):
        """
        Infer's an appropriate default scale for a given sequence of series.

        :param chart_series:
            A sequence of :code:`(series, shape)` pairs.
        :param dimension:
            The dimension, :code:`X` or :code:`Y` of the data to infer for.
        """
        from leather.scales.linear import Linear
        from leather.scales.ordinal import Ordinal

        # Default Number scale is Linear
        if data_type is Number:
            force_zero = False
            data_min = 0
            data_max = 0

            for series in series_list:
                if isinstance(series.shape, (Bars, Columns)):
                    force_zero = True

                data_min = min(data_min, series.min(dimension))
                data_max = max(data_max, series.max(dimension))

            if force_zero:
                if data_min > 0:
                    data_min = 0

                if data_max < 0:
                    data_max = 0

            scale = Linear(data_min, data_max)
        # Default Text scale is Ordinal
        elif data_type is Text:
            scale_values = None

            for series in series_list:
                if not scale_values:
                    scale_values = series.values(dimension)
                    continue

                if series.values(dimension) != scale_values:
                    raise ValueError('Mismatched series scales')

            scale = Ordinal(scale_values)

        return scale

    def project(self, value, target_range):
        raise NotImplementedError

    def project_interval(self, value, target_range):
        raise NotImplementedError

    def ticks(self, count):
        raise NotImplementedError
