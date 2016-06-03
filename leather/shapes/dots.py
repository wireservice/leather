#!/usr/bin/env python

from collections import defaultdict
import xml.etree.ElementTree as ET

import six

from leather.series import CategorySeries
from leather.shapes.base import Shape
from leather import theme


class Dots(Shape):
    """
    Render a series of data as dots.

    :param fill_color:
        The color to fill the dots. You may also specify a
        :func:`.style_function`. If not specified, default chart colors will be
        used.
    :param radius:
        The radius of the rendered dots. Defaults to
        :data:`.theme.default_dot_radius`. You may also specify a
        :func:`.style_function`.
    """
    def __init__(self, fill_color=None, radius=None):
        self._fill_color = fill_color
        self._radius = radius or theme.default_dot_radius

    def validate_series(self, series):
        """
        Verify this shape can be used to render a given series.
        """
        return True

    def to_svg(self, width, height, x_scale, y_scale, series, palette):
        """
        Render dots to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series dots')

        default_colors = defaultdict(lambda: next(palette))

        for d in series.data():
            if d.x is None or d.y is None:
                continue

            proj_x = x_scale.project(d.x, 0, width)
            proj_y = y_scale.project(d.y, height, 0)

            if callable(self._fill_color):
                fill_color = self._fill_color(d.x, d.y, d.row, d.i)
            elif self._fill_color:
                fill_color = self._fill_color
            else:
                fill_color = default_colors[d.z]

            if callable(self._radius):
                radius = self._radius(d.x, d.y, d.i)
            else:
                radius = self._radius

            group.append(ET.Element('circle',
                cx=six.text_type(proj_x),
                cy=six.text_type(proj_y),
                r=six.text_type(radius),
                fill=fill_color
            ))

        return group
