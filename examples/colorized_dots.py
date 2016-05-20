import random

import leather


dot_data = [(random.randint(0, 250), random.randint(0, 250)) for i in range(100)]

def colorizer(x, y, row, i):
    return 'rgb(%i, %i, %i)' % (x, y, 150)

chart = leather.Chart('Colorized dots')
chart.add_dots(dot_data, color=colorizer)
chart.to_svg('examples/charts/colorized_dots.svg')
