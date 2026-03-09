# Write a function called rhombus that draws a rhombus with a given side length and a given interior angle.

import turtle as t

def rhombus(side_length, angle):
    for _ in range(2):
        t.forward(side_length)
        t.left(angle)
        t.forward(side_length)
        t.left(180 - angle)

rhombus(150, 100)

t.done()
