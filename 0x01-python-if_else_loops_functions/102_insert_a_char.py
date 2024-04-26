#!/usr/bin/python3
def insert_a_char(string, n, char):
    if n < 0 or n >= len(string): # return string if index is out of bound
        return string
    else:
        return string[:n] + "{}".format(char) + string[n:]
