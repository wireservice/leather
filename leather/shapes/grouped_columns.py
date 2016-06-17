#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.series import CategorySeries
from leather.shapes.category import CategoryShape
from leather.utils import X, Z


class GroupedColumns(CategoryShape):
    """
    Render a categorized series of data as grouped columns.

    :param fill_color:
        A sequence of colors to fill the columns. The sequence must have length
        greater than or equal to the number of unique values in all categories.
        You may also specify a :func:`.style_function`.
    """
    def __init__(self, fill_color=None):
        self._fill_color = fill_color
        self._legend_dimension = X

    def validate_series(self, series):
        """
        Verify this shape can be used to render a given series.
        """
        if not isinstance(series, CategorySeries):
            raise ValueError('GroupedColumns can only be used to render CategorySeries.')

    def to_svg(self, width, height, x_scale, y_scale, series, palette):
        """
        Render columns to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series grouped-columns')

        zero_y = y_scale.project(0, height, 0)

        if self._fill_color:
            fill_color = self._fill_color
        else:
            fill_color = list(palette)

        label_colors = self.legend_labels(series, fill_color)

        categories = series.categories()
        category_counts = {c: series.values(Z).count(c) for c in categories}
        seen_counts = {c: 0 for c in categories}

        for d in series.data():
            if d.x is None or d.y is None:
                continue

            x1, x2 = x_scale.project_interval(d.z, 0, width)

            group_width = (x2 - x1) / category_counts[d.z]
            x2 = x1 + (group_width * (seen_counts[d.z] + 1)) - 1
            x1 = x1 + (group_width * seen_counts[d.z])

            proj_y = y_scale.project(d.y, height, 0)

            if d.y < 0:
                column_y = zero_y
                column_height = proj_y - zero_y
            else:
                column_y = proj_y
                column_height = zero_y - proj_y

            if callable(fill_color):
                color = fill_color(d)
            else:
                color = dict(label_colors)[d.x]

            seen_counts[d.z] += 1

            group.append(ET.Element('rect',
                x=six.text_type(x1),
                y=six.text_type(column_y),
                width=six.text_type(x2 - x1),
                height=six.text_type(column_height),
                fill=color
            ))

        return group
