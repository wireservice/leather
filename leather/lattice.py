#!/usr/bin/env python

from leather.chart import Chart
from leather.grid import Grid
from leather.scales import Scale
from leather.series import Series
from leather.utils import X, Y


class Lattice(object):
    """
    A grid of charts with synchronized scales and axes.

    :param data:
        A sequence of chart data sequences.
    :param shape:
        An instance of :class:`.Shape` to use to render all series.
    :param titles:
        An optional sequence of titles to be rendered above each chart.
    """
    def __init__(self, data, shape, titles=None):
        self._data = data
        self._shape = shape
        self._titles = titles

    def _validate_dimension(self, dimension, chart_series):
        """
        Verify all series have the same data types and generate a scale to fit
        all the data.
        """
        data_type = chart_series[0].types[dimension]

        for series in chart_series[1:]:
            if series.types[dimension] is not data_type:
                raise TypeError('All series must have the same data types.')

        return Scale.infer(chart_series, dimension, data_type)

    def to_svg(self, path=None, width=None, height=None):
        """
        Render the grid to an SVG.

        See :class:`.Grid` for additional documentation.
        """
        chart_series = []

        for seq in self._data:
            chart_series.append(Series(seq, self._shape))

        x_scale = self._validate_dimension(X, chart_series)
        y_scale = self._validate_dimension(Y, chart_series)

        grid = Grid()

        for i, series in enumerate(chart_series):
            if self._titles:
                title = self._titles[i]
            else:
                title = None

            chart = Chart(title)
            chart.set_x_scale(x_scale)
            chart.set_y_scale(y_scale)
            chart.add_series(series)

            grid.add_chart(chart)

        grid.to_svg(path, width, height)
