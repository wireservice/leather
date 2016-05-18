#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import leather
from tests.utils import XMLTest


class TestChart(XMLTest):
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

    def test_simple(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertElementCount(svg, '.series', 1)
        self.assertElementCount(svg, '.dots', 1)
        self.assertElementCount(svg, 'circle', 4)

    def test_multiple(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)
        chart.add_dots(self.data2)

        svg = self.render_chart(chart)

        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.dots', 2)
        self.assertElementCount(svg, 'circle', 9)
