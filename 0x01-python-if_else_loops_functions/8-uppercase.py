#!/usr/bin/python3
def uppercase(str):
    for s in str:
        c = ord(s)
        if ord('a') <= ord(s) <= ord('z'):
            c = ord(s) - 32
        print("{}".format(chr(c)), end="")
    print("")
