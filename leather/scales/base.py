#!/usr/bin/env python

class Scale(object):
    """
    Base class for various kinds of scale objects.
    """
    def project(self, value, range):
        raise NotImplementedError()

    def ticks(self, count):
        raise NotImplementedError()
