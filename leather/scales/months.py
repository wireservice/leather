#!/usr/bin/env python

from datetime import datetime, date
import math

from leather.scales.temporal import Temporal


def to_month_count(d):
    return (d.year * 12) + d.month


class Months(Temporal):
    """
    A scale that maps years and months to a coordinate range.

    This scale takes dates and datetimes, but treats them as ordinal values for
    purposes of projection. Thus you can use this scale to render
    :class:`.Bars` or :class:`.Columns` for yearly data.

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

        raise ValueError('Unsupported domain value for Annual scale.')

    def project(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to a target range.
        """
        d = self._value_as_date(value)

        segments = to_month_count(self._max) - to_month_count(self._min) + 1
        segment_size = float(range_max - range_min) / segments

        pos = to_month_count(d) - to_month_count(self._min)

        return range_min + ((pos + 0.5) * segment_size)

    def project_interval(self, value, range_min, range_max):
        """
        Project a value in this scale's domain to an interval in the target
        range. This is used for places :class:`.Bars` and :class:`.Columns`.
        """
        d = self._value_as_date(value)

        segments = to_month_count(self._max) - to_month_count(self._min) + 1
        segment_size = float(range_max - range_min) / segments
        gap = segment_size * 0.05

        pos = to_month_count(d) - to_month_count(self._min)
        a = pos
        b = pos

        if pos >= 0:
            b += 1
        else:
            a -= 1

        a = range_min + (a * segment_size) + gap
        b = range_min + (b * segment_size) - gap

        return (a, b)

    def ticks(self):
        """
        Generate a series of ticks for this scale.
        """
        count = 5
        a = to_month_count(self._min)
        b = to_month_count(self._max)

        size = int(math.ceil(float(b - a) / (count - 1)))
        values = []

        for i in range(count):
            month_count = a + (size * i)
            years = month_count // 12
            months = month_count % 12

            values.append(date(years, months, 1))

        return values

    def format_tick(self, value, i, count):
        """
        Display only year component.
        """
        return '%i-%i' % (value.year, value.month + 1)
