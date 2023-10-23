import leather

# data1 = [
#     (2, 'foo'),
#     (6, 'bar'),
#     (9, 'bing')
# ]
#
# data2 = [
#     (3, 'foo'),
#     (5, 'bar'),
#     (7, 'bing')
# ]
#
# lattice = leather.Lattice(shape=leather.Bars())
# lattice.add_many([data1, data2])
# lattice.to_svg('test.svg')

data1 = [
    (2, None),
    (3, None)
]

chart = leather.Chart()
chart.add_bars(data1)
chart.to_svg('test.svg')
