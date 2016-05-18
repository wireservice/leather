#!/usr/bin/env python

from leather.scales.base import Scale


class Linear(Scale):
    """
    A scale that linearly maps values from a domain to a range.
    """
    def __init__(self, domain_min, domain_max):
        self.min = domain_min
        self.max = domain_max

    def project(self, value, range_min, range_max):
        """
        Project a value to the given range.
        """
        pos = float(value - self.min) / (self.max - self.min)

        return ((range_max - range_min) * pos) + range_min

    def project_interval(self, value, range_min, range_max):
        raise NotImplementedError

    def ticks(self, count):
        """
        Return a sequence of :code:`count` ticks based on this scale.
        """
        i = float(self.max - self.min) / (count - 1)
        t = self.min

        yield t

        while t < self.max:
            t += i

            if int(t) == t:
                t = int(t)

            yield t
