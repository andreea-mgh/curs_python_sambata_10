import tkinter as tk
import random

def add_circle():
    radius = 20
    x = random.randint(radius, canvas.winfo_width() - radius)
    y = random.randint(radius, canvas.winfo_height() - radius)
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='blue')

root = tk.Tk()
root.title("Random Circles")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

button = tk.Button(root, text="Add Circle", command=add_circle)
button.pack(pady=10)

root.mainloop()