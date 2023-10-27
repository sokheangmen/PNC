# IMPORTS

from multiprocessing.sharedctypes import Value
from random import random
import tkinter as tk

######################### SIMPLE CODE  #########################

# x = 0
# y = 0
# def moveBall():
#     # TODO 
#     global x
#     global y
#     if x<550:
#         canvas.move(ball,10,10)
#         canvas.after(50, lambda:moveBall())
#         x += 10
#     elif y<550:
#         canvas.move(ball,-10,-10)
#         canvas.after(50, lambda:moveBall())
#         y += 10
#         if y == 550:
#             x = 0
#             y = 0
#     print(x,y)
#     return

######################### CLEAN CODE​ មួយណាក៏បាន ដូចគ្នា​ #########################

######################### VARABLE #########################

# SCREEN_WIDTH = 700
# SCREEN_HEIGHT = 700

# moveDown=True

# ######################### FUCTION #########################

# def moveBall():
#     global moveDown
#     positionx1=canvas.coords(ball)[0]
#     positiony2=canvas.coords(ball)[3]
#     if positionx1 == 0:
#         moveDown = True
#     elif positiony2 == SCREEN_WIDTH:
#         moveDown = False
#     if moveDown:
#         canvas.move(ball,10,10)
#         canvas.after(50, lambda:moveBall())
#     else:
#         canvas.move(ball,-10,-10)
#         canvas.after(50, lambda:moveBall())
#     return 

# ######################### MAIN #########################


# root = tk.Tk() 
# root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
# canvas = tk.Canvas(root)
# canvas.pack(expand=True, fill = 'both')

# ######################### CANVAS BALL #########################

# ball = canvas.create_oval(0,0,50,50,fill = "teal", outline = "red")
# moveBall()

# root.mainloop()

#######################################     EX2 #############################33#######################################33
from tkinter import *
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700 

moveDown=True

######################### FUCTION #########################

class Ball:
    def __init__(self,size,color):
        self.ball= canvas.create_oval(0,0,size,size,fill = "teal", outline = "red")
        self.speedx = 5
        self.speedy = 5
        self.moveBall()
    def moveBall(self):
        canvas.move(self.ball,self.speedx,self.speedy)
        pos = canvas.coords(self.ball)
        if pos[2]>=SCREEN_WIDTH or pos[0]<=0:
            self.speedx += -2
        if pos[3]>=SCREEN_HEIGHT or pos[1]<=0:
            self.speedy += -1
        root.after(40,self.moveBall)
    
######################### MAIN #########################


root = tk.Tk() 
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill = 'both')

######################### CANVAS BALL #########################
ball1=canvas.create_oval(0, 0, 50, 50, fill="orange")

root.mainloop()