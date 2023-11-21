"""TODO: Chirstmas scenery with a christmas tree, presents, and a moon."""
__author__ = "730668208"

"""Attempting the 15%, I have broken down two of my draw functions into smaller more digestable functions and
implemented circles, the drawing is also Christmas themed. The two functions that were broken down into smaller
functions are the draw_christmas_tree and draw_gift."""

from turtle import Turtle, colormode, done


def right_side_needle(a_turtle: Turtle) -> None:
    """Draws the right side of the Christmas Tree."""
    i = 0
    while i < 3:
        a_turtle.forward(54)
        a_turtle.left(135)
        a_turtle.forward(72)
        a_turtle.right(135)
        i += 1


def left_side_needle(a_turtle: Turtle) -> None:
    """Draws the left side of the Christmas Tree."""
    i = 0
    while i < 3:
        a_turtle.forward(72)
        a_turtle.left(135)
        a_turtle.forward(54)
        a_turtle.right(135)
        i += 1


def top_of_needle(a_turtle: Turtle) -> None:
    """Draws the top of the Christmas Tree."""
    a_turtle.left(135)
    a_turtle.forward(65)
    a_turtle.left(90)
    a_turtle.forward(60)


def tree_trunk(a_turtle: Turtle) -> None:
    """Draws the trunk of the Christmas Tree."""
    a_turtle.left(45)
    i = 0
    while i < 2:
        a_turtle.forward(140)
        a_turtle.left(90)
        a_turtle.forward(70)
        a_turtle.left(90)
        i += 1


def square(a_turtle: Turtle) -> None:
    """Draws a square for the gift."""
    i = 0
    while i < 4:
        a_turtle.forward(90)
        a_turtle.right(90)
        i += 1


def ribbon(a_turtle: Turtle) -> None:
    """Draws a ribbon for the gift."""
    i = 0
    i_two = 0
    while i < 3:
        a_turtle.forward(30)
        a_turtle.right(90)
        i += 1
    a_turtle.left(90)
    while i_two < 3:
        a_turtle.left(90)
        a_turtle.forward(30)
        a_turtle.left(90)
        a_turtle.forward(30)
        a_turtle.right(90)
        a_turtle.forward(30)
        i_two += 1


def draw_gift(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a gift."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.begin_fill()
    a_turtle.fillcolor("green")
    square(a_turtle)
    a_turtle.end_fill()
    a_turtle.color("red")
    a_turtle.begin_fill()
    a_turtle.fillcolor("red")
    ribbon(a_turtle)
    a_turtle.end_fill()


def draw_christmas_tree(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a Christmas Tree."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.begin_fill()
    a_turtle.fillcolor("green")
    right_side_needle(a_turtle)
    top_of_needle(a_turtle)
    left_side_needle(a_turtle)
    a_turtle.end_fill()
    a_turtle.begin_fill()
    a_turtle.fillcolor("brown")
    tree_trunk(a_turtle)
    a_turtle.end_fill()


def draw_rectangle(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a rectangle."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    i = 0
    while i < 4:
        a_turtle.forward(90)
        a_turtle.right(90)
        a_turtle.forward(30)
        a_turtle.right(90)
        i += 1


def draw_moon(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a moon."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.begin_fill()
    a_turtle.fillcolor("gray")
    a_turtle.circle(40)
    a_turtle.end_fill()


def main() -> None:
    """Christmas Scenery."""
    squirtle: Turtle = Turtle()
    draw_christmas_tree(squirtle, 25, 75)
    draw_gift(squirtle, 150, 25)
    draw_gift(squirtle, 250, 25)
    draw_moon(squirtle, 250, 200)
    done()


if __name__ == "__main__":
    main()