#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather import theme


class Legend(object):
    """
    Renders a legend describing the data series being charted.
    """
    def to_svg(self, width, series_list):
        """
        Render a legend series list and return it for embedding in an SVG.
        """
        group = ET.Element('g')

        rows = 1
        offset = 0

        for i, series in enumerate(series_list):
            fill_color = series._shape._fill_color

            if callable(fill_color):
                # TODO
                fill_color = 'black'

            text = six.text_type(series._name or 'Series %i' % i)
            text_width = (len(text) + 4) * theme.legend_font_char_width

            if offset + text_width > width:
                indent = 0
                rows += 1

            x = offset
            y = (rows - 1) * (theme.legend_font_char_height + theme.legend_gap)

            label = ET.Element('text',
                x=six.text_type(x),
                y=six.text_type(y),
                fill=theme.legend_color
            )
            label.set('font-family', theme.legend_font_family)
            label.set('font-size', six.text_type(theme.legend_font_size))
            label.text = text

            group.append(label)

            offset += text_width

        height = rows * (theme.legend_font_char_height + theme.legend_gap)

        return (group, height)
