import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Lines')
chart.add_lines(data)
chart.to_svg('examples/charts/lines.svg')
