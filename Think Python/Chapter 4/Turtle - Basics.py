import turtle as t

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

polygon(7, 30)