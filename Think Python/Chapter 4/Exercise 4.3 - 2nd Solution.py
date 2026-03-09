import turtle as t
import math

def triangle(radius, angle):
    t.forward(radius)      # vai até a borda
    t.left(180 - angle)    # vira para o segundo lado
    t.forward(radius)      # volta ao centro
    t.left(180)            # restaura direção original

def draw_pie(n, radius):
    angle = 360 / n

    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for _ in range(n):
        triangle(radius, angle)
        t.left(angle)

draw_pie(6, 120)

t.done()



# A primeira solução fui eu que desenvolvi, essa solução foi gerada por IA, por conta que a mesma informou que o meu caso cobria apenas para casos específicos