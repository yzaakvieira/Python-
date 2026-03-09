# Write a function called rectangle that draws a rectangle with given side lengths.
import turtle as t

def rectangle(length, height):
    for _ in range(2):
        # Obs: The use of the _ is because the count variable it does not appear in the body of the for loop.
        t.forward(length)
        t.left(90)
        t.forward(height)
        t.left(90)

rectangle(300, 80)

t.done()
