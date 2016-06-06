#!/usr/bin/env python

import leather


class TestChart(leather.LeatherTestCase):
    def setUp(self):
        self.data = [
            (0, 3),
            (4, 5),
            (7, 9),
            (10, 4)
        ]

    def test_ticks(self):
        chart = leather.Chart()
        chart.add_dots(self.data)

        axis = leather.Axis(ticks=6)
        chart.set_x_axis(axis)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'bottom', ['2', '4', '6', '8', '10', '0'])

    def test_tick_values(self):
        chart = leather.Chart()
        chart.add_dots(self.data)

        axis = leather.Axis(tick_values=[-12, 0, 17, 44, 87, 99])
        chart.set_x_axis(axis)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'bottom', ['-12', '17', '44', '87', '99', '0'])

    def test_tick_formatter(self):
        chart = leather.Chart()
        chart.add_dots(self.data)

        def test_formatter(value, i, count):
            return '%i+' % (value * 10)

        axis = leather.Axis(tick_formatter=test_formatter)
        chart.set_x_axis(axis)

        svg = self.render_chart(chart)

        self.assertTickLabels(svg, 'bottom', ['25+', '50+', '75+', '100+', '0+'])
