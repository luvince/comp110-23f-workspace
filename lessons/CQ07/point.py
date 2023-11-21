"""Point Class."""

from __future__ import annotations

__author__ = "730668208"


class Point:
    """Has points that are multiplied with a factor."""
    x: float
    y: float

    def __init__(self, input_x: float = 0.0, input_y: float = 0.0):
        """Fills in x and y."""
        self.x = input_x
        self.y = input_y

    def scale_by(self, factor: int) -> None:
        """Multiplies the x and y values by a parameter of factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Makes a new Point with the multiplied x and y values."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Puts x and y values into readable format."""
        str_info: str = f"x: {self.x}; y: {self.y}"
        return str_info
    
    def __mul__(self, factor: int | float) -> Point:
        """Makes a new Point class where the x and y value are multiplied by the factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Makes a new Point class where the x and y values are added by the factor."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    
