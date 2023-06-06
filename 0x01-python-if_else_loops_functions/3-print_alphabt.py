#!/usr/bin/python3
for a in range(97, 97+26):
    if chr(a) != "e" and chr(a) != "q":
        print("{}".format(chr(a)), end="")
