#!/usr/bin/env python

import os
import xml.etree.ElementTree as ET

import six

from leather.axis import Axis
from leather.scales.linear import LinearScale
from leather.scales.ordinal import OrdinalScale
from leather.series import Series
from leather.shapes.column import Column
from leather.shapes.dot import Dot
from leather.shapes.line import Line
from leather.utils import Box

DEFAULT_DOT = Dot()
DEFAULT_LINE = Line()
DEFAULT_COLUMN = Column()

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

    def add_dot(self, data, name=None, id=None, classes=None):
        """
        Shortcut method for adding a dotted series to the chart.
        """
        self.add_series(Series(data, name=name, id=id, classes=classes), DEFAULT_DOT)

    def add_line(self, data, name=None, id=None, classes=None):
        """
        Shortcut method for adding a line series to the chart.
        """
        self.add_series(Series(data, name=name, id=id, classes=classes), DEFAULT_LINE)

    def add_column(self, data, name=None, id=None, classes=None):
        """
        Shortcut method for adding a column series to the chart.
        """
        self.add_series(Series(data, name=name, id=id, classes=classes), DEFAULT_COLUMN)

    def _validate_dimension(self, scale, axis, orient, data_index):
        if not axis:
            if not scale:
                try:
                    data_min = 0
                    data_max = 0

                    for series, shape in self.layers:
                        sample = self.layers[0][0].data[0][data_index]

                        if not isinstance(sample, float) and not isinstance(sample, int):
                            raise ValueError()

                        for d in series.data:
                            data_min = min(data_min, d[data_index])
                            data_max = max(data_max, d[data_index])

                    scale = LinearScale([data_min, data_max])
                except ValueError:
                    scale_values = [d[0] for d in self.layers[0][0].data]

                    for series, shape in self.layers:
                        if [d[0] for d in series.data] != scale_values:
                            raise ValueError('Mismatched series scales')

                    scale = OrdinalScale(scale_values)
            else:
                scale = scale

            axis = Axis(scale, orient)
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

        x_scale, x_axis = self._validate_dimension(self.x_scale, self.x_axis, 'bottom', 0)
        y_scale, y_axis = self._validate_dimension(self.y_scale, self.y_axis, 'left', 1)

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
