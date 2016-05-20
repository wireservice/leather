import csv

import leather

with open('examples/realdata/gii.csv') as f:
    reader = csv.reader(f)
    next(reader)

    data = list(reader)[:10]

chart = leather.Chart('Test')
chart.add_x_axis(name='Test X Axis name')
chart.add_y_axis(name='The Y Axis has arrived')
chart.add_bars(data, x=1, y=0)
chart.to_svg('test.svg')
