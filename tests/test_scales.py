#!/usr/bin/env python

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
