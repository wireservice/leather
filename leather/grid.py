#!/usr/bin/env python

import math
import os
import xml.etree.ElementTree as ET

import six

import leather.svg as svg
from leather import theme


class Grid(object):
    """
    A grid of charts rendered together.
    """
    def __init__(self):
        self._charts = []

    def add_chart(self, chart):
        """
        Add a chart to the grid.
        """
        self._charts.append(chart)

    def to_svg(self, path, width=None, height=None):
        """
        Render the grid to an SVG.
        """
        if not width or not height:
            count = len(self._charts)

            columns = math.ceil(math.sqrt(count))
            rows = math.ceil(count / columns)

            width = columns * theme.default_width
            height = rows * theme.default_height

        root = ET.Element('svg',
            width=six.text_type(width),
            height=six.text_type(height),
            version='1.1',
            xmlns='http://www.w3.org/2000/svg'
        )

        chart_count = len(self._charts)
        grid_width = math.ceil(math.sqrt(chart_count))
        grid_height = math.ceil(chart_count / grid_width)
        chart_width = width / grid_width
        chart_height = height / grid_height

        for i, chart in enumerate(self._charts):
            x = (i % grid_width) * chart_width
            y = math.floor(i / grid_width) * chart_height

            group = ET.Element('g')
            group.set('transform', svg.translate(x, y))

            chart = chart.to_svg_group(chart_width, chart_height)
            group.append(chart)

            root.append(group)

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

            f.write(svg.HEADER)
            f.write(ET.tostring(root, encoding='unicode'))
            f.close()
        finally:
            if close and f is not None:
                f.close()
