#!/usr/bin/env python

from leather.chart import Chart
from leather.grid import Grid
from leather.scales import Scale
from leather.series import Series
from leather.shapes import Lines
from leather import theme
from leather.utils import DIMENSIONS, X, Y


class Lattice(object):
    """
    A grid of charts with synchronized shapes, scales, and axes.

    Lattice only supports graphing a single series of data.

    :param shape:
        An instance of :class:`.Shape` to use to render all series. Defaults
        to :class:`.Lines` if not specified.
    """
    def __init__(self, shape=None):
        self._shape = shape or Lines(theme.default_series_colors[0])
        self._series = []
        self._types = [None, None]

    def add_one(self, data, x=None, y=None, title=None):
        """
        Add a data series to this lattice.

        :param data:
            A sequence of data suitable for constructing a :class:`.Series`,
            or a sequence of such objects.
        :param x:
            See :class:`.Series`.
        :param y:
            See :class:`.Series`.
        :param title:
            A title to render above this chart.
        """
        series = Series(data, self._shape, x=x, y=y, name=title)

        for dimension in DIMENSIONS:
            if self._types[dimension]:
                if series._types[dimension] is not self._types[dimension]:
                    raise TypeError('All data series must have the same data types.')
            else:
                self._types[dimension] = series._types[dimension]

        self._series.append(series)

    def add_many(self, data, x=None, y=None, titles=None):
        """
        Same as :meth:`.add_one` except :code:`data` is a list of data series
        to be added simultaneously.

        See :meth:`.add_one` for other arguments.

        Note that :code:`titles` is a sequence of titles that must be the same
        length as :code:`data`.
        """
        for i, d in enumerate(data):
            title = titles[i] if titles else None
            self.add_one(d, x=x, y=y, title=title)

    def to_svg(self, path=None, width=None, height=None):
        """
        Render the grid to an SVG.

        See :class:`.Grid` for additional documentation.
        """
        x_scale = Scale.infer(self._series, X, self._types[X])
        y_scale = Scale.infer(self._series, Y, self._types[Y])

        grid = Grid()

        for i, series in enumerate(self._series):
            chart = Chart(title=series._name)
            chart.set_x_scale(x_scale)
            chart.set_y_scale(y_scale)
            chart.add_series(series)

            grid.add_chart(chart)

        grid.to_svg(path, width, height)
