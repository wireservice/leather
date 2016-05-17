#!/usr/bin/env python

from leather.renderable import Renderable

class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, scale, ticks=5, tick_width='1px', tick_size=4, tick_color='#eee', label_color='#9c9c9c', edge_color='#a8a8a8'):
        self.scale = scale
        self.ticks = ticks
        self.tick_width = tick_width
        self.tick_size = tick_size
        self.tick_color = tick_color
        self.label_color = label_color
        self.edge_color = edge_color

    def to_svg(self):
        raise NotImplementedError()
