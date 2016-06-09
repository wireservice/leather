#!/usr/bin/env python

from decimal import Decimal

from leather.scales.base import Scale


class Ordinal(Scale):
    """
    A scale that maps individual values (e.g. strings) to a range.
    """
    def __init__(self, domain):
        seen = set()
        self._domain = [v for v in domain if v not in seen and not seen.add(v)]

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        range_min = Decimal(range_min)
        range_max = Decimal(range_max)

        segments = len(self._domain)
        segment_size = (range_max - range_min) / segments
        pos = range_min + (self._domain.index(value) * segment_size) + (segment_size / 2)

        return pos

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        range_min = Decimal(range_min)
        range_max = Decimal(range_max)

        segments = len(self._domain)
        segment_size = (range_max - range_min) / segments
        gap = segment_size / Decimal(20)

        a = range_min + (self._domain.index(value) * segment_size) + gap
        b = range_min + ((self._domain.index(value) + 1) * segment_size) - gap

        return (a, b)

    def ticks(self):
        """
        Generate a series of ticks for this scale.
        """
        return self._domain
