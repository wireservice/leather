import leather

line_data = [
    (0, 1),
    (2, 5),
    (4, 4),
    (8, 3)
]

dot_data = [
    (1, 3),
    (2, 5),
    (6, 9),
    (10, 4)
]

chart = leather.Chart('Mixed shapes')
chart.add_line(line_data)
chart.add_dots(dot_data)
chart.to_svg('examples/charts/mixed_shapes.svg')
