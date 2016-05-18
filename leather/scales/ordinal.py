#!/usr/bin/env python

from leather.scales.base import Scale

class OrdinalScale(Scale):
    """
    A scale that maps individual values to a range.
    """
    def __init__(self, domain):
        self.domain = domain

    def project(self, value, target_range):
        """
        Project a value to a point in the given range.
        """
        segments = len(self.domain)
        segment_size = (target_range[1] - target_range[0]) / segments
        pos = target_range[0] + (self.domain.index(value) * segment_size) + (segment_size / 2)

        return pos

    def project_interval(self, value, target_range):
        """
        Project a value to a segment of the given range (for columns/bars).
        """
        segments = len(self.domain)
        segment_size = (target_range[1] - target_range[0]) / segments
        gap = segment_size * 0.05

        a = target_range[0] + (self.domain.index(value) * segment_size) + gap
        b = target_range[0] + ((self.domain.index(value) + 1) * segment_size) - gap

        return (a, b)

    def ticks(self, count):
        """
        Return a sequence of ticks for this scale. This will always be the
        complete domain, regardless of :code:`count`.
        """
        return self.domain
