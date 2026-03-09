import turtle as t
from turtle import penup, pendown
def jump(length):
    """Move forward length units without leaving a trail.
    Postcondition: Leaves the pen down.
    """
    penup()
    t.forward(length)
    pendown()


jump(2000)