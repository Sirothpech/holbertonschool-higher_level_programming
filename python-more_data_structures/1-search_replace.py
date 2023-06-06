#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    if search in range(0, len(my_list)):
        my_list.insert(search, replace)
    return my_list
