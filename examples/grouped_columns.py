import leather
from datetime import date

data = [
    ('Hello', 1, 'first'),
    ('World', 5, 'first'),
    ('Hello', 7, 'second'),
    ('Goodbye', 4, 'second'),
    ('Hello', 7, 'third'),
    ('Goodbye', 3, 'third'),
    ('Yellow', 4, 'third')
]

chart = leather.Chart('Columns')
chart.add_grouped_columns(data)
chart.to_svg('examples/charts/grouped_columns.svg')
