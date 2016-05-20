#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Columns(Shape):
    """
    Render a series of data as columns.

    :param color:
        The color to fill the columns. You may also specify a
        :func:`.style_function`.
    """
    def __init__(self, fill_color):
        self._fill_color = fill_color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render columns to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series columns')

        zero_y = y_scale.project(0, height, 0)

        for i, (x, y, row) in enumerate(series):
            if x is None or y is None:
                continue

            x1, x2 = x_scale.project_interval(x, 0, width)
            proj_y = y_scale.project(y, height, 0)

            if y < 0:
                column_y = zero_y
                column_height = proj_y - zero_y
            else:
                column_y = proj_y
                column_height = zero_y - proj_y

            if callable(self._fill_color):
                color = self._fill_color(x, y, row, i)
            else:
                color = self._fill_color

            group.append(ET.Element('rect',
                x=six.text_type(x1),
                y=six.text_type(column_y),
                width=six.text_type(x2 - x1),
                height=six.text_type(column_height),
                fill=color
            ))

        return group
