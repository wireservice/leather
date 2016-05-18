#!/usr/bin/env python

import os
import xml.etree.ElementTree as ET

import six

from leather.axis import Axis
from leather.data_types import Number, Text
from leather.scales.linear import LinearScale
from leather.scales.ordinal import OrdinalScale
from leather.series import Series
from leather.shapes.column import Column
from leather.shapes.dot import Dot
from leather.shapes.line import Line
from leather.utils import X, Y, DIMENSIONS, Box

DEFAULT_DOT = Dot()
DEFAULT_LINE = Line()
DEFAULT_COLUMN = Column()

class Chart(object):
    """
    Container for all chart types.
    """
    def __init__(self, width=800, height=400):
        self._width = width
        self._height = height
        self._margin = Box(
            top=20,
            right=20,
            bottom=20,
            left=20
        )

        self._layers = []
        self._types = [None, None]
        self._scales = [None, None]
        self._axes = [None, None]

    def add_series(self, series, shape):
        """
        Add a data :class:`.Series` to the chart.
        """
        for dim in DIMENSIONS:
            if not self._types[dim]:
                self._types[dim] = series.types[dim]
            elif series.types[dim] is not self._types[dim]:
                raise TypeError('Can\'t mix axis-data types: %s and %s' % (series.types[dim], self._types[dim]))

        self._layers.append((series, shape))

    def add_dot(self, data, name=None):
        """
        Shortcut method for adding a dotted series to the chart.
        """
        self.add_series(Series(data, name=name), DEFAULT_DOT)

    def add_line(self, data, name=None):
        """
        Shortcut method for adding a line series to the chart.
        """
        self.add_series(Series(data, name=name), DEFAULT_LINE)

    def add_column(self, data, name=None):
        """
        Shortcut method for adding a column series to the chart.
        """
        self.add_series(Series(data, name=name), DEFAULT_COLUMN)

    def _validate_dimension(self, dimension):
        """
        Validates that the given scale and axis are valid for the data that
        has been added to this chart. If a scale or axis has not been set,
        generates automated ones.
        """
        scale = self._scales[dimension]
        axis = self._axes[dimension]
        data_type = self._types[dimension]

        if not axis:
            if not scale:
                # Default Number scale is Linear
                if data_type is Number:
                    data_min = min([series.min(dimension) for series, shape in self._layers])
                    data_max = max([series.max(dimension) for series, shape in self._layers])

                    scale = LinearScale([data_min, data_max])
                # Default Text scale is Ordinal
                elif data_type is Text:
                    scale_values = None

                    for series, shape in self._layers:
                        if not scale_values:
                            scale_values = series.values(dimension)
                            continue

                        if series.values(dimension) != scale_values:
                            raise ValueError('Mismatched series scales')

                    scale = OrdinalScale(scale_values)
            else:
                scale = scale

            if dimension == X:
                orient = 'bottom'
            elif dimension == Y:
                orient = 'left'

            axis = Axis(scale, orient)
        # Verify data are within bounds
        else:
            pass

        return (scale, axis)

    def to_svg(self, path):
        """
        Render this chart to an SVG document.

        :param path:
            Filepath or file-like object to write to.
        """
        if not self._layers:
            raise ValueError('You must add at least one series to the chart before rendering.')

        canvas_bbox = Box(
            top=self._margin.top,
            right=self._width - self._margin.right,
            bottom=self._height - self._margin.bottom,
            left=self._margin.left
        )

        x_scale, x_axis = self._validate_dimension(X)
        y_scale, y_axis = self._validate_dimension(Y)

        svg = ET.Element('svg',
            width=six.text_type(self._width),
            height=six.text_type(self._height),
            version='1.1',
            xmlns='http://www.w3.org/2000/svg'
        )

        svg.append(x_axis.to_svg(canvas_bbox))
        svg.append(y_axis.to_svg(canvas_bbox))

        for series, shape in self._layers:
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
