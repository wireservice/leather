#!/usr/bin/env python

"""
Helpers for working with SVG.
"""

HEADER = '<?xml version="1.0" standalone="no"?>\n' + \
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n' + \
    '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'

def translate(x, y):
    return 'translate(%i %i)' % (x, y)
