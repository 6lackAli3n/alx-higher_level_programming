#!/usr/bin/python3
"""
This module contains a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class representing a base geometry.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
        Exception: Always raises an Exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")
