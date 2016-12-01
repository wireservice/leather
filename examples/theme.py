import leather

line_data = [
    (0, 1),
    (2, 5),
    (4, 4),
    (8, 3)
]

dot_data = [
    (1, 3),
    (2, 5),
    (6, 9),
    (10, 4)
]

leather.theme.title_font_family = 'Comic Sans MS'
leather.theme.legend_font_family = 'Comic Sans MS'
leather.theme.tick_font_family = 'Comic Sans MS'
leather.theme.default_series_colors = ['#ff0000', '#00ff00']

chart = leather.Chart('Theme')
chart.add_line(line_data)
chart.add_dots(dot_data)
chart.to_svg('examples/charts/theme.svg')
