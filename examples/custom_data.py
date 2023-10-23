import leather

data = [
    {'x': 0, 'q': {'y': [3]}},
    {'x': 4, 'q': {'y': [5]}},
    {'x': 7, 'q': {'y': [9]}},
    {'x': 8, 'q': {'y': [4]}},
]


def x(row, index):
    return row['x']


def y(row, index):
    return row['q']['y'][0]


chart = leather.Chart('Line')
chart.add_line(data, x=x, y=y)
chart.to_svg('examples/charts/custom_data.svg')
