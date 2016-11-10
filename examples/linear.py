import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Linear')
chart.add_x_scale(0, 20)
chart.add_y_scale(-10, 10)
chart.add_line(data)
chart.to_svg('examples/charts/linear.svg')
