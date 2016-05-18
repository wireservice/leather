#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Lines(Shape):
    """
    Render a series of data as a line.
    """
    def __init__(self, width='2px', color='blue'):
        self.width = width
        self.color = color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render lines to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series lines')

        path = ET.Element('path',
            stroke=self.color,
            fill='none'
        )
        path.set('stroke-width', self.width)

        d = []

        for x, y in series.data:
            proj_x = x_scale.project(x, [0, width])
            proj_y = y_scale.project(y, [height, 0])

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

        group.append(path)

        return group
