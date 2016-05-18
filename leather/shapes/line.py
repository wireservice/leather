#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape

class Line(Shape):
    """
    Render a series of data as a line.
    """
    def __init__(self, width='2px', color='blue'):
        self.width = width
        self.color = color

    def to_svg(self, bbox, x_scale, y_scale, series):
        """
        Render lines to SVG elements.
        """
        path = ET.Element('path',
            stroke=self.color,
            fill='none'
        )
        path.set('stroke-width', self.width)

        d = []

        for x, y in series.data:
            proj_x = x_scale.project(x, [bbox.left, bbox.right])
            proj_y = y_scale.project(y, [bbox.bottom, bbox.top])

            if not d:
                command = 'M'
            else:
                command = 'L'

            d.extend([
                command,
                six.text_type(proj_x),
                six.text_type(proj_y)
            ])

        path.set('d', ','.join(d))

        return path
