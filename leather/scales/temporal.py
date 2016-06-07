#!/usr/bin/env python

from datetime import datetime

import six

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
        numerator = value - self._min
        denominator = self._max - self._min

        # Python 2 does not support timedelta division
        if six.PY2:
            if isinstance(self._min, datetime):
                numerator = numerator.total_seconds()
                denominator = denominator.total_seconds()
            else:
                numerator = float(numerator.days)
                denominator = float(denominator.days)

        pos = numerator / denominator

        return ((range_max - range_min) * pos) + range_min

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        raise NotImplementedError

    def ticks(self):
        """
        Generate a series of ticks for this scale.
        """
        count = 5
        size = (self._max - self._min) / (count - 1)

        return [self._min + (size * i) for i in range(count)]
