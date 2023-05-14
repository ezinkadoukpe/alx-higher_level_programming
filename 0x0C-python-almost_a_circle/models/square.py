#!/usr/bin/python3
"""
    contains class Square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size function"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size function"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """overloading string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
