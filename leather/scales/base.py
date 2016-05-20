#!/usr/bin/env python

from datetime import date, datetime

from leather.data_types import Date, DateTime, Number, Text
from leather.shapes import Bars, Columns


class Scale(object):
    """
    Base class for various kinds of scale objects.
    """
    @classmethod
    def infer(cls, series_list, dimension, data_type):
        """
        Infer's an appropriate default scale for a given sequence of
        :class:`.Series`.

        :param chart_series:
            A sequence of :class:`.Series` instances
        :param dimension:
            The dimension, :code:`X` or :code:`Y` of the data to infer for.
        :param data_type:
            The type of data contained in the series dimension.
        """
        from leather.scales.linear import Linear
        from leather.scales.ordinal import Ordinal
        from leather.scales.temporal import Temporal

        # Default Time scale is Temporal
        if data_type is Date:
            data_min = date.max
            data_max = date.min

            for series in series_list:
                data_min = min(data_min, series.min(dimension))
                data_max = max(data_max, series.max(dimension))

            scale = Temporal(data_min, data_max)
        elif data_type is DateTime:
            data_min = datetime.max
            data_max = datetime.min

            for series in series_list:
                data_min = min(data_min, series.min(dimension))
                data_max = max(data_max, series.max(dimension))

            scale = Temporal(data_min, data_max)
        # Default Number scale is Linear
        elif data_type is Number:
            force_zero = False
            data_min = float('inf')
            data_max = float('-inf')

            for series in series_list:
                if isinstance(series._shape, (Bars, Columns)):
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

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        raise NotImplementedError

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        raise NotImplementedError

    def ticks(self, count):
        """
        Generate a series of ticks for this scale.
        """
        raise NotImplementedError
