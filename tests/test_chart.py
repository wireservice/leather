#!/usr/bin/env python

import os
import warnings

import leather


TEST_SVG = '.test.svg'


class TestChart(leather.LeatherTestCase):
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

    def tearDown(self):
        if os.path.exists(TEST_SVG):
            os.remove(TEST_SVG)

    def test_single_series(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertElementCount(svg, '.axis', 2)
        self.assertElementCount(svg, '.series', 1)
        self.assertElementCount(svg, '.dots', 1)
        self.assertElementCount(svg, 'circle', 4)

    def test_multiple_series(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)
        chart.add_dots(self.data2)

        svg = self.render_chart(chart)

        self.assertElementCount(svg, '.axis', 2)
        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.dots', 2)
        self.assertElementCount(svg, 'circle', 9)

    def test_set_scales(self):
        chart = leather.Chart()
        chart.set_x_scale(leather.Linear(0, 20))
        chart.set_y_scale(leather.Linear(0, 20))
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'left', ['5', '10', '15', '20', '0'])
        self.assertTickLabels(svg, 'bottom', ['5', '10', '15', '20', '0'])

    def test_add_scales(self):
        chart = leather.Chart()
        chart.add_x_scale(0, 20)
        chart.add_y_scale(0, 20)
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'left', ['5', '10', '15', '20', '0'])
        self.assertTickLabels(svg, 'bottom', ['5', '10', '15', '20', '0'])

    def test_scale_domain_warning(self):
        chart = leather.Chart()
        chart.add_x_scale(4, 7)
        chart.add_y_scale(0, 20)
        chart.add_dots(self.data1)

        with warnings.catch_warnings():
            warnings.simplefilter('error')

            with self.assertRaises(UserWarning):
                self.render_chart(chart)

    def test_set_axes(self):
        chart = leather.Chart()
        chart.set_x_axis(leather.Axis(ticks=[0, 4, 8]))
        chart.set_y_axis(leather.Axis(ticks=[3, 6, 9]))
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'left', ['3', '6', '9'])
        self.assertTickLabels(svg, 'bottom', ['4', '8', '0'])

    def test_add_axes(self):
        chart = leather.Chart()
        chart.add_x_axis(ticks=[0, 4, 8])
        chart.add_y_axis(ticks=[3, 6, 9])
        chart.add_dots(self.data1)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'left', ['3', '6', '9'])
        self.assertTickLabels(svg, 'bottom', ['4', '8', '0'])

    def test_to_svg_file_name(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)

        chart.to_svg('.test.svg')

        self.assertTrue(os.path.exists(TEST_SVG))

    def test_to_svg_file_handle(self):
        chart = leather.Chart()
        chart.add_dots(self.data1)

        with open('.test.svg', 'w') as f:
            chart.to_svg(f)

        self.assertTrue(os.path.exists(TEST_SVG))
