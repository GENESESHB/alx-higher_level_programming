#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    # Handle the case of an empty list
    if not list_of_integers:
        return None

    # Initialize left and right pointers
    left = 0
    right = len(list_of_integers) - 1

    # Perform binary search
    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid  # Peak might be on the left side
        else:
            left = mid + 1  # Peak might be on the right side

    # When the loop exits, left and right will be equal, and it will point to a peak
    return list_of_integers[left]


