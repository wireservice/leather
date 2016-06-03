import leather

data = [
    (2, 3, 'foo'),
    (4, 5, 'foo'),
    (7, 9, 'bar'),
    (8, 4, 'bar')
]

chart = leather.Chart('Dots')
series = leather.CategorySeries(data)
shape = leather.Dots()
chart.add_series(series, shape)
chart.to_svg('test.svg')
