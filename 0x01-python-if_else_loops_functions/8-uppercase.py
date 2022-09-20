#!/usr/bin/python3
def uppercase(strng):
    for char in strng:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print("")
