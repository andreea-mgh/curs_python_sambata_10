import turtle
import math

t = turtle.Turtle()
t.reset()
t.shape("turtle")
t.speed(5)

def stea(p, q, lungime=100):
    c = math.gcd(p, q)

    if c != 1:
        # daca steluta e formata din mai multe stelute
        p2 = p // c
        q2 = q // c

        # for _ in range(p2):
        #     t.forward(lungime)
        #     t.right(360*q2/p2)

        vertices = []
        angle_step = 360/p

        for i in range(p):
            current_angle = math.radians(angle_step * i)

            x = lungime * math.cos(current_angle)
            y = lungime * math.sin(current_angle)
            vertices.append((x, y))

        for i in range(p):
            t.penup()
            t.goto(vertices[i])
            t.pendown()
            t.goto(vertices[ (i+q) % p ])


    else:
        # daca e o linie continua
        for _ in range(p):
            t.forward(lungime)
            t.right(360*q/p)

def poligon(laturi, lungime=100):
    for _ in range(laturi):
        t.forward(lungime)
        t.left(360/laturi)

t.color(1, 0.5, 0)     # orange
# t.fillcolor(1, 1, 0) # yellow
# t.begin_fill()

# stea(11, 5)

# t.end_fill()


optiune = input()

if optiune == "stea":
    stea(12,5)
elif optiune == "poli":
    poligon(7)
else:
    print("nu stiu forma aia")




turtle.done()