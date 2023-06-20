#!/usr/bin/python3
"""
Write a function that append a text file (UTF8) and prints it to stdout:
"""


def append_write(filename="", text=""):
    """
    Write a function that append a text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
