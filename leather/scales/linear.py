#!/usr/bin/env python

from leather.scales.base import Scale

class LinearScale(Scale):
    """
    A scale that linearly maps values from a domain to a range.
    """
    def __init__(self, domain):
        self.domain = domain

    def project(self, value, range):
        """
        Project a value to the given range.
        """
        pos = (value - self.domain[0]) / (self.domain[1] - self.domain[0])

        return ((range[1] - range[0]) * pos) + range[0]

    def ticks(self, count):
        i = int((self.domain[1] - self.domain[0]) / count)

        return range(self.domain[0], self.domain[1] + i, i)
