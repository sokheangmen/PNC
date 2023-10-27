import tkinter as tk
import random

# ---------------------------------------------------------------------------
# Constant
# ---------------------------------------------------------------------------
SIZE_BALL =80
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

RIGHT ="RIGHT"
LEFT = "LEFT"
UP ="UP"
DOWN = "DOWN"

# ---------------------------------------------------------------------------
# Global
# ---------------------------------------------------------------------------
ballRedDirection = RIGHT
ballBlackDirection = RIGHT
ballYellowDirection = RIGHT
ballBlueDirection = RIGHT

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def moveBall(ball, direction):
 
    # 1 - Check if change direction -----------------------------------------
    ballX1 = canvas.coords(ball)[0]
    ballX2 = canvas.coords(ball)[2]

    if (direction == RIGHT) and  (ballX2 >= WINDOW_WIDTH) :
        direction = LEFT 

    if (direction == LEFT) and  (ballX1 <= 0) :
        direction = RIGHT 

    # 2 - Move ball----------------------------------------------------------
    if direction == RIGHT:
        x =  10
        y =  0
    else :
        x = -10
        y = 0
    canvas.move(ball,x, y)
    

    # 3 - Run again the move ball---------------------------------------------
    canvas.after(100, lambda: moveBall(ball, direction))

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
root = tk.Tk() 
root.geometry( str(WINDOW_WIDTH) + "x"  + str(WINDOW_HEIGHT))
frame = tk.Frame() 
canvas = tk.Canvas(frame)

# Create the ball--------------------------------------------------------------
ballRed = canvas.create_oval(0, 0, SIZE_BALL,  SIZE_BALL, fill="red")
ballBlack = canvas.create_oval(WINDOW_WIDTH-SIZE_BALL,  0,  WINDOW_HEIGHT, SIZE_BALL, fill="black")
ballYellow = canvas.create_oval( 0,WINDOW_WIDTH-SIZE_BALL,SIZE_BALL,WINDOW_WIDTH,fill="yellow")
ballBlue = canvas.create_oval(WINDOW_WIDTH-SIZE_BALL,WINDOW_WIDTH-SIZE_BALL,WINDOW_WIDTH,WINDOW_WIDTH, fill="blue")

# start to move-----------------------------------------------------------------
moveBall(ballRed, ballRedDirection)
moveBall(ballBlack, ballBlackDirection)
moveBall(ballYellow, ballYellowDirection)
moveBall(ballBlue, ballBlueDirection)


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()