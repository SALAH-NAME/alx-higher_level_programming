#!/usr/bin/python3
"""Defines the Rectangle class for the project"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance

        Args:
            width (int): The width of the new Rectangle instance
            height (int): The height of the new Rectangle instance
            x (int): The x coordinate of the new Rectangle instance
            y (int): The y coordinate of the new Rectangle instance
            id (int): The id of the new Rectangle instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle"""
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle"""
        self.__y = value
