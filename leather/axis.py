#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.renderable import Renderable


class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, orient='bottom', ticks=5, tick_width='1px', tick_size=4, tick_color='#eee', label_color='#9c9c9c', zero_color='#a8a8a8'):
        self.ticks = ticks
        self.tick_width = tick_width
        self.tick_size = tick_size
        self.tick_color = tick_color
        self.label_color = label_color
        self.zero_color = zero_color

    def to_svg(self, width, height, scale, orient):
        """
        Render this axis to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'axis ' + orient)

        if orient == 'left':
            label_x = -(self.tick_size * 2)
            x1 = -self.tick_size
            x2 = width
            range_min = height
            range_max = 0
        elif orient == 'bottom':
            label_y = height + (self.tick_size * 2)
            y1 = 0
            y2 = height + self.tick_size
            range_min = 0
            range_max = width

        for value in scale.ticks(self.ticks):
            tick_group = ET.Element('g')
            tick_group.set('class', 'tick')

            projected_value = scale.project(value, range_min, range_max)

            if value == 0:
                tick_color = self.zero_color
            else:
                tick_color = self.tick_color

            if orient == 'left':
                y1 = projected_value
                y2 = projected_value

            elif orient == 'bottom':
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

            if orient == 'left':
                x = label_x
                y = projected_value
                dy = '0.32em'
                text_anchor = 'end'
            elif orient == 'bottom':
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

            tick_group.append(tick)
            tick_group.append(label)

            group.append(tick_group)

        return group
