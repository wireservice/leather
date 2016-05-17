#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape

class Column(Shape):
    """
    Render a series of data as columns.
    """
    def __init__(self, color='green'):
        self.color = color

    def to_svg(self, bbox, x_scale, y_scale, series):
        group = ET.Element('g')

        for x, y in series.data:
            proj_x = x_scale.project(x, [bbox.left, bbox.right])
            proj_y = y_scale.project(y, [bbox.bottom, bbox.top])

            # TKTK
            group.append(ET.Element('circle',
                cx=six.text_type(proj_x),
                cy=six.text_type(proj_y),
                r=six.text_type(self.radius),
                fill=self.color
            ))

        return group
