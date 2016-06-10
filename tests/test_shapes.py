#!/usr/bin/env python

import leather


class TestBars(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.Bars('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])
        self.palette = (color for color in ['red', 'white', 'blue'])

    def test_to_svg(self):
        series = leather.Series([
            (0, 'foo'),
            (5, 'bar'),
            (10, 'bing')
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 3)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 100)

    def test_nulls(self):
        series = leather.Series([
            (0, 'foo'),
            (None, None),
            (10, 'bing')
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 0)


class TestColumns(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.Columns('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])
        self.palette = (color for color in ['red', 'white', 'blue'])

    def test_to_svg(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ])

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 3)
        self.assertEqual(float(rects[1].get('y')), 50)
        self.assertEqual(float(rects[1].get('height')), 50)

    def test_nulls(self):
        series = leather.Series([
            ('foo', 0),
            (None, None),
            ('bing', 10)
        ])

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[1].get('y')), 0)
        self.assertEqual(float(rects[1].get('height')), 100)


class TestDots(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.Dots('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])
        self.palette = (color for color in ['red', 'white', 'blue'])

    def test_linear(self):
        series = leather.Series([
            (0, 0),
            (5, 5),
            (10, 10)
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series, self.palette)
        circles = list(group)

        self.assertEqual(len(circles), 3)
        self.assertEqual(float(circles[1].get('cx')), 100)
        self.assertEqual(float(circles[1].get('cy')), 50)

    def test_ordinal(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ])

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series, self.palette)
        circles = list(group)

        self.assertEqual(len(circles), 3)
        self.assertEqual(float(circles[1].get('cx')), 100)
        self.assertEqual(float(circles[1].get('cy')), 50)

    def test_nulls(self):
        series = leather.Series([
            (0, 0),
            (None, None),
            (10, 10)
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series, self.palette)
        circles = list(group)

        self.assertEqual(len(circles), 2)
        self.assertEqual(float(circles[1].get('cx')), 200)
        self.assertEqual(float(circles[1].get('cy')), 0)


class TestLine(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.Line('red')
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['foo', 'bar', 'bing'])
        self.palette = (color for color in ['red', 'white', 'blue'])

    def test_linear(self):
        series = leather.Series([
            (0, 0),
            (5, 5),
            (10, 10)
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series, self.palette)
        paths = list(group)

        self.assertEqual(len(paths), 1)

    def test_ordinal(self):
        series = leather.Series([
            ('foo', 0),
            ('bar', 5),
            ('bing', 10)
        ])

        group = self.shape.to_svg(200, 100, self.ordinal, self.linear, series, self.palette)
        paths = list(group)

        self.assertEqual(len(paths), 1)

    def test_nulls(self):
        series = leather.Series([
            (0, 0),
            (None, None),
            (10, 10)
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.linear, series, self.palette)
        paths = list(group)

        self.assertEqual(len(paths), 2)

class TestGroupedBars(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.GroupedBars()
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['first', 'second', 'third'])
        self.palette = (color for color in ['red', 'white', 'blue'])
        self.rows = [
            (1, 'foo', 'first'),
            (5, 'bar', 'first'),
            (7, 'foo', 'second'),
            (4, 'bing', 'second'),
            (7, 'foo', 'third'),
            (3, 'bar', 'third'),
            (4, 'buzz', 'third')
        ]

    def test_to_svg(self):
        series = leather.CategorySeries(self.rows)

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 7)
        self.assertEqual(float(rects[1].get('x')), 0)
        self.assertEqual(float(rects[1].get('width')), 100)
        self.assertEqual(rects[1].get('fill'), 'white')

    def test_invalid_fill_color(self):
        series = leather.CategorySeries(self.rows)

        with self.assertRaises(ValueError):
            group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, ['one', 'two'])

        with self.assertRaises(ValueError):
            shape = leather.GroupedBars('red')

    def test_nulls(self):
        series = leather.CategorySeries([
            (0, 'foo', 'first'),
            (None, None, None),
            (10, 'bing', 'third')
        ])

        group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[0].get('x')), 0)
        self.assertEqual(float(rects[0].get('width')), 0)
