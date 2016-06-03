#!/usr/bin/env python

from collections import defaultdict
import xml.etree.ElementTree as ET

import six

from leather.series import CategorySeries
from leather.shapes.base import Shape
from leather import theme


class Dots(Shape):
    """
    Render a series of data as dots.

    :param fill_color:
        The color to fill the dots. You may also specify a
        :func:`.style_function`. If not specified, default chart colors will be
        used.
    :param radius:
        The radius of the rendered dots. Defaults to
        :data:`.theme.default_dot_radius`. You may also specify a
        :func:`.style_function`.
    """
    def __init__(self, fill_color=None, radius=None):
        self._fill_color = fill_color
        self._radius = radius or theme.default_dot_radius

    def validate_series(self, series):
        """
        Verify this shape can be used to render a given series.
        """
        return True

    def to_svg(self, width, height, x_scale, y_scale, series, palette):
        """
        Render dots to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series dots')

        default_colors = defaultdict(lambda: next(palette))

        for d in series.data():
            if d.x is None or d.y is None:
                continue

            proj_x = x_scale.project(d.x, 0, width)
            proj_y = y_scale.project(d.y, height, 0)

            if callable(self._fill_color):
                fill_color = self._fill_color(d)
            elif self._fill_color:
                fill_color = self._fill_color
            else:
                fill_color = default_colors[d.z]

            if callable(self._radius):
                radius = self._radius(d)
            else:
                radius = self._radius

            group.append(ET.Element('circle',
                cx=six.text_type(proj_x),
                cy=six.text_type(proj_y),
                r=six.text_type(radius),
                fill=fill_color
            ))

        return group

    def legend_to_svg(self, series, palette):
        """
        Render the legend entry for these shapes.
        """
        if self._fill_color:
            if callable(self._fill_colors):
                # TODO
                fill_color = 'black'
            else:
                fill_color = self._fill_color
        else:
            fill_color = next(palette)

        stroke_color = None

        bubble_width = theme.legend_bubble_size + theme.legend_bubble_offset

        text = six.text_type(series._name)
        text_width = (len(text) + 4) * theme.legend_font_char_width

        item_width = text_width + bubble_width

        # Group
        item_group = ET.Element('g')

        # Bubble
        bubble = ET.Element('rect',
            x=six.text_type(0),
            y=six.text_type(-theme.legend_font_char_height + theme.legend_bubble_offset),
            width=six.text_type(theme.legend_bubble_size),
            height=six.text_type(theme.legend_bubble_size)
        )

        if fill_color:
            bubble.set('fill', fill_color)
        elif stroke_color:
            bubble.set('fill', stroke_color)

        item_group.append(bubble)

        # Label
        label = ET.Element('text',
            x=six.text_type(bubble_width),
            y=six.text_type(0),
            fill=theme.legend_color
        )
        label.set('font-family', theme.legend_font_family)
        label.set('font-size', six.text_type(theme.legend_font_size))
        label.text = text

        item_group.append(label)

        return (item_group, item_width)
