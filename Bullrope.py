from tkinter import *
from tkinter import ttk
from functools import partial



root = Tk()
root.title("BullRope")


def movelabel(canvas,stier,event):
    if event.char=="d":
        canvas.move(stier,10,0)
    elif event.char=='a':
        canvas.move(stier,-10,0)
    elif event.char=='w':
        canvas.move(stier,0,-10)
    elif event.char=='s':
        canvas.move(stier,0,10)

    [x,y] = canvas.coords(stier)
    if x <= 0:
        canvas.move(stier, 1080, 0)
    if x >= 1080:
        canvas.move(stier, -1080, 0)
    if y <= 0:
        canvas.move(stier, 0, 1920)
    if y >= 1920:
        canvas.move(stier, 0, -1920)

bg = PhotoImage(file="background1.png")

canvas = Canvas(root, width = 1920, height = 1080)
canvas.place(x=0, y=0)
canvas.create_image( 0, 0, image = bg, anchor = "nw")
canvas.pack(fill = "both", expand = True)






stier = PhotoImage(file="Stier.png")


imgid=canvas.create_image(50, 10, image=stier, anchor= "w")
root.bind("<Key>",partial(movelabel,canvas,imgid))

root.mainloop()