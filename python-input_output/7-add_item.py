#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
import json


def add_item(args):
    """
    Script to add arguments to a Python list and save them to a file
    """
    filename = "add_item.json"

    # Load existing data from the file if it exists
    with open(filename) as f:
        data = json.load(f)

    # Add the arguments to the list
    data.extend(args)

    # Save the updated list to the file
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    # Remove the script name from the arguments
    args = sys.argv[1:]

    # Add the arguments to the list and save them to a file
    add_item(args)
