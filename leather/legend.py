#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather import svg
from leather import theme


class Legend(object):
    """
    Renders a legend describing the data series being charted.
    """
    def to_svg(self, width, series_list):
        """
        Render a legend series list and return it for embedding in an SVG.
        """
        legend_group = ET.Element('g')

        bubble_width = theme.legend_bubble_size + theme.legend_bubble_offset

        rows = 1
        indent = 0

        for i, series in enumerate(series_list):
            text = six.text_type(series._name or 'Series %i' % i)
            text_width = (len(text) + 4) * theme.legend_font_char_width

            if indent + text_width + bubble_width > width:
                indent = 0
                rows += 1

            y = (rows - 1) * (theme.legend_font_char_height + theme.legend_gap)

            # Group
            item_group = ET.Element('g')
            item_group.set('transform', svg.translate(indent, y))

            fill_color = getattr(series._shape, '_fill_color', None)
            stroke_color = getattr(series._shape, '_stroke_color', None)

            if callable(fill_color):
                # TODO
                fill_color = 'black'

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

            legend_group.append(item_group)
            indent += text_width + bubble_width

        height = rows * (theme.legend_font_char_height + theme.legend_gap)

        return (legend_group, height)
