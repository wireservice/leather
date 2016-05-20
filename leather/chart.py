#!/usr/bin/env python

from copy import copy
import os
import xml.etree.ElementTree as ET

import six

from leather.axis import Axis
from leather.data_types import Date, DateTime
from leather.legend import Legend
from leather.scales import Scale, Linear, Temporal
from leather.series import Series
from leather.shapes import Bars, Columns, Dots, Lines
import leather.svg as svg
from leather import theme
from leather.utils import X, Y, DIMENSIONS, Box, IPythonSVG


class Chart(object):
    """
    Container for all chart types.

    :param title:
        An optional title that will be rendered at the top of the chart.
    """
    def __init__(self, title=None):
        self._title = title
        self._series_colors = copy(theme.default_series_colors)

        self._legend = None
        self._layers = []
        self._types = [None, None]
        self._scales = [None, None]
        self._axes = [None, None]

    def set_x_scale(self, scale):
        """
        Set the X :class:`.Scale` for this chart.
        """
        self._scales[X] = scale

    def set_y_scale(self, scale):
        """
        See :meth:`.set_x_scale`.
        """
        self._scales[Y] = scale

    def add_x_scale(self, domain_min, domain_max):
        """
        Create and add a :class:`.Scale`.

        If the provided domain values are :class:`date` or :class:`datetime`
        then a :class:`.Temporal` scale will be created, otherwise it will
        :class:`.Linear`.

        If you want to set a custom scale class use :meth:`.set_x_scale`
        instead.
        """
        scale_type = Linear

        if isinstance(domain_min, Date.types) or isinstance(domain_min, DateTime.types):
            scale_type = Temporal

        self.set_x_scale(scale_type(domain_min, domain_max))

    def add_y_scale(self, domain_min, domain_max):
        """
        See :meth:`.add_x_scale`.
        """
        scale_type = Linear

        if isinstance(domain_min, Date.types) or isinstance(domain_min, DateTime.types):
            scale_type = Temporal

        self.set_y_scale(scale_type(domain_min, domain_max))

    def set_x_axis(self, axis):
        """
        Set an :class:`.Axis` class for this chart.
        """
        self._axes[X] = axis

    def set_y_axis(self, axis):
        """
        See :meth:`.set_x_axis`.
        """
        self._axes[Y] = axis

    def add_x_axis(self, ticks=None, tick_formatter=None, name=None):
        """
        Create and add an X :class:`.Axis`.

        If you want to set a custom axis class use :meth:`.set_x_axis` instead.
        """
        self._axes[X] = Axis(ticks, tick_formatter, name)

    def add_y_axis(self, ticks=None, tick_formatter=None, name=None):
        """
        See :meth:`.add_x_axis`.
        """
        self._axes[Y] = Axis(ticks, tick_formatter, name)

    def set_legend(self, legend):
        """
        Set a :class:`.Legend` to use for this chart.
        """
        self._legend = legend

    def add_series(self, series):
        """
        Add a data :class:`.Series` to the chart. The data types of the new
        series must be consistent with any series that have already been added.
        """
        for dim in DIMENSIONS:
            if not self._types[dim]:
                self._types[dim] = series._types[dim]
            elif series._types[dim] is not self._types[dim]:
                raise TypeError('Can\'t mix axis-data types: %s and %s' % (series._types[dim], self._types[dim]))

        self._layers.append(series)

    def add_bars(self, data, x=None, y=None, name=None, color=None):
        """
        Create and add a :class:`.Series` rendered with :class:`.Bars`.
        """
        if not color:
            color = self._series_colors.pop(0)

        self.add_series(Series(data, Bars(color), x=x, y=y, name=name))

    def add_columns(self, data, x=None, y=None, name=None, color=None):
        """
        Create and add a :class:`.Series` rendered with :class:`.Columns`.
        """
        if not color:
            color = self._series_colors.pop(0)

        self.add_series(Series(data, Columns(color), x=x, y=y, name=name))

    def add_dots(self, data, x=None, y=None, name=None, color=None, radius=None):
        """
        Create and add a :class:`.Series` rendered with :class:`.Dots`.
        """
        if not color:
            color = self._series_colors.pop(0)

        self.add_series(Series(data, Dots(color, radius), x=x, y=y, name=name))

    def add_lines(self, data, x=None, y=None, name=None, color=None, width=None):
        """
        Create and add a :class:`.Series` rendered with :class:`.Lines`.
        """
        if not color:
            color = self._series_colors.pop(0)

        self.add_series(Series(data, Lines(color, width), x=x, y=y, name=name))

    def _validate_dimension(self, dimension):
        """
        Validates that the given scale and axis are valid for the data that
        has been added to this chart. If a scale or axis has not been set,
        generates automated ones.
        """
        scale = self._scales[dimension]
        axis = self._axes[dimension]

        if not scale:
            scale = Scale.infer(self._layers, dimension, self._types[dimension])
        else:
            scale = scale

        if not axis:
            axis = Axis()

        return (scale, axis)

    def to_svg_group(self, width=None, height=None):
        """
        Render this chart to an SVG group element.

        This can then be placed inside an :code:`<svg>` tag to make a complete
        SVG graphic.

        See :meth:`.Chart.to_svg` for arguments.
        """
        width = width or theme.default_width
        height = height or theme.default_height

        if not self._layers:
            raise ValueError('You must add at least one series to the chart before rendering.')

        if isinstance(theme.margin, float):
            default_margin = width * theme.margin

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

        # Root / background
        root_group = ET.Element('g')

        root_group.append(ET.Element('rect',
            x=six.text_type(0),
            y=six.text_type(0),
            width=six.text_type(width),
            height=six.text_type(height),
            fill=theme.background_color
        ))

        # Margins
        margin_group = ET.Element('g')
        margin_group.set('transform', svg.translate(margin.left, margin.top))

        margin_width = width - (margin.left + margin.right)
        margin_height = height - (margin.top + margin.bottom)

        root_group.append(margin_group)

        # Header
        header_group = ET.Element('g')

        header_margin = 0

        if self._title:
            label = ET.Element('text',
                x=six.text_type(0),
                y=six.text_type(0),
                fill=theme.title_color
            )
            label.set('font-family', theme.title_font_family)
            label.set('font-size', six.text_type(theme.title_font_size))
            label.text = six.text_type(self._title)

            header_group.append(label)
            header_margin += theme.title_font_char_height + theme.title_gap

        if not self._legend:
            if len(self._layers) > 1:
                self._legend = Legend()

        if self._legend:
            legend_group, legend_height = self._legend.to_svg(margin_width, self._layers)
            legend_group.set('transform', svg.translate(0, header_margin))

            header_margin += legend_height
            header_group.append(legend_group)

        margin_group.append(header_group)

        # Body
        body_group = ET.Element('g')
        body_group.set('transform', svg.translate(0, header_margin))

        body_width = margin_width
        body_height = margin_height - header_margin

        margin_group.append(body_group)

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

        header_group.set('transform', svg.translate(left_margin, 0))

        body_group.append(axes_group)

        # Series
        series_group = ET.Element('g')

        for series in self._layers:
            series_group.append(series.to_svg(canvas_width, canvas_height, x_scale, y_scale))

        axes_group.append(series_group)

        return root_group

    def to_svg(self, path=None, width=None, height=None):
        """
        Render this chart to an SVG document.

        The :code:`width` and :code:`height` are specified in SVG's
        "unitless" units, however, it is usually convenient to specify them
        as though they were pixels.

        :param path:
            Filepath or file-like object to write to. If omitted then the SVG
            will be returned as a string. If running within IPython, then this
            will return a SVG object to be displayed.
        :param width:
            The output width, in SVG user units. Defaults to
            :data:`.theme.default_chart_width`.
        :param height:
            The output height, in SVG user units. Defaults to
            :data:`.theme.default_chart_height`.
        """
        width = width or theme.default_chart_width
        height = height or theme.default_chart_height

        root = ET.Element('svg',
            width=six.text_type(width),
            height=six.text_type(height),
            version='1.1',
            xmlns='http://www.w3.org/2000/svg'
        )

        group = self.to_svg_group(width, height)
        root.append(group)

        svg_text = svg.stringify(root)
        close = True

        if path:
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
                f.write(svg_text)
            finally:
                if close and f is not None:
                    f.close()
        else:
            return IPythonSVG(svg_text)
