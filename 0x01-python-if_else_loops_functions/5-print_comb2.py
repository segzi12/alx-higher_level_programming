#!/usr/bin/python3
# printing two digits numbers in  an  orderly  manner
for number in range(0, 100):
    print("{:02}" .format(number), end="")
    if number < 99:
        print(", ".format(), end="")
