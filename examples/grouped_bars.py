import leather
from datetime import date

data = [
    (1, 'Hello', 'first'),
    (5, 'World', 'first'),
    (7, 'Hello', 'second'),
    (4, 'Goodbye', 'second'),
    (7, 'Hello', 'third'),
    (3, 'Goodbye', 'third'),
    (4, 'Yellow', 'third')
]

chart = leather.Chart('Bars')
chart.add_grouped_bars(data)
chart.to_svg('examples/charts/grouped_bars.svg')
