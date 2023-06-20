#!/usr/bin/python3
"""
Returns the list of available attributes and methods for a given object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods for a given object.
    """
    return dir(obj)
