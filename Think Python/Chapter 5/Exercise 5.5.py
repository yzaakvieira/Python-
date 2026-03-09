# To draw a Koch curve with length x, all you have to do is:
import turtle as t
def koch_curve(length):
    t.forward(length/3)
    t.left(60)

print(koch_curve(8))