#!/usr/bin/env python

import leather


class TestGrid(leather.LeatherTestCase):
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

    def test_add_one(self):
        chart1 = leather.Chart()
        chart1.add_dots(self.data1)

        chart2 = leather.Chart()
        chart2.add_dots(self.data2)

        grid = leather.Grid()
        grid.add_one(chart1)
        grid.add_one(chart2)

        svg = self.render_chart(grid)

        self.assertElementCount(svg, '.axis', 4)
        self.assertElementCount(svg, '.series', 2)
        self.assertElementCount(svg, '.dots', 2)
        self.assertElementCount(svg, 'circle', 9)

    def test_add_many(self):
        chart1 = leather.Chart()
        chart1.add_dots(self.data1)

        chart2 = leather.Chart()
        chart2.add_dots(self.data2)

        grid = leather.Grid()
        grid.add_many([chart1, chart2, chart1])

        svg = self.render_chart(grid)

        self.assertElementCount(svg, '.axis', 6)
        self.assertElementCount(svg, '.series', 3)
        self.assertElementCount(svg, '.dots', 3)
        self.assertElementCount(svg, 'circle', 13)
