import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Line')
chart.add_x_scale(0, 10)
chart.add_x_axis(ticks=[0, 10])
chart.add_line(data)
chart.to_svg('examples/charts/ticks.svg')
