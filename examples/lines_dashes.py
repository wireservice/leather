import leather

data = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

chart = leather.Chart('Line Dashes')
chart.add_line(data, stroke_dasharray='2%')
chart.to_svg('examples/charts/lines_dashes.svg')
