#  IMPORTS
from tkinter import *
from PIL import ImageTk, Image
#IMAGE

#  CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#  VARIABLES
grid = [0,0,1,0,0,0,0]

SQUARE_SIZE  = SCREEN_WIDTH/len(grid) #choose the appropriate size of the squares
NUMBERONE=1
#  FUNCTIONS

def arrayToDrawing():
    for i in range(len(grid)):
        if grid[i]==NUMBERONE:
            canvas.create_rectangle(300,SQUARE_SIZE*i,360 ,SQUARE_SIZE+SQUARE_SIZE*i,fill="red")
            canvas.create_image(330,230,image=img)
        else :
            canvas.create_rectangle(300,SQUARE_SIZE*i,360,SQUARE_SIZE+SQUARE_SIZE*i)
    return None
    # draw a line with white and black squares using the global array

def getIndexOne(arr):
    # TODO
    for i in range(len(arr)):
        if arr[i]==NUMBERONE:
            return i
    return None


def moveDown(event):
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

def moveUp(event):
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


root = Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = Frame()
frame.master.title("PNC Data structure to graphism")
frame.pack(expand=True, fill='both')
canvas = Canvas(frame)
canvas.pack(expand=True, fill="both")
img=PhotoImage(file="image/dog2.png")
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
#call fuction 
arrayToDrawing()

root.mainloop()
