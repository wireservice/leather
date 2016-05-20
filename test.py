#!/usr/bin/env python

from datetime import date, datetime

import leather


data = [
    (datetime(2010, 1, 1), 4),
    (datetime(2011, 5, 4), 3),
    (datetime(2012, 6, 1, 11), 5),
    (datetime(2013, 1, 1), 6),
    (datetime(2014, 12, 1), 10)
]

chart = leather.Chart("X axis ftw")
chart.add_lines(data)
chart.to_svg('test.svg')
