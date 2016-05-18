#!/usr/bin/env python

from decimal import Decimal

import six


class DataType(object):
    """
    Base class for series data types.
    """
    @classmethod
    def infer(cls, v):
        if isinstance(v, Number.types):
            return Number
        elif isinstance(v, Text.types):
            return Text

        raise TypeError('No data type available for %s' % type(v))

class Number(DataType):
    """
    Data representing numbers.
    """
    types = (int, float, Decimal)

class Text(DataType):
    """
    Data representing text/strings.
    """
    types = six.string_types
