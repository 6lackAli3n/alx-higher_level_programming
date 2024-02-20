#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that represents a list with additional functionality.
    """

    def print_sorted(self):
    """
    Prints the list in sorted order (ascending sort).
    """
    sorted_list = sorted(self)
    print(sorted_list)
