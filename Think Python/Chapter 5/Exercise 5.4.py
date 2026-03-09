import turtle as t 

def draw(length):
    angle = 60
    factor = 0.6
    if length > 5:
        t.forward(length)
        t.left(angle)
        draw(factor * length)
        t.right(2 * angle)
        draw(factor * length)
        t.left(angle)
        t.back(length)

print(draw(100))
t.done