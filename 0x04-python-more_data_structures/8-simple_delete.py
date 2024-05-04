#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    else:
        return a_dictionary
    return a_dictionary
def print_sorted_dictionary(a_dictionary):
    my_dict = dict(sorted(a_dictionary.items()))
    for key, value in my_dict.items():
        print("{}: {}".format(key, value))
