import tkinter as tk
import random

def generate_bubbles(num_bubbles):
    bubbles = []
    for _ in range(num_bubbles):
        bubble = {
            'x': random.randint(0, 400),
            'y': random.randint(0, 400),
            'rad': random.randint(10, 50),
            'speed': random.uniform(1, 5)
        }
        bubbles.append(bubble)
    return bubbles

bubbles = generate_bubbles(10)

def draw_bubbles(canvas, bubbles):
    canvas.delete("all")
    for bubble in bubbles:
        x, y, rad = bubble['x'], bubble['y'], bubble['rad']
        canvas.create_oval(x - rad, y - rad, x + rad, y + rad, fill='', outline='white')

def move_bubbles(bubbles):
    for bubble in bubbles:
        bubble['y'] -= bubble['speed']
        if bubble['y'] < 0:
            bubble['y'] = 400 + bubble['rad']  # Reset to bottom if it goes off the top

def update():
    move_bubbles(bubbles)
    draw_bubbles(canvas, bubbles)
    root.after(20, update)

root = tk.Tk()
root.title("Bubble Animation")
canvas = tk.Canvas(root, width=400, height=400, bg="#403434")
canvas.pack()

draw_bubbles(canvas, bubbles)
update()
root.mainloop()