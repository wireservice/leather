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
        label_x = bbox.left - (self.tick_size * 2)
        x1 = bbox.left - self.tick_size
        x2 = bbox.right

        for value in range(self.scale.domain[0], self.scale.domain[1] + tick_increment, tick_increment):
            y = self.scale.project(value, [bbox.bottom, bbox.top])

            if value == self.scale.domain[0]:
                tick_color = self.edge_color
            else:
                tick_color = self.tick_color

            tick = ET.Element('line',
                x1=six.text_type(x1),
                y1=six.text_type(y),
                x2=six.text_type(x2),
                y2=six.text_type(y),
                stroke=tick_color,
            )
            tick.set('stroke-width', self.tick_width)

            label = ET.Element('text',
                x=six.text_type(label_x),
                y=six.text_type(y),
                dy='0.32em',
                fill=self.label_color
            )
            label.set('text-anchor', 'end')
            label.text = six.text_type(value)

            group.append(tick)
            group.append(label)

        return group
