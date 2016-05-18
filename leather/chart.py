#!/usr/bin/env python

import os
import xml.etree.ElementTree as ET

import six

from leather.axis import Axis
from leather.scales import Scale
from leather.series import Series
from leather.shapes.bars import Bars
from leather.shapes.columns import Columns
from leather.shapes.dots import Dots
from leather.shapes.lines import Lines
import leather.svg as svg
from leather.utils import X, Y, DIMENSIONS, Box

DEFAULT_BARS = Bars()
DEFAULT_COLUMNS = Columns()
DEFAULT_DOTS = Dots()
DEFAULT_LINES = Lines()


class Chart(object):
    """
    Container for all chart types.
    """
    def __init__(self):
        self._layers = []
        self._types = [None, None]
        self._scales = [None, None]
        self._axes = [None, None]

    def _set_scale(self, dimension, scale):
        """
        Set a new scale for this chart.
        """
        self._scales[dimension] = scale

    def set_x_scale(self, scale):
        """
        Set the X scale for this chart.
        """
        self._set_scale(X, scale)

    def set_y_scale(self, scale):
        """
        Set the Y scale for this chart.
        """
        self._set_scale(Y, scale)

    def _set_axis(self, dimension, axis):
        """
        Set a new axis for this chart.
        """
        self._axes[dimension] = axis

    def set_x_axis(self, axis):
        """
        Set the X axis for this chart.
        """
        self._set_axis(X, axis)

    def set_y_axis(self, axis):
        """
        Set the Y axis for this chart.
        """
        self._set_axis(Y, axis)

    def add_series(self, series):
        """
        Add a data :class:`.Series` to the chart.
        """
        for dim in DIMENSIONS:
            if not self._types[dim]:
                self._types[dim] = series.types[dim]
            elif series.types[dim] is not self._types[dim]:
                raise TypeError('Can\'t mix axis-data types: %s and %s' % (series.types[dim], self._types[dim]))

        self._layers.append(series)

    def add_bars(self, data, name=None):
        """
        Shortcut method for adding a bar series to the chart.
        """
        self.add_series(Series(data, DEFAULT_BARS, name=name))

    def add_columns(self, data, name=None):
        """
        Shortcut method for adding a column series to the chart.
        """
        self.add_series(Series(data, DEFAULT_COLUMNS, name=name))

    def add_dots(self, data, name=None):
        """
        Shortcut method for adding a dotted series to the chart.
        """
        self.add_series(Series(data, DEFAULT_DOTS, name=name))

    def add_lines(self, data, name=None):
        """
        Shortcut method for adding a line series to the chart.
        """
        self.add_series(Series(data, DEFAULT_LINES, name=name))

    def _validate_dimension(self, dimension):
        """
        Validates that the given scale and axis are valid for the data that
        has been added to this chart. If a scale or axis has not been set,
        generates automated ones.
        """
        scale = self._scales[dimension]
        axis = self._axes[dimension]

        if not axis:
            if not scale:
                scale = Scale.infer(self._layers, dimension, self._types[dimension])
            else:
                scale = scale

            axis = Axis()
        # Verify data are within bounds
        else:
            pass

        return (scale, axis)

    def to_svg_group(self, width, height, margin=None):
        """
        Render the completechart to an SVG group element that can be placed
        inside an :code:`<svg>` tag.
        """
        if not self._layers:
            raise ValueError('You must add at least one series to the chart before rendering.')

        if not margin:
            default_margin = width * 0.05

            margin = Box(
                top=default_margin,
                right=default_margin,
                bottom=default_margin,
                left=default_margin
            )
        elif not isinstance(margin, Box):
            margin = Box(*margin)

        canvas_width = width - (margin.left + margin.right)
        canvas_height = height - (margin.top + margin.bottom)

        root_group = ET.Element('g')
        root_group.set('transform', svg.translate(margin.left, margin.top))

        # Axes
        axes_group = ET.Element('g')

        x_scale, x_axis = self._validate_dimension(X)
        y_scale, y_axis = self._validate_dimension(Y)

        axes_group.append(x_axis.to_svg(canvas_width, canvas_height, x_scale, 'bottom'))
        axes_group.append(y_axis.to_svg(canvas_width, canvas_height, y_scale, 'left'))

        # Series
        series_group = ET.Element('g')

        for series in self._layers:
            series_group.append(series.to_svg(canvas_width, canvas_height, x_scale, y_scale))

        root_group.append(axes_group)
        root_group.append(series_group)

        return root_group

    def to_svg(self, path, width=600, height=600, margin=None):
        """
        Render this chart to an SVG document.

        :param path:
            Filepath or file-like object to write to.
        """
        root = ET.Element('svg',
            width=six.text_type(width),
            height=six.text_type(height),
            version='1.1',
            xmlns='http://www.w3.org/2000/svg'
        )

        group = self.to_svg_group(width, height, margin)
        root.append(group)

        close = True

        try:
            if hasattr(path, 'write'):
                f = path
                close = False
            else:
                dirpath = os.path.dirname(path)

                if dirpath and not os.path.exists(dirpath):
                    os.makedirs(dirpath)

                f = open(path, 'w')

            f.write(svg.HEADER)

            if six.PY3:
                f.write(ET.tostring(root, encoding='unicode'))
            else:
                f.write(ET.tostring(root, encoding='utf-8'))
        finally:
            if close and f is not None:
                f.close()
