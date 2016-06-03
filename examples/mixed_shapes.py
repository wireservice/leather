import leather

column_data = [
    ('Hello', 3),
    ('How', 5),
    ('Are', 9),
    ('You', 4)
]

line_data = [
    ('Hello', 1),
    ('How', 5),
    ('Are', 4),
    ('You', 3)
]

dot_data = [
    ('Hello', 3),
    ('How', 5),
    ('Are', 9),
    ('You', 4)
]

chart = leather.Chart('Mixed shapes')
chart.add_columns(column_data)
chart.add_line(line_data)
chart.add_dots(dot_data)
chart.to_svg('examples/charts/mixed_shapes.svg')
