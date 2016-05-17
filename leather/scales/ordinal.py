#!/usr/bin/env python

from leather.scales.base import Scale

class OrdinalScale(Scale):
    """
    A scale that maps individual values to a range.
    """
    def __init__(self, domain):
        self.domain = domain

    def project(self, value, range):
        """
        Project a value to a point in the given range.
        """
        segments = len(self.domain)
        segment_size = (range[1] - range[0]) / segments
        pos = range[0] + (self.domain.index(value) * segment_size) + (segment_size / 2)

        return pos

    def project_interval(self, value, range):
        segments = len(self.domain)
        segment_size = (range[1] - range[0]) / segments
        gap = segment_size * 0.05

        a = range[0] + (self.domain.index(value) * segment_size) + gap
        b = range[0] + ((self.domain.index(value) + 1) * segment_size) - gap

        return (a, b)

    def ticks(self, count):
        return self.domain
