#!/usr/bin/env python

import six
import xml.etree.ElementTree as ET

from leather import theme
from leather.shapes.base import Shape
from leather.utils import issequence


class CategoryShape(Shape):
    """
    Base class for shapes that can be used to render data :class:`.CategorySeries`.

    Extends the base :class:`.Shape` class.
    """
    def legend_dimension(self):
        return self._legend_dimension

    def legend_labels(self, series, palette):
        """
        Generate a dictionary of labels mappeds to colors for the legend.
        """
        label_colors = []
        legend_dimension = self._legend_dimension

        seen = set()
        legend_values = [v for v in series.values(self._legend_dimension) if v not in seen and not seen.add(v)]

        if issequence(palette):
            colors = list(palette)
            color_count = len(colors)

            for i, value in enumerate(legend_values):
                if i >= color_count:
                    raise ValueError('Fill color must have length greater than or equal to the number of unique values in all categories.')
                    
                label_colors.append((value, colors[i]))

        elif callable(palette):
            # TODO
            label_colors = []

        else:
            raise ValueError('Fill color must be a sequence of strings or a style function.')

        return label_colors

    def legend_to_svg(self, series, palette):
        """
        Render the legend entries for these shapes.
        """
        label_colors = self.legend_labels(series, palette)
        item_groups = []
        
        if hasattr(self, '_stroke_color'):
            if self._stroke_color:
                if callable(self._stroke_color):
                    # TODO
                    stroke_color = 'black'
                else:
                    stroke_color = self._stroke_color
            else:
                stroke_color = next(palette)
        else:
            stroke_color = None

        bubble_width = theme.legend_bubble_size + theme.legend_bubble_offset

        for label, fill_color in label_colors:
            text = six.text_type(label) if label is not None else 'Unnamed label'
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

            item_groups.append((item_group, item_width))
        
        return item_groups
