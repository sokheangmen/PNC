
#################### FUNCTIONS ######################
import tkinter as tk
#################### SCEEN ##########################

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

################### MAIN ##########################
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("PNC Data structure to graphism")
canvas = tk.Canvas(frame)
canvas['bg']='black'
###################  FUCTION ##################

def moveOval():
    canvas.move(myCircle,10,10)
    canvas.after(100, lambda:moveOval())

myCircle=canvas.create_oval(10,10,100,100,fill="red")
moveOval()

frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill="both")
root.mainloop()