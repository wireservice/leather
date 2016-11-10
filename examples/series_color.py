import leather

data = [
    ('Hello', 3),
    ('How', 5),
    ('Are', 9),
    ('You', 4)
]

chart = leather.Chart('Series color')
chart.add_columns(data, fill_color='#000000')
chart.to_svg('examples/charts/series_color.svg')
