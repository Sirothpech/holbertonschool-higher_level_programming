#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods for a given object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list containing the names of the object's attributes and methods.
    """
    return dir(obj)
