#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import leather


class TestBars(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Bars('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])
        self.rows = [
            (0, 'foo'),
            (None, None),
            (10, 'bing')
        ]

    def test_to_svg(self):
        series = leather.Series([
            (0, 'foo'),
            (5, 'bar'),
            (10, 'bing')
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series)
        rects = list(group)

        self.assertEqual(len(rects), 3)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 100)

    def test_nulls(self):
        series = leather.Series(self.rows, self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 0)

    def test_grouped(self):
        shape = leather.Bars(fill_color=['red', 'blue', 'green'], grouped=True)
        series = leather.Series([
            (0, 'foo'),
            (6, 'bar'),
            (5, 'bar'),
            (7, 'bar'),
            (3, 'bing'),
            (10, 'bing')
        ], shape)
        group = shape.to_svg(200, 100, self.linear, self.ordinal, series)

        base_series = leather.Series(self.rows, shape)
        base_group = self.shape.to_svg(200, 100, self.linear, self.ordinal, base_series)
        rects = list(group)
        base_rects = list(base_group)

        self.assertEqual(len(rects), 6)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 60)
        self.assertEqual(rects[1].get('fill'), 'blue')
        self.assertEqual(rects[5].get('y'), base_rects[1].get('y'))


class TestColumns(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Columns('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])

    def test_to_svg(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series)
        rects = list(group)

        self.assertEqual(len(rects), 3)
        self.assertEqual(float(rects[1].get('y')), 50)
        self.assertEqual(float(rects[1].get('height')), 50)

    def test_nulls(self):
        series = leather.Series([
            ('foo', 0),
            (None, None),
            ('bing', 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[1].get('y')), 0)
        self.assertEqual(float(rects[1].get('height')), 100)


class TestDots(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Dots('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])

    def test_linear(self):
        series = leather.Series([
            (0, 0),
            (5, 5),
            (10, 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series)
        circles = list(group)

        self.assertEqual(len(circles), 3)
        self.assertEqual(float(circles[1].get('cx')), 100)
        self.assertEqual(float(circles[1].get('cy')), 50)

    def test_ordinal(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series)
        circles = list(group)

        self.assertEqual(len(circles), 3)
        self.assertEqual(float(circles[1].get('cx')), 100)
        self.assertEqual(float(circles[1].get('cy')), 50)

    def test_nulls(self):
        series = leather.Series([
            (0, 0),
            (None, None),
            (10, 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series)
        circles = list(group)

        self.assertEqual(len(circles), 2)
        self.assertEqual(float(circles[1].get('cx')), 200)
        self.assertEqual(float(circles[1].get('cy')), 0)


class TestLines(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Lines('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])

    def test_linear(self):
        series = leather.Series([
            (0, 0),
            (5, 5),
            (10, 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series)
        paths = list(group)

        self.assertEqual(len(paths), 1)

    def test_ordinal(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series)
        paths = list(group)

        self.assertEqual(len(paths), 1)

    def test_nulls(self):
        series = leather.Series([
            (0, 0),
            (None, None),
            (10, 10)
        ], self.shape)

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series)
        paths = list(group)

        self.assertEqual(len(paths), 2)
