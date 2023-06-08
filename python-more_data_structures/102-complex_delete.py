#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    delete_key = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_key.append(key)

    for key in delete_key:
        del(a_dictionary[key])
    return a_dictionary
