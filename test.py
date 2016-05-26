import leather

import datetime

data = [
    (datetime.date(2010, 1, 1), -1),
    (datetime.date(2011, 1, 1), -1),
    (datetime.date(2012, 1, 1), 0),
    (datetime.date(2013, 1, 1), 1)
]

chart = leather.Chart()
chart.add_columns(data)
chart.add_lines(data)
chart.add_dots(data)
chart.set_x_scale(leather.Annual(datetime.date(2010, 1, 1), datetime.date(2014, 1, 1)))
chart.to_svg('test.svg')
