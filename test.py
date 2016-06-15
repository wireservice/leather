import datetime

import leather

data = [
    (0, 0),
    (5, 0),
    (10, 0)
]

chart = leather.Chart('Dots')
chart.add_x_scale(7, 10)
chart.add_line(data)
chart.to_svg('test.svg')
