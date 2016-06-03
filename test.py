import leather

data = [
    (2, 3, 'foo'),
    (4, 5, 'foo'),
    (7, 9, 'bar'),
    (8, 4, 'bar')
]

chart = leather.Chart('Dots')
chart.add_line(data, x=0, y=1, name='Short')
chart.add_line(data, x=1, y=0, name='Very very very very very very very very long')
chart.to_svg('test.svg')
