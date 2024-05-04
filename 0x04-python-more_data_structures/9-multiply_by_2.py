#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_dict = {}
    updated_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return updated_dict
def print_sorted_dictionary(a_dictionary):
    my_dict = dict(sorted(a_dictionary.items()))
    for key, value in my_dict.items():
        print("{}: {}".format(key, value))
