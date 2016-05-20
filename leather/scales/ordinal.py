#!/usr/bin/env python

from leather.scales.base import Scale

class Ordinal(Scale):
    """
    A scale that maps individual values (e.g. strings) to a range.
    """
    def __init__(self, domain):
        self.domain = domain

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        segments = len(self.domain)
        segment_size = float(range_max - range_min) / segments
        pos = range_min + (self.domain.index(value) * segment_size) + (segment_size / 2)

        return pos

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        segments = len(self.domain)
        segment_size = (range_max - range_min) / segments
        gap = segment_size * 0.05

        a = range_min + (self.domain.index(value) * segment_size) + gap
        b = range_min + ((self.domain.index(value) + 1) * segment_size) - gap

        return (a, b)

    def ticks(self, count):
        """
        Generate a series of ticks for this scale.
        """
        return self.domain
