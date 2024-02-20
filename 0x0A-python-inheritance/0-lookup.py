#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""

def lookup(obj):
    """
     Returns a list object containing the available attributes and methods
     of the given object.

     Args:
     obj: An object to inspect.

     Returns:
     list: A list containing the available attributes and methods.
     """
    return dir(obj)
