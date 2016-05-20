#!/usr/bin/env python

import random

import leather

dot_data = [(random.randint(0, 250), random.randint(0, 250)) for i in range(100)]

def colorizer(x, y, i):
    return 'rgb(%i, %i, %i)' % (x, y, 150)

chart = leather.Chart('Well that was easy')
chart.add_dots(dot_data, color=colorizer)
chart.to_svg('test.svg')

# dot_data = [
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ]
#
# line_data = [
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ]
#
# chart = leather.Chart()
# # chart.set_x_scale(leather.Linear(0, 20))
# chart.add_dots(dot_data)
# chart.add_lines(line_data)
# chart.to_svg('test.svg')

# bar_data = [
#     (3, 'foo'),
#     (5, 'bing blaarg murg'),
#     (9, 'baz'),
#     (4, 'blurg')
# ]
#
# def colorizer(x, y, i):
#     if y == 'baz':
#         return 'yellow'
#     else:
#         return 'blue'
#
# chart = leather.Chart('Bar charts are fun')
# chart.add_dots(bar_data, color=colorizer)
# chart.to_svg('test.svg')
#
# data = [[
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ], [
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ],[
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ]]
#
# grid = leather.Grid()
#
# chart = leather.Chart('Chart A')
# chart.add_lines(data[0])
# grid.add_chart(chart)
#
# chart = leather.Chart('Chart B')
# chart.add_dots(data[1])
# grid.add_chart(chart)
#
# chart = leather.Chart('Chart C')
# chart.add_dots(data[2])
# grid.add_chart(chart)
#
# grid.to_svg('test.svg')

# data = [[
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ], [
#     (0, 4),
#     (1, 3),
#     (2, 3),
#     (10, 7),
#     (15, 5)
# ], [
#     (0, 4),
#     (5, 5),
#     (6, 6),
#     (7, 7),
#     (8, 8)
# ], [
#     (4, 4),
#     (6, 3),
#     (7, 5),
#     (8, 6),
#     (12, 10)
# ]]
#
# lattice = leather.Lattice(data, leather.Lines('purple'), ['A', 'B', 'C', 'D'])
#
# lattice.to_svg('test.svg', 1200, 600)

# data = [
#     (3, 1),
#     (5, 3),
#     (9, 12),
#     (4, 15)
# ]
#
# chart = leather.Chart()
# chart.add_bars(data)
# chart.to_svg('test.svg')

# chart = leather.Chart()
# chart.set_x_scale(leather.Linear(0, 20))
# chart.set_x_axis(leather.Axis(ticks=5))
# chart.set_y_scale(leather.Linear(0, 20))
# chart.set_y_axis(leather.Axis(ticks=5))
# chart.add_dots(data)
#
# chart.to_svg('test.svg')
