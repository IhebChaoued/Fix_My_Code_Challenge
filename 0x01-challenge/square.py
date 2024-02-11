#!/usr/bin/python3
"""a module declaring and calling a class Square"""


class Square():
    """
    class square definition. Methods:
    - constructor
    - area_of_my_square: returns the area of a square
    - perimeter_of_my_square: returns perimeter of a square
    - str: defines and returns the string respresentation
    of a square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initiates a new Square object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of a square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
