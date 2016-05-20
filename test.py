import leather

data = [
    (-3, 'foo', -3),
    (5, 'bar', 5),
    (-9, 'baz', -9)
]

chart = leather.Chart('Negative columns')
chart.add_bars(data)
chart.to_svg('test.svg')
