#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for item in my_list:
            if my_list.index(item) == idx:
                my_list.remove(item)
        return my_list
