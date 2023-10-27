# IMPORTS 
import tkinter as tk 
######################### VARABLE #########################
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

moveRightBall1=True 
moveRightBall2=True 
moveRightBall3=True 

 
######################### FUCTION #########################
def moveBall(ball,position,speed):  
    ######### position x1 and x2#
    ballX1 = canvas.coords(ball)[0] 
    ballX2 = canvas.coords(ball)[2] 

    if ballX2 >= WINDOW_WIDTH: 
        position=False 
    elif ballX1 <= 0: 
        position=True 

    if position: 
       moveX = 10
    else: 
       moveX = -10
         
    canvas.move(ball, moveX, 0) 
    # canvas.move(ball, 0, moveY) down
######################### FOR CALL FUCTON  #########################
    canvas.after(speed, lambda:moveBall(ball,position,speed))
######################### # MAIN #########################
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)) 
canvas = tk.Canvas(root) 
canvas.pack(expand=True, fill='both') 
 
######################### CANVAS BALL #########################
ball1 = canvas.create_oval(0,0,50,50,fill="blue", outline="") 

ball2 = canvas.create_oval(0,100,50,150,fill="red", outline="") 

ball3 = canvas.create_oval(0,200,50,250,fill="navy", outline="") 

ball4 = canvas.create_oval(0,300,50,350,fill="navy", outline="") 

######################### CALL FUCTION #########################
moveBall(ball1,moveRightBall1,20) 
moveBall(ball2,moveRightBall2,20) 
moveBall(ball3,moveRightBall2,20) 
moveBall(ball4,moveRightBall2,20) 

root.mainloop()