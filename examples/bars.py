import leather

data = [
    (3, 'Hello'),
    (5, 'How'),
    (9, 'Are'),
    (4, 'You')
]

chart = leather.Chart('Bars')
chart.add_bars(data)
chart.to_svg('examples/charts/bars.svg')
