
#################### FUNCTIONS ######################

import tkinter as tk

#################### SCEEN ##########################

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#################### ARRAY ##########################

grid = [0,0,1,0,0,0,0]

#################### ARRAY #########################

SQUARE_SIZE  = SCREEN_WIDTH/len(grid) #choose the appropriate size of the squares

#################### VARIABLES ######################

NUMBERONE=1

#################### FUNCTIONS ######################
def arrayToDrawing():
    for i in range(len(grid)):
        if grid[i]==NUMBERONE:
            canvas.create_rectangle(SQUARE_SIZE*i,300,SQUARE_SIZE+SQUARE_SIZE*i,360 ,fill="red")
        else :
            canvas.create_rectangle(SQUARE_SIZE*i,300,SQUARE_SIZE+SQUARE_SIZE*i,360)
    return None

def getIndexOne(arr):
    # TODO
    for i in range(len(arr)):
        if arr[i]==NUMBERONE:
            return i
    return None


def moveRight(event):
    global grid
    # TODO 
    indexOfOne=getIndexOne(grid)
    if indexOfOne !=len(grid)-1:
        grid[indexOfOne]=0
        grid[indexOfOne+1]=1
    # print(grid)
    canvas.delete("all")
    #call fuction
    arrayToDrawing()

def moveLeft(event):
    # TODO 
    global grid
    indexOfOne=getIndexOne(grid)
    if indexOfOne !=0:
        grid[indexOfOne]=0
        grid[indexOfOne-1]=1
    # print(grid)
    canvas.delete("all")
    #call fuction
    arrayToDrawing()

################### MAIN ##########################
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("PNC Data structure to graphism")
frame.pack(expand=True, fill='both')
canvas = tk.Canvas(frame)
canvas.pack(expand=True, fill="both")

################### CALL FUCTION ##################

root.bind("<r>", moveRight)
root.bind("<l>", moveLeft)
arrayToDrawing()

root.mainloop()
