#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.renderable import Renderable

class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, scale, orient='bottom', ticks=5, tick_width='1px', tick_size=4, tick_color='#eee', label_color='#9c9c9c', zero_color='#a8a8a8'):
        self.scale = scale
        self.orient = orient
        self.ticks = ticks
        self.tick_width = tick_width
        self.tick_size = tick_size
        self.tick_color = tick_color
        self.label_color = label_color
        self.zero_color = zero_color

    def to_svg(self, bbox):
        group = ET.Element('g')

        if self.orient == 'left':
            label_x = bbox.left - (self.tick_size * 2)
            x1 = bbox.left - self.tick_size
            x2 = bbox.right
            project_range = [bbox.bottom, bbox.top]
        elif self.orient == 'bottom':
            label_y = bbox.bottom + (self.tick_size * 2)
            y1 = bbox.top
            y2 = bbox.bottom + self.tick_size
            project_range = [bbox.left, bbox.right]

        for value in self.scale.ticks(self.ticks):
            projected_value = self.scale.project(value, project_range)

            if value == 0:
                tick_color = self.zero_color
            else:
                tick_color = self.tick_color

            if self.orient == 'left':
                y1 = projected_value
                y2 = projected_value

            elif self.orient == 'bottom':
                x1 = projected_value
                x2 = projected_value

            tick = ET.Element('line',
                x1=six.text_type(x1),
                y1=six.text_type(y1),
                x2=six.text_type(x2),
                y2=six.text_type(y2),
                stroke=tick_color
            )

            tick.set('stroke-width', self.tick_width)

            if self.orient == 'left':
                x = label_x
                y = projected_value
                dy = '0.32em'
                text_anchor = 'end'
            elif self.orient == 'bottom':
                x = projected_value
                y = label_y
                dy = '1em'
                text_anchor = 'middle'

            label = ET.Element('text',
                x=six.text_type(x),
                y=six.text_type(y),
                dy=dy,
                fill=self.label_color
            )

            label.set('text-anchor', text_anchor)
            label.text = six.text_type(value)

            group.append(tick)
            group.append(label)

        return group
