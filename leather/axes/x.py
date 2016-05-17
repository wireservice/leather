#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.axes.base import Axis

class XAxis(Axis):
    """
    A horizontal or vertical chart axis.
    """
    def to_svg(self, bbox):
        group = ET.Element('g')

        tick_increment = int((self.scale.domain[1] - self.scale.domain[0]) / self.ticks)
        label_x = bbox.left - self.tick_size
        x1 = bbox.left - (self.tick_size / 2)
        x2 = bbox.left + (self.tick_size / 2)

        for value in range(self.scale.domain[0], self.scale.domain[1], tick_increment):
            y = self.scale.project(value, [bbox.bottom, bbox.top])

            tick = ET.Element('line',
                x1=six.text_type(x1),
                y1=six.text_type(y),
                x2=six.text_type(x2),
                y2=six.text_type(y),
                stroke=self.color
            )

            label = ET.Element('text',
                x=six.text_type(label_x),
                y=six.text_type(y),
                fill=self.color
            )
            label.set('text-anchor', 'end')
            label.set('dominant-baseline', 'middle')
            label.text = six.text_type(value)

            group.append(tick)
            group.append(label)

        group.append(ET.Element('line',
            x1=six.text_type(bbox.left),
            y1=six.text_type(bbox.top),
            x2=six.text_type(bbox.left),
            y2=six.text_type(bbox.bottom),
            stroke=self.color
        ))

        return group
