#!/usr/bin/env python

import math
import os
import xml.etree.ElementTree as ET

import six

from leather.utils import svg_translate


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

    def to_svg(self, path, width=1200, height=1200):
        """
        Render the grid to an SVG.
        """
        svg = ET.Element('svg',
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
            group.set('transform', svg_translate(x, y))

            chart = chart.to_svg_group(chart_width, chart_height)
            group.append(chart)
            
            svg.append(group)

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
