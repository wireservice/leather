#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import leather


class TestBars(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Bars()
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])

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


class TestColumns(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Columns()
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


class TestDots(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Dots()
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


class TestLines(unittest.TestCase):
    def setUp(self):
        self.shape = leather.Lines()
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
