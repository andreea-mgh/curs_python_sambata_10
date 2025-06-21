from tkinter import *
import random
fereastra=Tk()
plansa=Canvas(fereastra,width=400, height=400)
plansa.pack()
plansa.create_rectangle(150,150,250,230)
plansa.create_polygon(150,150,200,80,250,150,fill="",outline="black")
fereastra.mainloop()