import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

def tick_formatter(value, index, tick_count):
    return '%i (%i/%i)' % (value, index, tick_count)

chart = leather.Chart('Line')
chart.add_x_axis(tick_formatter=tick_formatter)
chart.add_line(data)
chart.to_svg('examples/charts/tick_format.svg')
