#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.axes.base import Axis

class XAxis(Axis):
    """
    A horizontal or vertical chart axis.
    """
    def to_svg(self, bbox):
        return ET.Element('line',
            x1=six.text_type(bbox.left),
            y1=six.text_type(bbox.top),
            x2=six.text_type(bbox.left),
            y2=six.text_type(bbox.bottom),
            stroke='black'
        )
