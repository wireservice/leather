#!/usr/bin/env python

from leather.scales.base import Scale

class LinearScale(Scale):
    """
    A scale that linearly maps values from a domain to a range.
    """
    def __init__(self, domain):
        self.min = domain[0]
        self.max = domain[1]

    def project(self, value, target_range):
        """
        Project a value to the given range.
        """
        pos = (value - self.min) / (self.max - self.min)

        return ((target_range[1] - target_range[0]) * pos) + target_range[0]

    def project_interval(self, value, target_range):
        raise NotImplementedError

    def ticks(self, count):
        """
        Return a sequence of :code:`count` ticks based on this scale.
        """
        i = int((self.max - self.min) / count)

        return range(self.min, self.max + i, i)
