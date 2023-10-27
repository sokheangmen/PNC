# IMPORTS
from array import array
from re import X
import tkinter as tk
import random

colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

# FUNCTIONS
def drawRandomCircle():
    # TODO
    pos=randomCanvas()
    randomCanvas()
    canvas.create_oval(pos[0]-pos[1]/2,pos[2]-pos[0]/2,pos[1]+pos[0]/2,pos[2]+pos[0]/2 ,fill=colors[random.randrange(0,len(colors)-1)])
    return

def onclick(event):
    # TODO  
    pos=randomCanvas()
    canvas.create_rectangle(pos[2]-pos[1]/2,pos[2]-pos[0]/2,pos[1]+pos[0]/2,pos[2]+pos[0]/2 ,fill=colors[random.randrange(0,len(colors)-1)])
    canvas.after(3000, lambda:drawRandomCircle())
    return

def randomCanvas():
    size=random.randrange(30,300)
    x=random.randrange(0,800)
    y=random.randrange(0,800)
    arrayOfrandom=[size,x,y]
    return arrayOfrandom
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

# call the draw cicle after 5 seconds

root.bind("<space>",onclick)

root.mainloop()