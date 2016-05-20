import leather

data1 = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

data2 = [
    (3, 4),
    (5, 6),
    (7, 10),
    (8, 2)
]

chart1 = leather.Chart('Dots')
chart1.add_dots(data1)

chart2 = leather.Chart('Lines')
chart2.add_lines(data2)

grid = leather.Grid()
grid.add_chart(chart1)
grid.add_chart(chart2)
grid.to_svg('examples/charts/grid.svg')
