from tkinter import *
from PIL import Image, ImageTk


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

TILE_SIZE = 64

MAP_W = len(game_map[0])
MAP_H = len(game_map)


root = Tk()

canvas = Canvas(root, width =TILE_SIZE*MAP_W,
                      height=TILE_SIZE*MAP_H)


wall_img = Image.open('resurse/stone.png').resize((TILE_SIZE, TILE_SIZE))
root.wall_img = ImageTk.PhotoImage(wall_img)

grass_img = Image.open('resurse/grass.png').resize((TILE_SIZE, TILE_SIZE))
root.grass_img = ImageTk.PhotoImage(grass_img)

player_img = Image.open('resurse/sprite1.png').resize((TILE_SIZE, TILE_SIZE))
root.player_img = ImageTk.PhotoImage(player_img)

enemy_img = Image.open('resurse/sprite2.png').resize((TILE_SIZE, TILE_SIZE))
root.enemy_img = ImageTk.PhotoImage(enemy_img)

coin_img = Image.open('resurse/coin.png').resize((TILE_SIZE, TILE_SIZE))
root.coin_img = ImageTk.PhotoImage(coin_img)

for y in range(MAP_H):
    for x in range(MAP_W):
        # color = ""
        if game_map[y][x] == '█':
            canvas.create_image(x*TILE_SIZE, y*TILE_SIZE, image=root.wall_img, anchor='nw')
        else:
            canvas.create_image(x*TILE_SIZE, y*TILE_SIZE, image=root.grass_img, anchor='nw')
            if game_map[y][x] == '$':
                canvas.create_image(x*TILE_SIZE, y*TILE_SIZE, image=root.coin_img, anchor='nw')
            elif game_map[y][x] == '!':
                canvas.create_image(x*TILE_SIZE, y*TILE_SIZE, image=root.enemy_img, anchor='nw')
            elif game_map[y][x] == 'p':
                canvas.create_image(x*TILE_SIZE, y*TILE_SIZE, image=root.player_img, anchor='nw')
            



        # x1 = x * TILE_SIZE
        # y1 = y * TILE_SIZE
        # x2 = x1 + TILE_SIZE
        # y2 = y1 + TILE_SIZE

        # canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

canvas.pack()
root.mainloop()