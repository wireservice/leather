#!/usr/bin/env python

import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart()
chart.add_dot(data)
chart.to_svg('test.svg')
