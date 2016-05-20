import leather

data1    = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

data2 = [
    (2, 4),
    (7, 3),
    (6, 2),
    (5, 9)
]

chart = leather.Chart('Multiple series')
chart.add_dots(data1)
chart.add_dots(data2)
chart.to_svg('examples/charts/multiple_series.svg')
