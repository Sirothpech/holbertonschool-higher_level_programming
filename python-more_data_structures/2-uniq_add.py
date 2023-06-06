#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    sum = 0
    new_list = []
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
    return sum
