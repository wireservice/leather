#!/usr/bin/env python

from leather.chart import Chart
from leather.data_types import Number, Text
from leather.grid import Grid
from leather.scales.linear import LinearScale
from leather.scales.ordinal import OrdinalScale
from leather.series import Series
from leather.utils import X, Y


class Lattice(object):
    """
    A grid of charts with synchronized scales.

    :param data:
         A sequence of chart data sequences.
    """
    def __init__(self, data, shape):
        self._data = data
        self._shape = shape

    def _validate_dimension(self, dimension, chart_series):
        scale = None
        axis = None

        data_type = chart_series[0].types[dimension]

        for series in chart_series[1:]:
            if series.types[dimension] is not data_type:
                raise TypeError('All series must have the same data types.')

        # Default Number scale is Linear
        if data_type is Number:
            data_min = min([series.min(dimension) for series in chart_series])
            data_max = max([series.max(dimension) for series in chart_series])

            scale = LinearScale(data_min, data_max)
        # Default Text scale is Ordinal
        elif data_type is Text:
            scale_values = None

            for series in chart_series:
                if not scale_values:
                    scale_values = series.values(dimension)
                    continue

                if series.values(dimension) != scale_values:
                    raise ValueError('Mismatched series scales')

            scale = OrdinalScale(scale_values)

        return (scale, axis)

    def to_svg(self, path, width=1200, height=1200):
        """
        Render the grid to an SVG.
        """
        chart_series = []

        for seq in self._data:
            chart_series.append(Series(seq))

        x_scale, x_axis = self._validate_dimension(X, chart_series)
        y_scale, y_axis = self._validate_dimension(Y, chart_series)

        grid = Grid()

        for series in chart_series:
            chart = Chart()
            chart.set_x_scale(x_scale)
            chart.set_y_scale(y_scale)
            chart.set_x_axis(x_axis)
            chart.set_y_axis(y_axis)
            chart.add_series(series, self._shape)

            grid.add_chart(chart)

        grid.to_svg(path, width, height)
