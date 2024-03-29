from tkinter import *
from base import *
import time

stop = 1


def render():
    global hole, root, stop
    stop = 1
    while stop:
        for y in range(0, size_y):
            for x in range(0, size_x):
                if hole[y, x] == 1:
                    canv.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill="green", tag='a')
        hole = next_motion(hole)
        root.update()
        canv.delete('a')


def rand():
    for i in range(1000):
        hole[random.randint(0, size_x-1), random.randint(1, size_y-1)] = 1
    render()


def callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    

def foget():
    global stop, hole, start_hole
    stop = 0
    time.sleep(0.01)
    canv.delete('a')
    hole = start_hole.copy()


root = Tk()
root.resizable(False, False)


canv = Canvas(width=size_x*10, height=size_y*10)
canv.create_rectangle(0, 0, size_x*10, size_y*10, fill='blue')
canv.grid(column=0, row=0, rowspan=2)

startBtn = Button(text='Start!', command=render)
startBtn.grid(column=0, row=2)

randBtn = Button(text='Random!', command=rand)
randBtn.grid(column=0, row=3)

restBtn = Button(text='Reset', command=foget)
restBtn.grid(column=0, row=4)

mainloop()
