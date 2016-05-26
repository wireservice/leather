#!/usr/bin/env python

from datetime import datetime, date

from leather.scales.temporal import Temporal


class Annual(Temporal):
    """
    A scale that maps years to a pixel range.

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
        elif isinstance(value, (int, float)):
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

        return range_min + ((pos + 0.5) * segment_size)

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

    def ticks(self, count):
        """
        Generate a series of ticks for this scale.
        """
        return [date(year, 1, 1) for year in range(self._min.year, self._max.year + 1)]

    def format_tick(self, value, i, count):
        """
        Display only year component.
        """
        return value.year
