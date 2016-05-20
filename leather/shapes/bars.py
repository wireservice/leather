#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Bars(Shape):
    """
    Render a series of data as bars.

    :param color:
        The color to fill the bars. You may also specify a
        :func:`.style_function`.
    """
    def __init__(self, fill_color):
        self._fill_color = fill_color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render bars to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series bars')

        zero_x = x_scale.project(0, 0, width)

        for i, (x, y, row) in enumerate(series):
            if x is None or y is None:
                continue

            y1, y2 = y_scale.project_interval(y, height, 0)
            proj_x = x_scale.project(x, 0, width)

            if x < 0:
                bar_x = proj_x
                bar_width = zero_x - proj_x
            else:
                bar_x = zero_x
                bar_width = proj_x - zero_x

            if callable(self._fill_color):
                color = self._fill_color(x, y, row, i)
            else:
                color = self._fill_color

            group.append(ET.Element('rect',
                x=six.text_type(bar_x),
                y=six.text_type(y2),
                width=six.text_type(bar_width),
                height=six.text_type(y1 - y2),
                fill=color
            ))

        return group
