import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Dots')
chart.add_dots(data)
chart.to_svg('examples/charts/dots.svg')
