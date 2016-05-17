#!/usr/bin/env python

class Scale(object):
    def project(self, value, range):
        raise NotImplementedError()

    def ticks(self, count):
        raise NotImplementedError()
