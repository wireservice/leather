#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Columns(Shape):
    """
    Render a series of data as columns.
    """
    def __init__(self, color='green'):
        self.color = color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render columns to SVG elements.
        """
        group = ET.Element('g')

        for x, y in series.data:
            x1, x2 = x_scale.project_interval(x, [0, width])
            proj_y = y_scale.project(y, [height, 0])

            group.append(ET.Element('rect',
                x=six.text_type(x1),
                y=six.text_type(proj_y),
                width=six.text_type(x2 - x1),
                height=six.text_type(height - proj_y),
                fill=self.color
            ))

        return group
