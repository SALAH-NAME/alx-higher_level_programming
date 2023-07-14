#!/usr/bin/python3
"""Defines the Square class for the project"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance

        Args:
            size (int): The size of the new Square instance
            x (int): The x coordinate of the new Square instance
            y (int): The y coordinate of the new Square instance
            id (int): The id of the new Square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
