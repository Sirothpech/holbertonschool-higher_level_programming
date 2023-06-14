#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after
each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    punct = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = True  # To keep track if a new line has already been printed
    for i, char in enumerate(text):
        if new_line and char == " ":
            continue
        if char in punct:
            print(char, end="")
            if i < len(text) - 1 and text[i+1] not in punct:
                print("\n\n", end="")
                new_line = True
            else:
                print("\n", end="")
                new_line = False
        else:
            print(char, end="")
            new_line = False
