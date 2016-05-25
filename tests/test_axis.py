#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import leather
from tests.utils import XMLTest


class TestChart(XMLTest):
    def setUp(self):
        self.data = [
            (0, 3),
            (4, 5),
            (7, 9),
            (10, 4)
        ]

    def test_tick_formatter(self):
        chart = leather.Chart()
        chart.add_dots(self.data)

        def test_formatter(value, i, count):
            return '%i+' % (value * 10)

        axis = leather.Axis(tick_formatter=test_formatter)
        chart.set_x_axis(axis)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'bottom', ['25+', '50+', '75+', '100+', '0+'])
