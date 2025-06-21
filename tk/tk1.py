from tkinter import *
from random import randint as rand

def adauga_cerc():
    x = rand(0, 400)
    y = rand(0, 400)
    plansa.create_oval(x, y, x+20, y+20, fill="yellow", outline="orange")

def adauga_patrat():
    x = rand(0, 400)
    y = rand(0, 400)
    plansa.create_rectangle(x, y, x+50, y+50, fill="orange", outline="yellow")
    
    win.after(1000, adauga_patrat)

win = Tk()

plansa = Canvas(win, width=400, height=400, bg="#99ECFF")
plansa.pack()

plansa.create_oval(20, 20, 40, 40, fill="yellow", outline="orange")

buton = Button(win, text="inca unul", command=adauga_cerc)
buton.pack()

# programeaza o functie dupa un nr de milisecunde
win.after(1000, adauga_patrat)

win.mainloop()