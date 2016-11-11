# -*- coding: utf8 -*-

import datetime

import leather

data = [
    (0, 'foo'),
    (5, u'👍'),
    (10, 'bar')
]

chart = leather.Chart('Dots')
chart.add_bars(data)
chart.to_svg('test.svg')
