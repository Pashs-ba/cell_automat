from tkinter import *
from base import *
import time


def render():
    global hole, root
    while True:
        for y in range(0, size_y):
            for x in range(0, size_x):
                if hole[y, x] == 1:
                    canv.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill="black")
                else:
                    canv.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill="white")
        hole = next_motion(hole)
        root.update()
        time.sleep(0.01)


def callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    



root = Tk()
root.geometry('500x600')

canv = Canvas(width=size_x*10, height=size_y*10)
canv.pack()
btn = Button(text='Start!', command=render)
btn.pack()

canv.bind('<Button - 1>', callback)
mainloop()