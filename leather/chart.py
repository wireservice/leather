#!/usr/bin/env python

import os
import xml.etree.ElementTree as ET

import six

from leather.axes.x import XAxis
from leather.axes.y import YAxis
from leather.scales.linear import LinearScale
from leather.series import Series
from leather.shapes.dot import Dot
from leather.shapes.line import Line
from leather.utils import Box

DEFAULT_DOT = Dot()
DEFAULT_LINE = Line()

class Chart(object):
    """
    Container for all chart types.
    """
    def __init__(self):
        self.width = 800
        self.height = 400
        self.margin = Box(
            top=20,
            right=20,
            bottom=20,
            left=20
        )

        self.x_scale = None
        self.y_scale = None

        self.x_axis = None
        self.y_axis = None

        self.layers = []

    def add_series(self, series, shape):
        """
        Add a data :class:`.Series` to the chart.
        """
        self.layers.append((series, shape))

        # Validate added series has same scale types as other series?
        #if x_datum isinstance(number)

    def add_line(self, data, name=None, id=None, classes=None):
        """
        Shortcut method for adding a line series to the chart.
        """
        self.add_series(Series(data, name=name, id=id, classes=classes), DEFAULT_LINE)

    def add_dot(self, data, name=None, id=None, classes=None):
        """
        Shortcut method for adding a dotted series to the chart.
        """
        self.add_series(Series(data, name=name, id=id, classes=classes), DEFAULT_DOT)

    def _validate_x_axis(self):
        if not self.x_axis:
            if not self.x_scale:
                x_min = 0
                x_max = 0

                for series, shape in self.layers:
                    for d in series.data:
                        x_min = min(x_min, d[0])
                        x_max = max(x_max, d[0])

                scale = LinearScale([x_min, x_max])
            else:
                scale = self.x_scale

            axis = XAxis(scale)
        # Verify data are within bounds
        else:
            pass

        return (scale, axis)

    def _validate_y_axis(self):
        if not self.y_axis:
            if not self.y_scale:
                y_min = 0
                y_max = 0

                for series, shape in self.layers:
                    for d in series.data:
                        y_min = min(y_min, d[1])
                        y_max = max(y_max, d[1])

                scale = LinearScale([y_min, y_max])
            else:
                scale = self.y_scale

            axis = YAxis(scale)
        # Verify data are within bounds
        else:
            pass

        return (scale, axis)

    def to_svg(self, path):
        canvas_bbox = Box(
            top=self.margin.top,
            right=self.width - self.margin.right,
            bottom=self.height - self.margin.bottom,
            left=self.margin.left
        )

        x_scale, x_axis = self._validate_x_axis()
        y_scale, y_axis = self._validate_y_axis()

        svg = ET.Element('svg',
            width=six.text_type(self.width),
            height=six.text_type(self.height),
            version='1.1',
            xmlns='http://www.w3.org/2000/svg'
        )

        svg.append(x_axis.to_svg(canvas_bbox))
        svg.append(y_axis.to_svg(canvas_bbox))

        for series, shape in self.layers:
            svg.append(shape.to_svg(canvas_bbox, x_scale, y_scale, series))

        close = True

        try:
            if hasattr(path, 'write'):
                f = path
                close = False
            else:
                dirpath = os.path.dirname(path)

                if dirpath and not os.path.exists(dirpath):
                    os.makedirs(dirpath)

                f = open(path, 'w')

            f.write('<?xml version="1.0" standalone="no"?>\n')
            f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n')
            f.write('"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
            f.write(ET.tostring(svg, encoding='unicode'))
            f.close()
        finally:
            if close and f is not None:
                f.close()
