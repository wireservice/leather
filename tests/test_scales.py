#!/usr/bin/env python

from datetime import date, datetime
from decimal import Decimal

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import leather
from tests.utils import XMLTest


class TestLinear(XMLTest):
    def test_project(self):
        scale = leather.Linear(0, 10)

        self.assertEqual(scale.project(2, 0, 20), 4)
        self.assertEqual(scale.project(10, 0, 40), 40)
        self.assertEqual(scale.project(5, 10, 40), 25)
        self.assertEqual(scale.project(5, 10, 41), 25.5)

        scale = leather.Linear(10, 40)

        self.assertEqual(scale.project(25, 0, 10), 5)
        self.assertEqual(scale.project(4, 0, 20), -4)

        scale = leather.Linear(10, 0)

        self.assertEqual(scale.project(5, 0, 10), 5)
        self.assertEqual(scale.project(15, 0, 20), -10)

        scale = leather.Linear(-10, 10)

        self.assertEqual(scale.project(0, 0, 10), 5)
        self.assertEqual(scale.project(-10, -5, 10), -5)

        scale = leather.Linear(-20, -10)

        self.assertEqual(scale.project(-15, 0, 10), 5)
        self.assertEqual(scale.project(-10, -5, 10), 10)

    def test_ticks(self):
        scale = leather.Linear(0, 10)

        self.assertEqual(scale.ticks(5), [0, 2.5, 5, 7.5, 10])
        self.assertEqual(scale.ticks(6), [0, 2, 4, 6, 8, 10])

    def test_decimal(self):
        scale = leather.Linear(Decimal(0), Decimal(10))

        self.assertEqual(scale.project(Decimal(2), Decimal(0), Decimal(20)), Decimal(4))
        self.assertEqual(scale.project(Decimal(10), Decimal(0), Decimal(40)), Decimal(40))
        self.assertEqual(scale.project(Decimal(5), Decimal(10), Decimal(40)), Decimal(25))
        self.assertEqual(scale.project(Decimal(5), Decimal(10), Decimal(41)), Decimal(25.5))

        self.assertEqual(scale.ticks(5)[1], Decimal(2.5))
        self.assertEqual(scale.ticks(6)[1], Decimal(2))

class TestOrdinal(XMLTest):
    def test_project(self):
        scale = leather.Ordinal(['a', 'b', 'c', 'd'])

        self.assertEqual(scale.project('b', 0, 20), 7.5)

        scale = leather.Ordinal(['a', 'd', 'c', 'b'])

        self.assertEqual(scale.project('b', 0, 20), 17.5)

    def test_project_interval(self):
        scale = leather.Ordinal(['a', 'b', 'c', 'd'])

        self.assertEqual(scale.project_interval('b', 0, 20), (5.25, 9.75))

        scale = leather.Ordinal(['a', 'd', 'c', 'b'])

        self.assertEqual(scale.project_interval('b', 0, 20), (15.25, 19.75))

    def test_ticks(self):
        scale = leather.Ordinal(['a', 'b', 'c', 'd'])

        self.assertEqual(scale.ticks(4), ['a', 'b', 'c', 'd'])
        self.assertEqual(scale.ticks(5), ['a', 'b', 'c', 'd'])
        self.assertEqual(scale.ticks(6), ['a', 'b', 'c', 'd'])


class TestTemporal(XMLTest):
    """
    Note: due to leap-year calculations, it's almost impossible to write
    exact tests for this scale which are not trivial.
    """
    def test_project(self):
        scale = leather.Temporal(date(2010, 1, 1), date(2014, 1, 1))

        self.assertAlmostEqual(scale.project(date(2011, 1, 1), 0, 20), 5, 1)
        self.assertAlmostEqual(scale.project(date(2012, 1, 1), 0, 20), 10, 1)
        self.assertAlmostEqual(scale.project(date(2009, 1, 1), 0, 20), -5, 1)

        scale = leather.Temporal(datetime(2010, 1, 1), datetime(2014, 1, 1))

        self.assertAlmostEqual(scale.project(datetime(2011, 1, 1), 0, 20), 5, 1)
        self.assertAlmostEqual(scale.project(datetime(2012, 1, 1), 0, 20), 10, 1)
        self.assertAlmostEqual(scale.project(datetime(2009, 1, 1), 0, 20), -5, 1)

    def test_project_interval(self):
        scale = leather.Temporal(date(2010, 1, 1), date(2014, 1, 1))

        with self.assertRaises(NotImplementedError):
            scale.project_interval(date(2011, 1, 1), 0, 20)

    def test_ticks(self):
        scale = leather.Temporal(date(2010, 1, 1), date(2014, 1, 1))

        ticks = scale.ticks(5)
        self.assertEqual(ticks[0], date(2010, 1, 1))
        self.assertEqual(ticks[-1], date(2014, 1, 1))


