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

    def test_zeros(self):
        series = leather.Series([
            (0, 'foo'),
            (0, None),
            (0, 'bing')
        ])

        linear = leather.Linear(0, 0)

        group = self.shape.to_svg(200, 100, linear, self.ordinal, series, self.palette)
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
        self.palette = (color for color in ['red', 'white', 'blue', 'yellow'])
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
        self.assertEqual(float(rects[3].get('y')), 36)
        self.assertEqual(float(rects[3].get('height')), 14)
        self.assertEqual(rects[1].get('fill'), 'white')

    def test_invalid_fill_color(self):
        series = leather.CategorySeries(self.rows)

        with self.assertRaises(ValueError):
            group = self.shape.to_svg(200, 100, self.linear, self.ordinal, series, ['one', 'two'])

        with self.assertRaises(ValueError):
            shape = leather.GroupedBars('red')
            shape.to_svg(100, 100, self.linear, self.ordinal, series, self.palette)

    def test_style_function(self):
        def color_code(d):
            if d.y == 'foo':
                return 'green'
            else:
                return 'black'

        shape = leather.GroupedBars(color_code)
        series = leather.CategorySeries(self.rows)

        group = shape.to_svg(200, 100, self.linear, self.ordinal, series, self.palette)
        rects = list(group)

        self.assertEqual(rects[0].get('fill'), 'green')
        self.assertEqual(rects[1].get('fill'), 'black')
        self.assertEqual(rects[2].get('fill'), 'green')
        self.assertEqual(rects[3].get('fill'), 'black')
        self.assertEqual(rects[4].get('fill'), 'green')

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

class TestGroupedColumns(leather.LeatherTestCase):
    def setUp(self):
        self.shape = leather.GroupedColumns()
        self.linear = leather.Linear(0, 10)
        self.ordinal = leather.Ordinal(['first', 'second', 'third'])
        self.palette = (color for color in ['red', 'white', 'blue', 'yellow'])
        self.rows = [
            ('foo', 1, 'first'),
            ('bar', 5, 'first'),
            ('foo', 7, 'second'),
            ('bing', 4, 'second'),
            ('foo', 7, 'third'),
            ('bar', 3, 'third'),
            ('buzz', 4, 'third')
        ]

    def test_to_svg(self):
        series = leather.CategorySeries(self.rows)

        group = self.shape.to_svg(100, 200, self.ordinal, self.linear, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 7)
        self.assertEqual(float(rects[1].get('y')), 100)
        self.assertEqual(float(rects[1].get('height')), 100)
        self.assertEqual(float(rects[3].get('x')), 50)
        self.assertEqual(float(rects[3].get('width')), 16)
        self.assertEqual(rects[1].get('fill'), 'white')

    def test_invalid_fill_color(self):
        series = leather.CategorySeries(self.rows)

        with self.assertRaises(ValueError):
            group = self.shape.to_svg(100, 200, self.ordinal, self.linear, series, ['one', 'two'])

        with self.assertRaises(ValueError):
            shape = leather.GroupedColumns('red')
            shape.to_svg(100, 100, self.ordinal, self.linear, series, self.palette)

    def test_style_function(self):
        def color_code(d):
            if d.x == 'foo':
                return 'green'
            else:
                return 'black'

        shape = leather.GroupedColumns(color_code)
        series = leather.CategorySeries(self.rows)

        group = shape.to_svg(100, 200, self.ordinal, self.linear, series, self.palette)
        rects = list(group)

        self.assertEqual(rects[0].get('fill'), 'green')
        self.assertEqual(rects[1].get('fill'), 'black')
        self.assertEqual(rects[2].get('fill'), 'green')
        self.assertEqual(rects[3].get('fill'), 'black')
        self.assertEqual(rects[4].get('fill'), 'green')

    def test_nulls(self):
        series = leather.CategorySeries([
            ('foo', 0, 'first'),
            (None, None, None),
            ('bing', 10, 'third')
        ])

        group = self.shape.to_svg(100, 200, self.ordinal, self.linear, series, self.palette)
        rects = list(group)

        self.assertEqual(len(rects), 2)
        self.assertEqual(float(rects[1].get('y')), 0)
        self.assertEqual(float(rects[1].get('height')), 200)
