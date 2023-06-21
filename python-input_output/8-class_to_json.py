#!/usr/bin/python3
"""
Write a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Write a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    """
    if isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, str):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    else:
        return obj.__dict__