class TestYears(XMLTest):
    def test_project(self):
        scale = leather.Years(date(2010, 1, 1), date(2014, 1, 1))

        self.assertEqual(scale.project(date(2011, 1, 1), 0, 20), 6)
        self.assertEqual(scale.project(date(2012, 1, 1), 0, 20), 10)
        self.assertEqual(scale.project(date(2009, 1, 1), 0, 20), -6)

        scale = leather.Years(datetime(2010, 1, 1), datetime(2014, 1, 1))

        self.assertEqual(scale.project(datetime(2011, 1, 1), 0, 20), 6)
        self.assertEqual(scale.project(datetime(2012, 1, 1), 0, 20), 10)
        self.assertEqual(scale.project(datetime(2009, 1, 1), 0, 20), -6)

        scale = leather.Years(2010, 2014)

        self.assertEqual(scale.project(2011, 0, 20), 6)
        self.assertEqual(scale.project(2012, 0, 20), 10)
        self.assertEqual(scale.project(2009, 0, 20), -6)

    def test_project_interval(self):
        scale = leather.Years(date(2010, 1, 1), date(2014, 1, 1))

        self.assertEqual(scale.project_interval(date(2011, 1, 1), 0, 20), (4.2, 7.8))

    def test_ticks(self):
        scale = leather.Years(date(2010, 1, 1), date(2014, 1, 1))

        self.assertEqual(scale.ticks(5), [
            date(2010, 1, 1),
            date(2011, 1, 1),
            date(2012, 1, 1),
            date(2013, 1, 1),
            date(2014, 1, 1)
        ])


class TestMonths(XMLTest):
    """
    See notes for :class:`.TestTemporal`.
    """
    def test_project(self):
        scale = leather.Months(date(2010, 1, 1), date(2014, 1, 1))

        self.assertAlmostEqual(scale.project(date(2011, 1, 1), 0, 48), 12, 0)
        self.assertAlmostEqual(scale.project(date(2012, 1, 1), 0, 48), 24, 0)
        self.assertAlmostEqual(scale.project(date(2008, 12, 1), 0, 48), -12, 0)

        scale = leather.Months(datetime(2010, 1, 1), datetime(2014, 1, 1))

        self.assertAlmostEqual(scale.project(datetime(2011, 1, 1), 0, 48), 12, 0)
        self.assertAlmostEqual(scale.project(datetime(2012, 1, 1), 0, 48), 24, 0)
        self.assertAlmostEqual(scale.project(datetime(2008, 12, 1), 0, 48), -12, 0)

        with self.assertRaises(ValueError):
            scale = leather.Months(2010, 2014)

    def test_project_interval(self):
        scale = leather.Months(date(2010, 1, 1), date(2014, 1, 1))

        a, b = scale.project_interval(date(2011, 1, 1), 0, 48)
        self.assertAlmostEqual(a, 11.5, 0)
        self.assertAlmostEqual(b, 12.5, 0)

    def test_ticks(self):
        scale = leather.Months(date(2010, 1, 1), date(2014, 1, 1))

        self.assertEqual(scale.ticks(5), [
            date(2010, 1, 1),
            date(2011, 1, 1),
            date(2012, 1, 1),
            date(2013, 1, 1),
            date(2014, 1, 1)
        ])

        scale = leather.Months(date(2010, 1, 1), date(2012, 1, 1))

        self.assertEqual(scale.ticks(5), [
            date(2010, 1, 1),
            date(2010, 7, 1),
            date(2011, 1, 1),
            date(2011, 7, 1),
            date(2012, 1, 1)
        ])
