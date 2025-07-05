from noise import pnoise2
from math import floor
from tkinter import *

MAP_W = 70
MAP_H = 70

TILE_SIZE = 10

sea_level = 64
beach_level = 80
grass_level = 128
snow_level = 200

root = Tk()

canvas = Canvas(root, width =TILE_SIZE*MAP_W,
                      height=TILE_SIZE*MAP_H)

tile_map = []

for y in range(MAP_H):
    row=[]
    for x in range(MAP_W):
        valoare = int(pnoise2(x*0.05, y*0.05) * 128+128)
        # color = f"#{valoare:02x}{valoare:02x}{valoare:02x}"
        
        color = ""

        if valoare < sea_level:
            color = "blue"
        elif valoare < beach_level:
            color = "yellow"
        elif valoare < grass_level:
            color = "green"
        elif valoare < snow_level:
            color = "gray"
        else:
            color = "white"


        x1 = x * TILE_SIZE
        y1 = y * TILE_SIZE
        x2 = x1 + TILE_SIZE
        y2 = y1 + TILE_SIZE

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')


canvas.pack()
root.mainloop()