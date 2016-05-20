#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather import svg
from leather import theme


class Axis(object):
    """
    A horizontal or vertical chart axis.

    :param ticks:
        The number of ticks to display for this axis. Defaults to
        :data:`.theme.default_ticks`
    :param tick_formatter:
        An optional :func:`.tick_format_function`.
    """
    def __init__(self, ticks=None, tick_formatter=None, name=None):
        self._ticks = ticks or theme.default_ticks
        self._tick_formatter = tick_formatter or tick_format_function
        self._name = name

    def _estimate_left_tick_width(self, scale):
        """
        Estimate the y axis space used by tick labels.
        """
        ticks = scale.ticks(self._ticks)
        tick_count = len(ticks)
        max_len = 0

        for i, value in enumerate(ticks):
            max_len = max(max_len, len(self._tick_formatter(value, i, tick_count)))

        return max_len * theme.tick_font_char_width

    def estimate_label_margin(self, scale, orient):
        """
        Estimate the space needed for the tick labels.
        """
        margin = 0

        if orient == 'left':
            margin += self._estimate_left_tick_width(scale) + (theme.tick_size * 2)
        elif orient == 'bottom':
            margin += theme.tick_font_char_height + (theme.tick_size * 2)

        if self._name:
            margin += theme.axis_title_font_char_height + theme.axis_title_gap

        return margin

    def to_svg(self, width, height, scale, orient):
        """
        Render this axis to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'axis ' + orient)

        # Axis title
        if orient == 'left':
            title_x = -(self._estimate_left_tick_width(scale) + theme.axis_title_gap)
            title_y = height / 2
            dy=''
            transform = svg.rotate(270, title_x, title_y)
        elif orient == 'bottom':
            title_x = width / 2
            title_y = height + theme.tick_font_char_height + (theme.tick_size * 2) + theme.axis_title_gap
            dy='1em'
            transform = ''

        title = ET.Element('text',
            x=six.text_type(title_x),
            y=six.text_type(title_y),
            dy=dy,
            fill=theme.axis_title_color,
            transform=transform
        )
        title.set('text-anchor', 'middle')
        title.set('font-family', theme.axis_title_font_family)
        title.text = self._name

        group.append(title)

        # Ticks
        if orient == 'left':
            label_x = -(theme.tick_size * 2)
            x1 = -theme.tick_size
            x2 = width
            range_min = height
            range_max = 0
        elif orient == 'bottom':
            label_y = height + (theme.tick_size * 2)
            y1 = 0
            y2 = height + theme.tick_size
            range_min = 0
            range_max = width

        tick_values = scale.ticks(self._ticks)
        tick_count = len(tick_values)

        for i, value in enumerate(tick_values):
            # Tick group
            tick_group = ET.Element('g')
            tick_group.set('class', 'tick')
            group.append(tick_group)

            # Tick line
            projected_value = scale.project(value, range_min, range_max)

            if value == 0:
                tick_color = theme.zero_color
            else:
                tick_color = theme.tick_color

            if orient == 'left':
                y1 = projected_value
                y2 = projected_value

            elif orient == 'bottom':
                x1 = projected_value
                x2 = projected_value

            tick = ET.Element('line',
                x1=six.text_type(x1),
                y1=six.text_type(y1),
                x2=six.text_type(x2),
                y2=six.text_type(y2),
                stroke=tick_color
            )
            tick.set('stroke-width', six.text_type(theme.tick_width))

            tick_group.append(tick)

            # Tick label
            if orient == 'left':
                x = label_x
                y = projected_value
                dy = '0.32em'
                text_anchor = 'end'
            elif orient == 'bottom':
                x = projected_value
                y = label_y
                dy = '1em'
                text_anchor = 'middle'

            label = ET.Element('text',
                x=six.text_type(x),
                y=six.text_type(y),
                dy=dy,
                fill=theme.label_color
            )
            label.set('text-anchor', text_anchor)
            label.set('font-family', theme.tick_font_family)

            value = self._tick_formatter(value, i, tick_count)
            label.text = six.text_type(value)

            tick_group.append(label)

        return group


def tick_format_function(value, index, tick_count):
    """
    This example shows how to define a function to format tick values for
    display.

    :param x:
        The value to be formatted.
    :param index:
        The index of the tick.
    :param tick_count:
        The total number of ticks being displayed.
    :returns:
        A stringified tick value for display.
    """
    return six.text_type(value)
