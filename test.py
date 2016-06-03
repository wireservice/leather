import leather

data = [
    (2, 3, 'foo'),
    (4, 5, 'foo'),
    (7, 9, 'bar'),
    (8, 4, 'bar')
]

chart = leather.Chart('Dots')
chart.add_dots(data, x=0, y=1, name='Short')
chart.add_dots(data, x=1, y=0, name='Very very very very very very very very long')
chart.add_dots(data, x=1, y=1, name='Looooooooooooooooooooooooooooooooooooooooooooooooooong')
chart.to_svg('test.svg')
