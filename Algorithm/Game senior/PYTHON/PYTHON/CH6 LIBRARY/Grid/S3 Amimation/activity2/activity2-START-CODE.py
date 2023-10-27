# IMPORTS
import tkinter as tk
import random

colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

# FUNCTIONS
def drawRandomCircle():
    # TODO
    size=random.randrange(30,300)
    x=random.randrange(0,800)
    y=random.randrange(0,800)
    canvas.create_oval(x-size/2,y-size/2,x+size/2,y+size/2 ,fill=colors[random.randrange(0,len(colors)-1)])
    return

def onclick(event):
    # TODO  
    size=random.randrange(30,300)
    x=random.randrange(0,800)
    y=random.randrange(0,800)
    canvas.create_rectangle(x-size/2,y-size/2,x+size/2,y+size/2 ,fill=colors[random.randrange(0,len(colors)-1)])
    canvas.after(3000, lambda:drawRandomCircle())
    return
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

# call the draw cicle after 5 seconds

root.bind("<space>",onclick)

root.mainloop()