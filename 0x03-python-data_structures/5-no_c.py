#!/usr/bin/python3
def no_c(my_string):
    string  = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            string += i
    return string
