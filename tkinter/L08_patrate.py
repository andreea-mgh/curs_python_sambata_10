from tkinter import *
import random
fereastra=Tk()
plansa=Canvas(fereastra,width=400, height=400)
plansa.pack()

def dreptunghi_aleatoriu(latime,inaltime,culoare):
    x1=random.randrange(latime)
    y1=random.randrange(inaltime)
    x2=x1+random.randrange(latime)
    y2=y1+random.randrange(inaltime)
    plansa.create_rectangle(x1,y1,x2,y2,fill=culoare)
    
dreptunghi_aleatoriu(200,300,'green')
dreptunghi_aleatoriu(300,100,'red')
dreptunghi_aleatoriu(100,100,'magenta')
dreptunghi_aleatoriu(200,200,'#ffd800')
dreptunghi_aleatoriu(300,200,'#ff7799')

fereastra.mainloop()