#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        read_data = f.read()
    print(read_data)
    f.closed
