#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum1 = 0
    sum2 = 0
    for score, weight in my_list:
        sum1 += score*weight
        sum2 += weight
    return sum1/sum2
