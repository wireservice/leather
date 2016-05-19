#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Bars(Shape):
    """
    Render a series of data as columns.
    """
    def __init__(self, color):
        self.color = color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render columns to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series bars')

        for x, y in series.data:
            proj_x = x_scale.project(x, 0, width)
            y1, y2 = y_scale.project_interval(y, height, 0)

            group.append(ET.Element('rect',
                x=six.text_type(0),
                y=six.text_type(y2),
                width=six.text_type(proj_x),
                height=six.text_type(y1 - y2),
                fill=self.color
            ))

        return group
