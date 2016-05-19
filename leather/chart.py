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
    def __init__(self, title=None):
        self._title = title

        self.title_color = '#333'
        self.title_font_family = 'Monaco'
        self.title_font_size = '16px'
        self.title_font_char_height = 20
        self.title_font_char_width = 9

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

        See :meth:`to_svg` for argument descriptions.
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
        elif isinstance(margin, int):
            margin = Box(margin, margin, margin, margin)
        elif not isinstance(margin, Box):
            margin = Box(*margin)

        root_width = width - (margin.left + margin.right)
        root_height = height - (margin.top + margin.bottom)

        root_group = ET.Element('g')
        root_group.set('transform', svg.translate(margin.left, margin.top))

        header_group = ET.Element('g')
        header_margin = 0

        # Title
        if self._title:
            label = ET.Element('text',
                x=six.text_type(0),
                y=six.text_type(0),
                fill=self.title_color
            )
            label.set('font-family', self.title_font_family)
            label.set('font-size', self.title_font_size)
            label.text = six.text_type(self._title)

            header_group.append(label)
            header_margin += self.title_font_char_height

        body_group = ET.Element('g')
        body_group.set('transform', svg.translate(0, header_margin))

        body_width = root_width
        body_height = root_height - header_margin

        # Axes
        x_scale, x_axis = self._validate_dimension(X)
        y_scale, y_axis = self._validate_dimension(Y)

        bottom_margin = x_axis.estimate_label_margin(x_scale, 'bottom')
        left_margin = y_axis.estimate_label_margin(y_scale, 'left')

        canvas_width = body_width - left_margin
        canvas_height = body_height - bottom_margin

        axes_group = ET.Element('g')
        axes_group.set('transform', svg.translate(left_margin, 0))

        axes_group.append(x_axis.to_svg(canvas_width, canvas_height, x_scale, 'bottom'))
        axes_group.append(y_axis.to_svg(canvas_width, canvas_height, y_scale, 'left'))

        # Series
        series_group = ET.Element('g')

        for series in self._layers:
            series_group.append(series.to_svg(canvas_width, canvas_height, x_scale, y_scale))

        axes_group.append(series_group)
        body_group.append(axes_group)

        root_group.append(header_group)
        root_group.append(body_group)

        return root_group

    def to_svg(self, path, width=600, height=600, margin=None):
        """
        Render this chart to an SVG document.

        :param path:
            Filepath or file-like object to write to.
        :param width:
            The output width, in SVG user units.
        :param height:
            The output height, in SVG user units.
        :param margin:
            An instance of :class:`.Box`, a sequence of offsets in the format
            :code:`(top, right, bottom, left)` or a single :code:`int` to be
            used for all sides. Or, :code:`None`, in which case a default offset
            equal to 5% of :code:`width`.
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
