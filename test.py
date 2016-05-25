import leather

data = [
    (-1, -1),
    (0, 0),
    (1, 1)
]

chart = leather.Chart()
chart.add_lines(data)
chart.to_svg('test.svg')
