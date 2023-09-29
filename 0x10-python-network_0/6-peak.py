#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mil = int(size / 2)
    peak = list_of_integers[mil]
    if peak > list_of_integers[mil - 1] and peak > list_of_integers[mil + 1]:
        return peak
    elif peak < list_of_integers[mil - 1]:
        return find_peak(list_of_integers[:mil])
    else:
        return find_peak(list_of_integers[mil + 1:])
