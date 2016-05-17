#!/usr/bin/env python

from leather.renderable import Renderable

class Axis(Renderable):
    """
    A horizontal or vertical chart axis.
    """
    def __init__(self, scale, ticks=None):
        self.scale = scale
        self.ticks = None

    def to_svg(self):
        raise NotImplementedError()
