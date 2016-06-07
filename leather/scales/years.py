#!/usr/bin/env python

from datetime import datetime, date
from decimal import Decimal
import math

from leather.scales.temporal import Temporal


class Years(Temporal):
    """
    A scale that maps years to a coordinate range.

    This scale takes linear values (dates, datetimes, or numbers), but treats
    them as ordinal values for purposes of projection. Thus you can use this
    scale to render :class:`.Bars` or :class:`.Columns` for yearly data.

    :param domain_min:
        The minimum value of the domain.
    :param domain_max:
        The maximum value of the domain.
    """
    def __init__(self, domain_min, domain_max):
        self._min = self._value_as_date(domain_min)
        self._max = self._value_as_date(domain_max)

    def _value_as_date(self, value):
        """
        Convert a date or number to a date for consistent logic.
        """
        if isinstance(value, (datetime, date)):
            return value
        elif isinstance(value, (int, float, Decimal)):
            return date(value, 1, 1)

        raise ValueError('Unsupported domain value for Annual scale.')

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        d = self._value_as_date(value)

        segments = self._max.year - self._min.year + 1
        segment_size = (range_max - range_min) / segments

        pos = d.year - self._min.year

        if pos >= 0:
            pos += 0.5
        else:
            pos -= 0.5

        return range_min + (pos * segment_size)

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        d = self._value_as_date(value)

        segments = self._max.year - self._min.year + 1
        segment_size = (range_max - range_min) / segments
        gap = segment_size * 0.05

        pos = d.year - self._min.year

        a = range_min + ((pos) * segment_size) + gap
        b = range_min + ((pos + 1) * segment_size) - gap

        return (a, b)

    def ticks(self):
        """
        Generate a series of ticks for this scale.
        """
        count = 5
        size = int(math.ceil(float(self._max.year - self._min.year) / count))
        values = []

        for i in range(count):
            years = self._min.year + (i * size)

            values.append(date(years, 1, 1))

        return values

    def format_tick(self, value, i, count):
        """
        Display only year component.
        """
        return value.year
