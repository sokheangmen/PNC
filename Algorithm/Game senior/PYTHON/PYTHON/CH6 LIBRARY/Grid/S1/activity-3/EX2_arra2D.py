#  IMPORTS
import tkinter as tk

#  CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#  VARIABLES
grid = [
    [0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0]
]
    
    

SQUARE_SIZE  = SCREEN_WIDTH/len(grid) #choose the appropriate size of the squares
NUMBERONE=1
#  FUNCTIONS
def arrayToDrawing():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i]==NUMBERONE:
                canvas.create_rectangle(SQUARE_SIZE*i,(360*j)+50,SQUARE_SIZE+SQUARE_SIZE*i,(300*j)+50,fill="red")
            # else :
            #     canvas.create_rectangle(SQUARE_SIZE*i,300,SQUARE_SIZE+SQUARE_SIZE*i,360)
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


root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("PNC Data structure to graphism")
frame.pack(expand=True, fill='both')
canvas = tk.Canvas(frame)
canvas.pack(expand=True, fill="both")

root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
#call fuction 
arrayToDrawing()

root.mainloop()
