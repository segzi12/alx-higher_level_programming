#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
def print_sorted_dictionary(a_dictionary):
    my_dict = dict(sorted(a_dictionary.items()))
    for key, value in my_dict.items():
        print("{}: {}".format(key, value))
