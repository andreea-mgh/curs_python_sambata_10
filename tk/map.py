from tkinter import *


game_map = ['████████████████',
            '█    █$█  !  █ █',
            '██ $ █       ! █',
            '█$   ███  $  ███',
            '█    ! █     ! █',
            '█   ████     █ █',
            '█   █    p   █ █',
            '█   !        █$█',
            '████████████████', ]

game_map = [list(row) for row in game_map]

TILE_SIZE = 16

MAP_W = len(game_map[0])
MAP_H = len(game_map)


root = Tk()

canvas = Canvas(root, width =TILE_SIZE*MAP_W,
                      height=TILE_SIZE*MAP_H)


for y in range(MAP_H):
    for x in range(MAP_W):
        color = ""
        if game_map[y][x] == '█':
            color = "gray"
        else:
            color = "green"
        
        x1 = x * TILE_SIZE
        y1 = y * TILE_SIZE
        x2 = x1 + TILE_SIZE
        y2 = y1 + TILE_SIZE

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

canvas.pack()
root.mainloop()