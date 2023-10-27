# IMPORTS
import tkinter as tk
from turtle import position

moveright=True
# FUNCTIONS

def moveBall():
    # TODO 
    global moveright
    positionx=canvas.coords(ball)[0]
    positionx2=canvas.coords(ball)[2]

    if positionx2==600:
        moveright=False
    elif positionx==0:
        moveright=True
    if moveright:
        canvas.move(ball,10,10)
        canvas.after(50, lambda:moveBall())
    else:
        canvas.move(ball,-10,-10)
        canvas.after(50, lambda:moveBall())
    # print(positionx,positionx2)
    return


# MAIN 
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

ball = canvas.create_oval(0,0,50,50,fill="teal", outline="red")

moveBall()

root.mainloop()