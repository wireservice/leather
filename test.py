import leather

data1    = [
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
]

data2 = [
    (2, 4),
    (7, 3),
    (6, 2),
    (5, 9)
]

data3 = [
    (2, 7),
    (7, 2)
]

chart = leather.Chart('Multiple series')
chart.add_x_axis(name='Foo')
chart.add_dots(data1, name="This is a really insanely long series name......")
chart.add_dots(data2, name="And this one is almost as long!")
chart.add_dots(data3, name="But this one's short.")
chart.to_svg('test.svg')
