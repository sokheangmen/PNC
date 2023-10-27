#  IMPORTS
import tkinter as tk

#  CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#  VARIABLES
grid = [0,0,1,0,0,0,0]

SQUARE_SIZE  = SCREEN_WIDTH/len(grid) #choose the appropriate size of the squares
COLOR=1
#  FUNCTIONS
def arrayToDrawing():
    for i in range(len(grid)):
        if grid[i]==COLOR:
            canvas.create_rectangle(SQUARE_SIZE*i,300,SQUARE_SIZE+SQUARE_SIZE*i,360 ,fill="red")
        else :
            canvas.create_rectangle(SQUARE_SIZE*i,300,SQUARE_SIZE+SQUARE_SIZE*i,360)
    return None
    # draw a line with white and black squares using the global array


root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("PNC Data structure to graphism")
frame.pack(expand=True, fill='both')
canvas = tk.Canvas(frame)
canvas.pack(expand=True, fill="both")

arrayToDrawing()

root.mainloop()
