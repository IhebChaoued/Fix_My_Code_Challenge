#!/usr/bin/python3
"""A module declaring and calling a class Square"""

class Square():
    """
    Class Square definition. Methods:
    - __init__: Initializes a new Square object
    - area_of_my_square: Returns the area of a square
    - perimeter_of_my_square: Returns the perimeter of a square
    - __str__: Defines and returns the string representation
      of a square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes a new Square object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculates and returns the area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculates and returns the perimeter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of a square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
