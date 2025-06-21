from tkinter import *
from random import randint as rand

bubbles = []

for i in range(25):
    bubble = {
        "x": rand(0, 400),
        "y": rand(0, 400),
        "rad": rand(3, 15),
        "speed": rand(1, 5)
    }
    bubbles.append(bubble)

def draw_bubbles():
    canvas.delete("all")
    for bubble in bubbles:
        x, y, rad = bubble['x'], bubble['y'], bubble['rad']
        canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="", outline="white")

def move_bubble():
    for bubble in bubbles:
        bubble['y'] -= bubble['speed']
        if bubble['y'] < 0:
            bubble['y'] = 400

def update():
    move_bubble()
    draw_bubbles()
    root.after(20, update)

root = Tk()

canvas = Canvas(root, width=400, height=400, bg="#331C0B")
canvas.pack()

draw_bubbles()
root.after(20, update)
root.mainloop()