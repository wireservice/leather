#!/usr/bin/env python

from leather.renderable import Renderable

class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, scale, ticks=5, tick_size=8, color='black'):
        self.scale = scale
        self.ticks = ticks
        self.tick_size = tick_size
        self.color = color

    def to_svg(self):
        raise NotImplementedError()
