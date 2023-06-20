#!/usr/bin/python3
"""
Write a function that write a text file (UTF8) and prints it to stdout:
"""


def write_file(filename="", text=""):
    """
    Write a function that write a text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)
