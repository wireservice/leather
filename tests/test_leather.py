#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import six

import leather

dot_data = [
    ('foo', 3),
    ('bing', 5),
    ('baz', 9),
    ('blurg', 4)
]

line_data = [
    ('foo', 7),
    ('bing', 2),
    ('baz', 3),
    ('blurg', 4)
]

chart = leather.Chart()
chart.add_column(line_data)
chart.add_dot(dot_data)
chart.to_svg('test.svg')

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
        chart.add_line(self.data1)
        chart.add_line(self.data2)
        chart.add_line(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_dot(self):
        chart = leather.Chart()
        chart.add_dot(self.data1)
        chart.add_dot(self.data2)
        chart.add_dot(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_column(self):
        chart = leather.Chart()
        chart.add_column(self.data1)
        chart.add_column(self.data2)
        chart.add_column(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_mixed(self):
        chart = leather.Chart()
        chart.add_line(self.data1)
        chart.add_dot(self.data2)
        chart.add_column(self.data3)

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
        chart.add_line(self.data1)
        chart.add_line(self.data2)
        chart.add_line(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_dot(self):
        chart = leather.Chart()
        chart.add_dot(self.data1)
        chart.add_dot(self.data2)
        chart.add_dot(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_column(self):
        chart = leather.Chart()
        chart.add_column(self.data1)
        chart.add_column(self.data2)
        chart.add_column(self.data3)

        output = six.StringIO()
        chart.to_svg(output)

    def test_mixed(self):
        chart = leather.Chart()
        chart.add_line(self.data1)
        chart.add_dot(self.data2)
        chart.add_column(self.data3)

        output = six.StringIO()
        chart.to_svg(output)
