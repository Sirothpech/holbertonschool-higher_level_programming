#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    matrix = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000, "D": 500}
    number = 0
    position = 0
    for key in reversed(roman_string):
        if matrix[key] < position:
            number -= matrix[key]
        else:
            number += matrix[key]
        position = matrix[key]
    return number
