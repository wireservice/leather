import leather

data = [
    (3, 'Hello'),
    (5, 'Hello'),
    (5, 'Hello'),
    (5, 'How'),
    (5, 'How'),
    (7, 'Are'),
    (9, 'Are'),
    (4, 'You'),
    (3, 'You'),
    (2, 'You')
]

chart = leather.Chart('Bars')
chart.add_grouped_bars(data, color=leather.theme.default_series_colors)
chart.to_svg('examples/charts/grouped_bars.svg')
