========
Examples
========

Data series
===========

Simple pairs
------------

.. literalinclude:: ../examples/simple_pairs.py
    :language: python

.. figure:: ../examples/charts/simple_pairs.svg

Table from csv.reader
---------------------

Sequence row data, such as is returned by :func:`csv.reader` can be accessed by specifying the indices of the columns containing the :code:`x` and :code:`y` values.

Note that leather does not automatically convert numerical strings, such as those stored in a CSV. If you want that you'll need to use a smarter table reader, such as `agate <http://agate.rtfd.io/>`_

.. literalinclude:: ../examples/csv_reader.py
    :language: python

.. figure:: ../examples/charts/csv_reader.svg

Table from csv.DictReader
-------------------------

Dict row data, such as is returned by :class:`csv.DictReader` can be accessed by specifying the indices of the columns containing the :code:`x` and :code:`y` values.

See previous example for note on strings from CSVs.

.. literalinclude:: ../examples/csv_dict_reader.py
    :language: python

.. figure:: ../examples/charts/csv_dict_reader.svg

Custom data
-----------

TKTK

Multiple series
---------------

Multiple data series can be displayed on a single chart so long as they all use the same type of :class:`.Scale`.

.. literalinclude:: ../examples/multiple_series.py
    :language: python

.. figure:: ../examples/charts/multiple_series.svg

Shapes
======

Bars
----

.. literalinclude:: ../examples/bars.py
    :language: python

.. figure:: ../examples/charts/bars.svg

Columns
-------

.. literalinclude:: ../examples/columns.py
    :language: python

.. figure:: ../examples/charts/columns.svg

Dots
----

.. literalinclude:: ../examples/dots.py
    :language: python

.. figure:: ../examples/charts/dots.svg

Lines
-----

.. literalinclude:: ../examples/lines.py
    :language: python

.. figure:: ../examples/charts/lines.svg

Mixing shapes
-------------

You can mix different shapes for different series on the same chart.

.. literalinclude:: ../examples/mixed_shapes.py
    :language: python

.. figure:: ../examples/charts/mixed_shapes.svg

Scales
======

Linear
------

TKTK

Ordinal
-------

TKTK

Temporal
--------

TKTK

Axes
====

Changing tick count
-------------------

TKTK

Customizing tick format
-----------------------

TKTK

Styling
=======

Changing theme values
---------------------

TKTK

Changing chart defaults
-----------------------

TKTK

Styling data based on value
---------------------------

Style attributes of individual data points can be set by value using a :func:`.style_function`.

.. literalinclude:: ../examples/colorized_dots.py
    :language: python

.. figure:: ../examples/charts/colorized_dots.svg

Chart grids
===========

With mixed scales
-----------------

You can add charts of completely different types to a single graphic by using :class:`.Grid`.

.. literalinclude:: ../examples/grid.py
    :language: python

.. figure:: ../examples/charts/grid.svg

With consistent scales
----------------------

A grid of charts can automatically be synchronized to a consistent view using :class:`.Lattice`.

.. literalinclude:: ../examples/lattice.py
    :language: python

.. figure:: ../examples/charts/lattice.svg
