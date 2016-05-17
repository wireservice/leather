#!/usr/bin/env python

import leather

dot_data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

line_data = [
    (0, 4),
    (1, 3),
    (2, 5),
    (5, 6),
    (9, 10)
]

chart = leather.Chart()
chart.add_dot(dot_data)
chart.add_line(line_data)
chart.to_svg('test.svg')
