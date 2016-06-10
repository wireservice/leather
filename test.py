import datetime

import leather

data = [
    (datetime.date(2001, 1, 1), 1000),
    (datetime.date(2001, 2, 1), 2000),
    (datetime.date(2001, 3, 1), 3000)
]

chart = leather.Chart('Dots')
chart.set_x_scale(leather.Temporal(data[0][0], data[-1][0]))
chart.add_line(data)
chart.to_svg('test.svg')
