#!/usr/bin/env python

from decimal import Decimal

from leather.scales.base import Scale


class Linear(Scale):
    """
    A scale that linearly maps values from a domain to a range.

    :param domain_min:
        The minimum value of the input domain.
    :param domain_max:
        The maximum value of the input domain.
    """
    def __init__(self, domain_min, domain_max):
        self._min = Decimal(domain_min)
        self._max = Decimal(domain_max)

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        value = Decimal(value)
        range_min = Decimal(range_min)
        range_max = Decimal(range_max)

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
