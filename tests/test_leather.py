#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import six

import leather


class TestLinearScale(unittest.TestCase):
    def setUp(self):
        self.data1 = [
            (0, 3),
            (4, 5),
            (7, 9),
            (8, 4)
        ]

        self.data2 = [
            (0, 4),
            (1, 3),
            (2, 5),
            (5, 6),
            (9, 10)
        ]

        self.data3 = [
            (7, 2),
        ]

    def test_line(self):
        chart = leather.Chart()
        chart.add_lines(self.data1)
        chart.add_lines(self.data2)
        chart.add_lines(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_dot(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)
        chart.add_dots(self.data2)
        chart.add_dots(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_column(self):
        chart = leather.Chart()
        chart.add_columns(self.data1)
        chart.add_columns(self.data2)
        chart.add_columns(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_mixed(self):
        chart = leather.Chart()
        chart.add_lines(self.data1)
        chart.add_dots(self.data2)
        chart.add_columns(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_force_scale(self):
        data = [
            (1, 2),
            (3, 1),
            (5, 1),
            (9, 5)
        ]

        chart = leather.Chart()
        chart.set_x_scale(leather.LinearScale(0, 20))
        chart.add_lines(data)
        chart.add_dots(data)
        chart.add_columns(data)

        output = six.StringIO()
        chart.to_svg(output)


class TestOrdinalScale(unittest.TestCase):
    def setUp(self):
        self.data1 = [
            ('foo', 3),
            ('bing', 5),
            ('baz', 9),
            ('blurg', 4)
        ]

        self.data2 = [
            ('foo', 7),
            ('bing', 2),
            ('baz', 3),
            ('blurg', 4)
        ]

        self.data3 = [
            ('foo', 2),
            ('bing', 1),
            ('baz', 1),
            ('blurg', 5)
        ]

    def test_line(self):
        chart = leather.Chart()
        chart.add_lines(self.data1)
        chart.add_lines(self.data2)
        chart.add_lines(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_dot(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)
        chart.add_dots(self.data2)
        chart.add_dots(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_column(self):
        chart = leather.Chart()
        chart.add_columns(self.data1)
        chart.add_columns(self.data2)
        chart.add_columns(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_mixed(self):
        chart = leather.Chart()
        chart.add_lines(self.data1)
        chart.add_dots(self.data2)
        chart.add_columns(self.data3)

        output = six.StringIO()
        chart.to_svg(output)
