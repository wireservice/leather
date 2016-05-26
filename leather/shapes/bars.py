#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape
from leather.utils import Y, issequence


class Bars(Shape):
    """
    Render a series of data as bars.

    :param color:
        The color to fill the bars. You may also specify a
        :func:`.style_function` or a sequence of colors for grouped bars.
    :param grouped:
        If True, any values in data with equal x values will be rendered as
        grouped bars. Defaults to False.
    """
    def __init__(self, fill_color, grouped=False):
        self._fill_color = fill_color
        self._grouped = grouped

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render bars to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series bars')

        zero_x = x_scale.project(0, 0, width)

        if self._grouped:
            y_values = series.values(Y)
            y_counts = {y: y_values.count(y) for y in set(y_values)}
        
            seen_y_counts = {y: 0 for y in set(y_values)}

        for i, (x, y, row) in enumerate(series):
            if x is None or y is None:
                continue

            y1, y2 = y_scale.project_interval(y, height, 0)

            if self._grouped:
                group_height = (y1 - y2) / y_counts[y]

                y1 = y2 + (group_height * (seen_y_counts[y] + 1)) - 1
                y2 = y2 + (group_height * seen_y_counts[y])
                seen_y_counts[y] += 1

            proj_x = x_scale.project(x, 0, width)

            if x < 0:
                bar_x = proj_x
                bar_width = zero_x - proj_x
            else:
                bar_x = zero_x
                bar_width = proj_x - zero_x

            if callable(self._fill_color):
                color = self._fill_color(x, y, row, i)
            elif issequence(self._fill_color) and self._grouped:
                color = self._fill_color[seen_y_counts[y] - 1]
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
