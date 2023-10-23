============
Installation
============

Users
-----

To use leather install it with pip::

    pip install leather

Developers
----------

If you are a developer that also wants to hack on leather, install it from git::

    git clone git://github.com/wireservice/leather.git
    cd leather
    mkvirtualenv leather

    pip install -e .[test]

    python setup.py develop

.. note::

    To run the leather tests with coverage::

        pytest --cov leather

Supported platforms
-------------------

leather supports the following versions of Python:

* Python 2.7
* Python 3.3+
* `PyPy <https://www.pypy.org/>`_

It is tested primarily on OSX, but due to its minimal dependencies it should work on both Linux and Windows.

.. note::

    `iPython <https://ipython.org/>`_ or `Jupyter <https://jupyter.org/>`_ user? Leather works great there too.
