#!/usr/bin env python

import random

import leather

# Example 1

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

# Example 2

dot_data = [(random.randint(0, 250), random.randint(0, 250)) for i in range(100)]

def colorizer(x, y, i):
    return 'rgb(%i, %i, %i)' % (x, y, 150)

chart = leather.Chart('Well that was easy')
chart.add_dots(dot_data, color=colorizer)
chart.to_svg('docs/example2.svg')
