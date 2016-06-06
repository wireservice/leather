#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from lxml import etree


class LeatherTestCase(unittest.TestCase):
    """
    Unittest case for quickly asserting logic about charts.
    """
    def render_chart(self, chart):
        """
        Verify the column names in the given table match what is expected.
        """
        svg = chart.to_svg()

        return self.parse_svg(svg)

    def parse_svg(self, text):
        return etree.fromstring(text.replace(' xmlns="http://www.w3.org/2000/svg"', ''))

    def assertElementCount(self, svg, selector, count):
        series = svg.cssselect(selector)
        self.assertEqual(len(series), count)

    def assertTickLabels(self, svg, orient, compare):
        ticks = [t.text for t in svg.cssselect('.%s .tick text' % orient)]
        self.assertSequenceEqual(ticks, compare)
