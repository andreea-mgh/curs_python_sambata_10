from tkinter import *
fereastra=Tk()
plansa=Canvas(fereastra, width=420, height=420)
plansa.pack()

latura=100

for i in range(0,4,1):
    for j in range(0,4,1):
        if (i in (0,2) and j in (0,2)) or (i in (1,3) and j in (1,3)):
            culoare = 'black'
        else:
            culoare = 'white'
            col=1
        plansa.create_rectangle(10+latura*i,10+latura*j,10+latura*(i+1),10+latura*(j+1),fill=culoare)

fereastra.mainloop()