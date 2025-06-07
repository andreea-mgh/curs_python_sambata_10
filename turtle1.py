import turtle
from random import randint as r

t = turtle.Turtle()
t.reset()
t.shape("turtle")
t.speed(5)

def poligon(laturi, lungime=100):
    for _ in range(laturi):
        t.forward(lungime)
        t.left(360/laturi)


for _ in range(30):
    t.penup()
    t.setposition(r(-300, 300), r(-300, 300))
    t.pendown()

    poligon(6, r(20, 150))



turtle.done()