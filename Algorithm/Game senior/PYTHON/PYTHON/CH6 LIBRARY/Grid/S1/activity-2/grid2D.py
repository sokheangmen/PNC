
#################### IMPORT ######################

import tkinter as tk
  
from tkinter import *


#################### SCEEN ##########################

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 750


#################### ARRAY ##########################

grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,4,0,0,0,0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,0,0,0,0],
        [0,0,4,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,1,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,2,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,4,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
 ]


#################### ARRAY #########################

# SQUARE_SIZE  = SCREEN_WIDTH/len(grid) #choose the appropriate size of the squares

#################### VARIABLES ######################
# bg = PhotoImage (file="gg.png")
NUMBERONE=1
NUMBEWTOW=2
NUMBETREE=3
NUMBEFOUR=4

#################### FUNCTIONS ######################

def arrayToDrawing():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==NUMBERONE:
                canvas.create_rectangle(50*col,50*row,(50*col)+50,(50*row)+50,fill="blue")
                canvas.create_image(50*col+25,50*row+30, image=img)
            elif grid[row][col]==NUMBEWTOW:
                # canvas.create_rectangle(50*col,50*row,(50*col)+50,(50*row)+50 ,fill="black")
                canvas.create_image(55*col-5,50*row+25, image=wall)
            elif  grid[row][col]==NUMBETREE:
                canvas.create_image(55*col-29,50*row+25, image=wall)
            elif  grid[row][col]==NUMBEFOUR:
                canvas.create_image(60*col+5,50*row+25, image=wall)
            else:
                # canvas.create_image(10,10 ,image=bg)
                canvas.create_rectangle(50*col,50*row,(50*col)+50,(50*row)+50 ,fill="blue")
    return None

#################### FUNCTIONS ######################

def getIndexOne(arr):
    # TODO
    positionOfOne=[]
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col]==NUMBERONE:
                positionOfOne.append(col)
                positionOfOne.append(row)
    return positionOfOne
   

#################### FUNCTIONS ######################

def moveRight(event):
    global grid
    # TODO 
    lastCol= len(grid[0])-1
    positionChar=getIndexOne(grid)
    # [row,col]
    charRow=positionChar[1]
    charCol=positionChar[0]
    if charCol !=lastCol and  grid[charRow][charCol+1] !=NUMBETREE :
        grid[charRow][charCol]=0 
        grid[charRow][charCol+1]=1
    # if charCol != NUMBEWTOW:
    #     grid[charRow][charCol+1]=1
    print(positionChar)
    canvas.delete("all")
    arrayToDrawing()

#################### FUNCTIONS ######################

def moveLeft(event):
    # TODO 
    global grid
    positionChar = getIndexOne(grid)
    charRow = positionChar[1]
    charCol = positionChar[0]
    if charCol !=0 and grid[charRow][charCol-1] !=NUMBETREE :
        grid[charRow][charCol]=0
        grid[charRow][charCol-1]=1
    canvas.delete("all")
    arrayToDrawing()
    # print(positionChar)

#################### FUNCTIONS ######################

def moveUp(event):
    # TODO 
    global grid
    positionChar=getIndexOne(grid)
    charRow=positionChar[1]
    charCol=positionChar[0]
    if charRow != 0 and grid[charRow-1][charCol] !=NUMBETREE :
        grid[charRow][charCol]=0
        grid[charRow-1][charCol]=1
    canvas.delete("all")
    arrayToDrawing()
    # print(positionChar)

#################### FUNCTIONS ######################

def moveDown(event): 
    # TODO 
    global grid
    positionChar = getIndexOne(grid)
    charRow = positionChar[1]
    charCol = positionChar[0]
    if charRow+1<len(grid) and grid[charRow+1][charCol] !=NUMBETREE :
        grid[charRow][charCol]=0
        grid[charRow+1][charCol]=1
    canvas.delete("all")
    # print(positionChar)
    arrayToDrawing()

################### MAIN ##########################

root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("PNC Data structure to graphism")
img = PhotoImage (file="dog3.png")
wall = PhotoImage (file="images.png")
# bg = PhotoImage (file="gg.png")
frame.pack(expand=True, fill='both')
canvas = tk.Canvas(frame)
canvas.pack(expand=True, fill="both")

################### CALL FUCTION ##################

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
arrayToDrawing()

#################### FUNCTIONS ######################
root.mainloop()
