#!/usr/bin/env python

import os
import sys

# Path munging
sys.path.insert(0, os.path.abspath('..'))

# Extensions
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx'
]
# autodoc_member_order = 'bysource'
autodoc_default_flags = ['members', 'show-inheritance']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3.5', None)
}

# Templates
templates_path = ['_templates']
master_doc = 'index'

# Metadata
project = 'leather'
copyright = '2016, Christopher Groskopf'
version = '0.3.4'
release = '0.3.4'

exclude_patterns = ['_build']
pygments_style = 'sphinx'

# HTMl theming
html_theme = 'furo'

html_static_path = ['_static']
htmlhelp_basename = 'leatherdoc'
