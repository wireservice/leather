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

leather.theme.title_font_family = 'Comic Sans MS'
leather.theme.legend_font_family = 'Comic Sans MS'
leather.theme.tick_font_family = 'Comic Sans MS'
leather.theme.default_series_colors = ['#ff0000', '#00ff00', '#0000ff']

chart = leather.Chart('Theme')
chart.add_columns(column_data)
chart.add_line(line_data)
chart.add_dots(dot_data)
chart.to_svg('examples/charts/theme.svg')
