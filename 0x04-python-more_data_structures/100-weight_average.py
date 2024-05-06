#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    for j, k in my_list:
        score += k * j
        weight += k
    result = score / weight
    return result
