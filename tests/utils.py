#!/usr/bin/env python

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from lxml import etree
import six


class XMLTest(unittest.TestCase):
    """
    Unittest case for quickly asserting logic about tables.
    """
    def render_chart(self, chart):
        """
        Verify the column names in the given table match what is expected.
        """
        output = six.StringIO()
        chart.to_svg(output)
        text = output.getvalue()

        text = text.replace(' xmlns="http://www.w3.org/2000/svg"', '')

        return etree.fromstring(text)

    def assertElementCount(self, svg, selector, count):
        series = svg.cssselect(selector)
        self.assertEqual(len(series), count)
