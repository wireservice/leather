from datetime import date

import leather

data = [
    (date(1995, 5, 13), 3, 'foo'),
    (date(1995, 6, 1), 5, 'foo'),
    (date(1995, 6, 5), 9, 'bar'),
    (date(1995, 7, 2), 4, 'bar')
]

chart = leather.Chart('Dots')
chart.add_line(data)
chart.to_svg('test.svg')
