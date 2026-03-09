import turtle as t

a = t.Turtle()
t.forward(200)
def square( length):
    for i in range(4):
        t.left(90)
        t.forward(length ) 

square(50)
square(200)
square(250)
square(300)
square(350)
t.done()

