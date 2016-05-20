import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Simple pairs')
chart.add_dots(data)
chart.to_svg('examples/charts/simple_pairs.svg')
