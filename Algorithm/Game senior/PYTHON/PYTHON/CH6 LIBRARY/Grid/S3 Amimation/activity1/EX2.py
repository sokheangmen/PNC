import tkinter as tk
import random


# colors_________________________________
colors= ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 
'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 
'silver', 'teal', 'white', 'yellow']

# fuction_________________________________

def display():
    size=random.randrange(30,300)
    x=random.randrange(0,800)
    y=random.randrange(0,800)
    canvas.create_rectangle(x-size/2,y-size/2,x+size/2,y+size/2 ,fill=colors[random.randrange(0,len(colors)-1)])

def clickc(event):
    canvas.after(2000, lambda:display())

root = tk.Tk() 
root.geometry("800x600")
frame = tk.Frame() 
canvas = tk.Canvas(frame)


root.bind("<space>" ,clickc)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()