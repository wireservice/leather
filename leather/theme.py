"""
This module contains all style configuration for rendering charts. Setting any
of these variables will change how charts are rendered.
"""

# CHART

#: Default chart width
default_chart_width: int = 800

#: Default chart height
default_chart_height: int = 600

#: Chart background color
background_color: str = '#f9f9f9'

#: Chart margin as a percent of chart width
margin: float = 0.05

# CHART TITLE

#: Chart title text color
title_color: str = '#333'

#: Chart title font
title_font_family: str = 'Monaco'

#: Chart title font size
title_font_size: int = 16

#: Approximate glyph height of the title font
title_font_char_height: int = 16

#: Approximate glyph width of the title font
title_font_char_width: int = 9

#: Gap between title and rest of chart
title_gap: int = 4

# LEGEND

#: Chart legend text color
legend_color: str = '#666'

#: Chart legend font
legend_font_family: str = 'Monaco'

#: Chart legend font size
legend_font_size: int = 14

#: Approximate glyph height of the legend font
legend_font_char_height: int = 14

#: Approximate glyph width of the legend font
legend_font_char_width: int = 8

#: Gap between legend and rest of chart
legend_gap: int = 4

#: Size of the bubble next to an legend item
legend_bubble_size: int = 10

#: Offset from the top of the glyph
legend_bubble_offset: int = 4

# AXIS

#: Axis title text color
axis_title_color: str = '#666'

#: Axis title font
axis_title_font_family: str = 'Monaco'

#: Axis title font size
axis_title_font_size: int = 14

#: Approximate glyph height of the axis title font
axis_title_font_char_height: int = 14

#: Approximate glyph width of the axis title font
axis_title_font_char_width: int = 8

#: Gap between axis title and rest of chart
axis_title_gap: int = 16

# TICKS

#: Width of a tick mark
tick_width: int = 1

#: Length of a tick mark
tick_size: int = 4

#: Color of tick marks
tick_color: str = '#eee'

#: Color of the zero tick mark
zero_color: str = '#a8a8a8'

# TICK LABELS

#: Color of tick label text
label_color: str = '#9c9c9c'

#: Tick label font
tick_font_family: str = 'Monaco'

#: Tick label font size
tick_font_size: int = 14

#: Approximate glyph height of the tick label font
tick_font_char_height: int = 14

#: Approximate glyph width of the tick label font
tick_font_char_width: int = 8

# SERIES

#: Default sequence of :class:`.Shape` colors
default_series_colors: list[str] = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

#: Default :class:`.Dots` radius
default_dot_radius: int = 3

#: Default :class:`.Line` width
default_line_width: int = 2

#: Default stroke-dasharray property when using dashes on a line
default_stroke_dasharray: str = 'none'
