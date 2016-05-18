#!/usr/bin/env python

class Scale(object):
    """
    Base class for various kinds of scale objects.
    """
    def project(self, value, target_range):
        raise NotImplementedError

    def project_interval(self, value, target_range):
        raise NotImplementedError

    def ticks(self, count):
        raise NotImplementedError
