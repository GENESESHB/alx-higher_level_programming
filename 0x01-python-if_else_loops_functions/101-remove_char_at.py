#!/usr/bin/python3
def remove_char_at(str, n):
    str_c = ""
    for i in range(0, len(str)):
        if i != n:
            str_c = str_c + str[i]
    return (str_c)
