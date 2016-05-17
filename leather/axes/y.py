#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.axes.base import Axis

class YAxis(Axis):
    """
    A horizontal or vertical chart axis.
    """
    def to_svg(self, bbox):
        group = ET.Element('g')

        tick_increment = int((self.scale.domain[1] - self.scale.domain[0]) / self.ticks)
        label_y = bbox.bottom + self.tick_size
        y1 = bbox.bottom - (self.tick_size / 2)
        y2 = bbox.bottom + (self.tick_size / 2)

        for value in range(self.scale.domain[0], self.scale.domain[1], tick_increment):
            x = self.scale.project(value, [bbox.left, bbox.right])

            tick = ET.Element('line',
                x1=six.text_type(x),
                y1=six.text_type(y1),
                x2=six.text_type(x),
                y2=six.text_type(y2),
                stroke='black'
            )

            label = ET.Element('text',
                x=six.text_type(x),
                y=six.text_type(label_y),
                fill=self.color
            )
            label.set('text-anchor', 'middle')
            label.set('dominant-baseline', 'hanging')
            label.text = six.text_type(value)

            group.append(tick)
            group.append(label)

        group.append(ET.Element('line',
            x1=six.text_type(bbox.left),
            y1=six.text_type(bbox.bottom),
            x2=six.text_type(bbox.right),
            y2=six.text_type(bbox.bottom),
            stroke='black'
        ))

        return group
