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

Multiple data series can be displayed on a single chart.

TKTK

Shapes
======

Bars
----

TKTK

Columns
-------

TKTK

Dots
----

TKTK

Lines
-----

.. literalinclude:: ../examples/lines.py
    :language: python

.. figure:: ../examples/charts/lines.svg

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

Grids
=====

With mixed scales
-----------------

TKTK

With consistent scales
----------------------

TKTK
