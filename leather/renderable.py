#!/usr/bin/env python

class Renderable(object):
    """
    Abstract base class for renderable chart elements.
    """
    def to_svg(self, width, height):
        raise NotImplementedError()
