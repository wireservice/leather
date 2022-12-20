#!/usr/bin/env python

import leather
from leather.utils import X, Y, Z


class TestSeries(leather.LeatherTestCase):
    def test_pairs(self):
        data = [
            ('foo', 1),
            ('bar', 2),
            ('baz', 3)
        ]

        series = leather.Series(data)

        self.assertSequenceEqual(series.values(X), ['foo', 'bar', 'baz'])
        self.assertSequenceEqual(series.values(Y), [1, 2, 3])

    def test_lists(self):
        data = [
            ('foo', 1, 4),
            ('bar', 2, 5),
            ('baz', 3, 6)
        ]

        series = leather.Series(data)

        self.assertSequenceEqual(series.values(X), ['foo', 'bar', 'baz'])
        self.assertSequenceEqual(series.values(Y), [1, 2, 3])

        series = leather.Series(data, x=2, y=0)

        self.assertSequenceEqual(series.values(X), [4, 5, 6])
        self.assertSequenceEqual(series.values(Y), ['foo', 'bar', 'baz'])

        with self.assertRaises(TypeError):
            series = leather.Series(data, x='words')

    def test_dicts(self):
        data = [
            {'a': 'foo', 'b': 1, 'c': 4},
            {'a': 'bar', 'b': 2, 'c': 5},
            {'a': 'baz', 'b': 3, 'c': 6}
        ]

        with self.assertRaises(KeyError):
            series = leather.Series(data)

        series = leather.Series(data, x='c', y='a')

        self.assertSequenceEqual(series.values(X), [4, 5, 6])
        self.assertSequenceEqual(series.values(Y), ['foo', 'bar', 'baz'])

    def test_custom(self):
        class Obj:
            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c =c

        data = [
            Obj('foo', 1, 4),
            Obj('bar', 2, 5),
            Obj('baz', 3, 6)
        ]

        with self.assertRaises(TypeError):
            series = leather.Series(data)

        with self.assertRaises(TypeError):
            series = leather.Series(data, x='words', y='more')

        def get_x(row, i):
            return row.b

        def get_y(row, i):
            return row.c

        series = leather.Series(data, x=get_x, y=get_y)

        self.assertSequenceEqual(series.values(X), [1, 2, 3])
        self.assertSequenceEqual(series.values(Y), [4, 5, 6])


class TestCategorySeries(leather.LeatherTestCase):
    def test_triples(self):
        data = [
            ('foo', 1, 'a'),
            ('bar', 2, 'a'),
            ('baz', 3, 'b')
        ]

        series = leather.CategorySeries(data)

        self.assertSequenceEqual(series.values(X), ['foo', 'bar', 'baz'])
        self.assertSequenceEqual(series.values(Y), [1, 2, 3])
        self.assertSequenceEqual(series.values(Z), ['a', 'a', 'b'])
