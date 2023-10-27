
################### # IMPORTS ##########################

import tkinter as tk

################### VARABEL ##########################

moveright1 = True
moveright2 = True
moverleft1 = True
moverleft2 = True

# #################### FUNCTIONS ##########################
def moveRed():
    # TODO 
    global moveright
    positionx=canvas.coords(ballRed)[0]
    positionx2=canvas.coords(ballRed)[2]

    if positionx2 == 600:
        moveright = False
    elif positionx == 0:
        moveright = True
    if moveright:
        canvas.move(ballRed,10,10)
        canvas.after(50, lambda:moveRed())
    else:
        canvas.move(ballRed,-10,-10)
        canvas.after(50, lambda:moveRed())
    # print(positionx,positionx2)
    return

# ################### FUNCTIONS ##########################
def moveBlue():
    # TODO 
    global moveright2
    positionx=canvas.coords(ballBlue)[0]
    positionx2=canvas.coords(ballBlue)[2]

    if positionx2 == 600:
        moveright2 = False
    elif positionx == 0:
        moveright2 = True
    if moveright2:
        canvas.move(ballBlue,10,10)
        canvas.after(50, lambda:moveBlue())
    else:
        canvas.move(ballBlue,-10,-10)
        canvas.after(50, lambda:moveBlue())
    # print(positionx,positionx2)
    return
################### FUNCTIONS ##########################
def moveBlack():
    # TODO 
    global moverleft1
    positionx = canvas.coords(ballBlack)[1]
    positionx2 = canvas.coords(ballBlack)[3]
    if positionx2 == 50:
        moverleft1 = False
    elif positionx == 550:
        moverleft1 = True
    if moverleft1:
        canvas.move(ballBlack,10,-10)
        canvas.after(50, lambda:moveBlack())
    else:
        canvas.move(ballBlack,-10,10)
        canvas.after(50, lambda:moveBlack())
    # print(positionx,positionx2)
    return
################### FUNCTIONS ##########################
def moveNavy():
    # TODO 
    global moverleft2
                        ## x1 y1 X2 y2
    positiony1 = canvas.coords(ballNavy)[1]
    positionx2 = canvas.coords(ballNavy)[2]

    if positiony1 == 550:
        moverleft2 = False
    elif  positionx2 == 600:
        moverleft2 = True
    if moverleft2:
        canvas.move(ballNavy,-10,10)
        canvas.after(50, lambda:moveNavy())
    else:
        canvas.move(ballNavy,10,-10)
        canvas.after(50, lambda:moveNavy())
    # print( positiony1,positionx2)
    return



################### MAIN ##########################

root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

################### CANVAS ##########################

ballRed = canvas.create_oval(0,0,50,50,fill="red", outline = "red")
ballBlue = canvas.create_oval(550,550,600,600,fill="blue", outline = "blue")
ballBlack = canvas.create_oval(0,550,50,600,fill="black", outline = "black")
ballNavy = canvas.create_oval(550,0,600,50,fill="navy", outline = "navy")

################### CALL FUCTION  ######################

moveRed()
moveBlue()
moveBlack()
moveNavy()

root.mainloop()