#!/usr/bin env python

import leather


data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Example chart')
chart.add_lines(data)
chart.add_dots(data)
chart.to_svg('docs/example.svg')
