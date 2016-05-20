#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from lxml import etree


class XMLTest(unittest.TestCase):
    """
    Unittest case for quickly asserting logic about tables.
    """
    def render_chart(self, chart):
        """
        Verify the column names in the given table match what is expected.
        """
        text = chart.to_svg()
        text = text.replace(' xmlns="http://www.w3.org/2000/svg"', '')

        return etree.fromstring(text)

    def assertElementCount(self, svg, selector, count):
        series = svg.cssselect(selector)
        self.assertEqual(len(series), count)

    def assertTickLabels(self, svg, orient, compare):
        ticks = [t.text for t in svg.cssselect('.%s .tick text' % orient)]
        self.assertSequenceEqual(ticks, compare)
