#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.series import CategorySeries
from leather.shapes.category import CategoryShape
from leather.utils import Y, Z
from leather import theme


class GroupedBars(CategoryShape):
    """
    Render a categorized series of data as grouped bars.

    :param fill_color:
        A sequence of colors to fill the bars. The sequence must have length
        greater than or equal to the number of unique values in all categories. 
        You may also specify a :func:`.style_function`.
    """
    def __init__(self, fill_color=None):
        self._fill_color = fill_color
        self._legend_dimension = Y

    def validate_series(self, series):
        """
        Verify this shape can be used to render a given series.
        """
        if not isinstance(series, CategorySeries):
            raise ValueError('GroupedBars can only be used to render CategorySeries.')

    def to_svg(self, width, height, x_scale, y_scale, series, palette):
        """
        Render bars to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series grouped-bars')

        zero_x = x_scale.project(0, 0, width)

        if self._fill_color:
            fill_color = self._fill_color
        else:
            fill_color = list(palette)

        label_colors = self.legend_labels(series, fill_color)

        categories = series.categories()
        category_counts = {c: series.values(Z).count(c) for c in categories}
        seen_counts = {c: 0 for c in categories}

        # Bars display "top-down"
        for i, d in enumerate(series.data()):
            if d.x is None or d.y is None:
                continue

            y1, y2 = y_scale.project_interval(d.z, height, 0)

            group_height = (y1 - y2) / category_counts[d.z]
            y1 = y2 + (group_height * (seen_counts[d.z] + 1)) - 1
            y2 = y2 + (group_height * seen_counts[d.z])

            proj_x = x_scale.project(d.x, 0, width)

            if d.x < 0:
                bar_x = proj_x
                bar_width = zero_x - proj_x
            else:
                bar_x = zero_x
                bar_width = proj_x - zero_x

            if callable(fill_color):
                color = fill_color(d)
                print(color)
            else:
                color = dict(label_colors)[d.y]

            seen_counts[d.z] += 1

            group.append(ET.Element('rect',
                x=six.text_type(bar_x),
                y=six.text_type(y2),
                width=six.text_type(bar_width),
                height=six.text_type(y1 - y2),
                fill=color
            ))

        return group
