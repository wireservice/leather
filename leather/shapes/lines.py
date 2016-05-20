#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape
from leather import theme


class Lines(Shape):
    """
    Render a series of data as a lines.

    :param color:
        The color to stroke the lines.
    :param width:
        The width of the lines. Defaults to :data:`.theme.default_line_width`.
    """
    def __init__(self, stroke_color, width=None):
        self._stroke_color = stroke_color
        self._width = width or theme.default_line_width

    def _new_path(self):
        """
        Start a new path.
        """
        path = ET.Element('path',
            stroke=self._stroke_color,
            fill='none'
        )
        path.set('stroke-width', six.text_type(self._width))

        return path

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render lines to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series lines')

        path = self._new_path()

        d = []

        for x, y, row in series:
            if x is None or y is None:
                if d:
                    path.set('d', ' '.join(d))
                    group.append(path)

                d = []
                path = self._new_path()

                continue

            proj_x = x_scale.project(x, 0, width)
            proj_y = y_scale.project(y, height, 0)

            if not d:
                command = 'M'
            else:
                command = 'L'

            d.extend([
                command,
                six.text_type(proj_x),
                six.text_type(proj_y)
            ])

        if d:
            path.set('d', ' '.join(d))
            group.append(path)

        return group
