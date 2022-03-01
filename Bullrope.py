from tkinter import *
from tkinter import ttk
from functools import partial




root = Tk()
root.title("BullRope")
canvas = Canvas(root, width = 500, height = 500) #Fenster mit den Starrt buttons erstellen



def movelabel(canvas,stier,event): #Funktion um den Stier zu bewegen 
    if event.keysym=="Right":
        canvas.move(stier,10,0)
    elif event.keysym=='Left':
        canvas.move(stier,-10,0)


    [x,y] = canvas.coords(stier)
    if x <= 0:
        canvas.move(stier, 1920, 0)
    if x >= 1920:
        canvas.move(stier, -1920, 0)

def delay():
    hello = Label(root, text="Viel Spaß beim spielen").pack()
    root.after(1000, game)

def tutorial():
    steuerung = Label(root, text="So Schnell wie möglich die linke > Pfeiltaste drücken").pack()




def game():
    global stier, imgid, bg, canvas, top 
    es = Toplevel()
    es.title("Einzelspieler")
    bg = PhotoImage(file="background.png")

    canvas = Canvas(es, width = 1920, height = 1080)
    canvas.place(x=0, y=0)
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    canvas.pack(fill = "both", expand = True)

    stier = PhotoImage(file="Stier.png")

    imgid=canvas.create_image(300, 736, image=stier, anchor= "w")
    es.bind("<Key>",partial(movelabel,canvas,imgid))

Tutorialbtn = Button(root, text="Tutorial", command =tutorial, fg="#00EEEE", bg="#727272").pack()
Einzelspielerbtn = Button(root, text="Einzelspieler", command =delay, fg="#00EEEE", bg="#727272").pack()






root.mainloop()