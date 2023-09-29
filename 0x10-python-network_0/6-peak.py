#!/usr/bin/python3
"""Defines algorithems peak."""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid element is a peak
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    # If there is no peak in the middle, return the remaining element
    return list_of_integers[left]

