#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape
from leather import theme


class Dots(Shape):
    """
    Render a series of data as dots.

    :param fill_color:
        The color to fill the dots. You may also specify a function, which will
        be called with the arguments :code:`(x, y, index)` and should return a
        color.
    :param radius:
        The radius of the rendered dots. Defaults to
        :data:`.theme.default_dot_radius`.
    """
    def __init__(self, fill_color, radius=None):
        self._fill_color = fill_color
        self._radius = radius or theme.default_dot_radius

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render dots to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series dots')

        for i, (x, y) in enumerate(series.data):
            if x is None or y is None:
                continue

            proj_x = x_scale.project(x, 0, width)
            proj_y = y_scale.project(y, height, 0)

            if callable(self._fill_color):
                fill_color = self._fill_color(x, y, i)
            else:
                fill_color = self._fill_color

            group.append(ET.Element('circle',
                cx=six.text_type(proj_x),
                cy=six.text_type(proj_y),
                r=six.text_type(self._radius),
                fill=fill_color
            ))

        return group
