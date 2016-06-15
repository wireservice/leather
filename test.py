import datetime

import leather

data = [
    (0, 0),
    (5, 5),
    (10, 10)
]

chart = leather.Chart('Dots')
chart.add_x_scale(7, 10)
chart.add_y_scale(7, 10)
chart.add_line(data)
chart.to_svg('test.svg')

foo = leather.Chart('Dots')
foo.add_x_scale(7, 10)
foo.add_line(data)
foo.to_svg('test.svg')
