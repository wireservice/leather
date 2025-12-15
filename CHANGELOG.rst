0.4.1 - December 15, 2025
-------------------------

* Add Python 3.13 and 3.14 support. Drop support for end-of-life versions 3.8 and 3.9.

0.4.0 - February 23, 2024
-------------------------

* feat: :meth:`.Chart.add_line` accepts a `stroke_dasharray argument <https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray>`_.
* feat: Add a ``default_stroke_dasharray`` theme option.
* fix: Apply the ``axis_title_font_size`` and ``tick_font_size`` theme options.

0.3.5 - October 23, 2023
------------------------

* Leather no longer reconfigures Python warnings globally.
* Add Python 3.11 and 3.12 support.
* Drop Python 3.7 support (end-of-life was June 27, 2023).

0.3.4 - October 8, 2021
-----------------------

* Add Python 3.10 support.

0.3.3 - November 30, 2016
-------------------------

* Fix examples that used invalid column data. (#81)
* lxml is no longer imported by default. (#83)
* Ordinal scales can now display data from multiple series with different values. (#76)
* Better error handling for data types supported by different shapes.

0.3.2 - November 11, 2016
-------------------------

* Fix trove classifiers.

0.3.1 - November 11, 2016
-------------------------

* Fix unicode rendering issue in Python2.7 and PyPy. (#74)

0.3.0 - November 11, 2016
-------------------------

* Add examples for many more use-cases. (#11)
* Fixed bars so that data are displayed top-down when using :meth:`.Chart.add_bars`. (#72)
* Changed default colors. (#51)
* Fixed a rare file handling bug when saving SVG files.
* Leather will now issue a warning if you attempt to render a chart with data exceeding the scale domain. (#42)
* Linear scales will now default to the domain :code:`[0, 1]` if no values are provided. (#66)
* Axis no longer takes a number of ticks as an argument. Instead pass a list of custom tick values.
* Scales :code:`tick` methods no longer take a number of ticks as an argument. (They should self-optimize.)
* Scales that cross :code:`0` will now always have a tick at :code:`0`. (#54)
* Implemented auto-ticking. (#23)
* :func:`.style_function` now takes a :class:`.Datum` instances, rather than a list of arguments.
* Renamed the :code:`Lines` class to :class:`.Line` to be more accurate.
* Implemented :class:`.CategorySeries`.
* Implemented a more elegant pattern for colorizing series.
* Refactored :class:`.Series` so :class:`.Shape` is no longer a parameter.
* Tick values can now be overridden with the :code:`tick_values` argument. (#56)
* Added methods to customize scales and axes for :class:`.Lattice` charts. (#17)
* Expanded unit tests for :class:`.Scale` subclasses.
* Zero lines now render above other tick marks. (#31)
* Fixed rendering of :class:`.Bar` and :class:`.Column` shapes for negative values. (#52)
* Refactored the :class:`.Lattice` API.

0.2.0
-----

* Initial prototype

0.1.0
-----

* Never released
