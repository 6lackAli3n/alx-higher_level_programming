#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): The x coordinate of the rectangle's position
        y (int): The y coordinate of the rectangle's position
        id (int): The id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with '#' characters, considering x and y"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise TypeError("{} attribute does not exist".format(key))

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
        value (int): The width value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle
                
        Args:
        value (int): The height value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieve the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle
                
        Args:
        value (int): The x coordinate value to set
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieve the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle
        Args:
        value (int): The y coordinate value to set
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
