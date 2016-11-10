from datetime import date

import leather

data = [
    (date(2015, 1, 1), 3),
    (date(2015, 3, 1), 5),
    (date(2015, 6, 1), 9),
    (date(2015, 9, 1), 4)
]

chart = leather.Chart('Temporal')
chart.add_x_scale(date(2014, 1, 1), date(2016, 1, 1))
chart.add_line(data)
chart.to_svg('examples/charts/temporal.svg')
