#!/usr/bin/env python

class Series(object):
    """
    A series of data and associated metadata.
    """
    def __init__(self, data=[], name=None, id=None, classes=[]):
        self.data = data
        self.name = name
        self.id = id
        self.classes = classes
