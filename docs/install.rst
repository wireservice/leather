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

    # If running Python 3 (strongly recommended for development)
    pip install -r requirements-py3.txt

    # If running Python 2
    pip install -r requirements-py2.txt

    python setup.py develop
    tox

.. note::

    To run the leather tests with coverage::

        nosetests --with-coverage tests

Supported platforms
-------------------

leather supports the following versions of Python:

* Python 2.7
* Python 3.3+
* `PyPy <http://pypy.org/>`_

It is tested primarily on OSX, but due to its minimal dependencies it should work on both Linux and Windows.

.. note::

    `iPython <http://ipython.org/>`_ or `Jupyter <https://jupyter.org/>`_ user? Leather works great there too.
