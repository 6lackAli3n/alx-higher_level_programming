#!/usr/bin/python3
"""
This module contains a class BaseGeometry with methods for geometry operations.
"""


class BaseGeometry:
    """
    A class representing a base geometry
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
        Exception: Always raises an Exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates an integer value.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to validate.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
