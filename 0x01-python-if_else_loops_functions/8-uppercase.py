#!/usr/bin/python3
def uppercase(str):
    for letter in c:
        ascii_value = ord(letter)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        print("{}".format(chr(ascii_value)), end="")
    print()
