#!/usr/bin/python3
"""Defines a Rectangle class."""


 class Rectangle:
 """Represents a rectangle."""

 def __init__(self, width=0, height=0):
 """Initializes a new Rectangle.

 Args:
     width (int): The width of the rectangle.
     height (int): The height of the rectangle.
     """
     self.width = width
     self.height = height

@property
def width(self):
    """Gets the width of the rectangle."""
    return self.__width

@width.setter
def width(self, value):
    """Sets the width of the rectangle.

     Args:
         value (int): The width of the rectangle.

         
         Raises:
             TypeError: If value is not an integer.
             ValueError: If value is less than 0.
             """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@property
def height(self):
    """Gets the height of the rectangle."""
    return self.__height

@height.setter
def height(self, value):
    """Sets the height of the rectangle.

    Args:
        value (int): The height of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value

