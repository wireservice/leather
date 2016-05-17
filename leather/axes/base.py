#!/usr/bin/env python

from leather.renderable import Renderable

class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, scale, orient='bottom', ticks=5, tick_width='1px', tick_size=4, tick_color='#eee', label_color='#9c9c9c', edge_color='#a8a8a8'):
        self.scale = scale
        self.orient = orient
        self.ticks = ticks
        self.tick_width = tick_width
        self.tick_size = tick_size
        self.tick_color = tick_color
        self.label_color = label_color
        self.edge_color = edge_color

    def to_svg(self, bbox):
        group = ET.Element('g')

        if self.orient == 'bottom':
            label_x = bbox.left - (self.tick_size * 2)
            x1 = bbox.left - self.tick_size
            x2 = bbox.right
        elif self.orient == 'left':
            label_y = bbox.bottom + (self.tick_size * 2)
            y1 = bbox.top
            y2 = bbox.bottom + self.tick_size

        for value in self.scale.ticks(self.ticks):
            projected_value = self.scale.project(value, [bbox.bottom, bbox.top])

            if value == self.scale.domain[0]:
                tick_color = self.edge_color
            else:
                tick_color = self.tick_color

            if self.orient == 'bottom':
                tick = ET.Element('line',
                    x1=six.text_type(x1),
                    y1=six.text_type(projected_value),
                    x2=six.text_type(x2),
                    y2=six.text_type(projected_value),
                    stroke=tick_color,
                )
            elif self.orient == 'left':
                tick = ET.Element('line',
                    x1=six.text_type(projected_value),
                    y1=six.text_type(y1),
                    x2=six.text_type(projected_value),
                    y2=six.text_type(y2),
                    stroke=tick_color
                )

            tick.set('stroke-width', self.tick_width)

            if self.orient == 'bottom':
                label = ET.Element('text',
                    x=six.text_type(label_x),
                    y=six.text_type(y),
                    dy='0.32em',
                    fill=self.label_color
                )
            elif self.orient == 'left':
                label = ET.Element('text',
                    x=six.text_type(x),
                    y=six.text_type(label_y),
                    dy='1em',
                    fill=self.label_color
                )

            label.set('text-anchor', 'end')
            label.text = six.text_type(value)

            group.append(tick)
            group.append(label)

        return group
