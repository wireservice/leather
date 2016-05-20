#!/usr/bin/env python

from datetime import date, datetime, time

from leather.scales.base import Scale


class Temporal(Scale):
    """
    A scale that linearly maps date/datetime values from a domain to a range.

    :param domain_min:
        The minimum date/datetime of the input domain.
    :param domain_max:
        The maximum date/datetime of the input domain.
    """
    def __init__(self, domain_min, domain_max):
        self._min = domain_min
        self._max = domain_max

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        pos = (value - self._min) / (self._max - self._min)

        return ((range_max - range_min) * pos) + range_min

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        raise NotImplementedError

    def ticks(self, count):
        """
        Generate a series of ticks for this scale.
        """
        size = (self._max - self._min) / (count - 1)

        return [self._min + (size * i) for i in range(count)]
