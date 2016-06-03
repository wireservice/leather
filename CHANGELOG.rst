0.3.0
-----

* :func:`.style_function` now takes a :class:`.Datum` instances, rather than a list of arguments.
* Renamed the :code:`Lines` class to :class:`.Line` to be more accurate.
* Implemented :class:`.CategorySeries`.
* Implemented a more elegant pattern for colorizing series.
* Refactored :class:`.Series` so :class:`.Shape` is no longer a parameter.
* Tick values can now be overridden with the :code:`tick_values` argument. (#56)
* Added methods to customize scales and axes for :class:`.Lattice` charts. (#17)
* Expanded unit tests for :class:`.Scale` subclasses.
* Implemented :class:`.Months` scale type.
* Implemented :class:`.Years` scale type.
* Zero lines now render above other tick marks. (#31)
* Fixed rendering of :class:`.Bar` and :class:`.Column` shapes for negative values. (#52)
* Refactored the :class:`.Lattice` API.

0.2.0
-----

* Initial prototype

0.1.0
-----

* Never released
