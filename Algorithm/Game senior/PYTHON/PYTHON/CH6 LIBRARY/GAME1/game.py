# IMPORTS 
from tkinter import*
import tkinter as tk 
import random
from PIL import ImageTk, Image
######################### VARABLE #########################
# WINDOW_HEIGHT = 600
# WINDOW_WIDTH = 600
root = tk.Tk()
root.geometry("760x600")
frame = tk.Frame()
frame.master.title("EX3")
canvas = tk.Canvas(frame)
img = PhotoImage (file="dog.png")
######################### VARABLE #########################
numberOfColor=random.randint(0,4)
def myEventTrigger(event):
    for j in range(4):
        if j == numberOfColor:
            canvas.create_rectangle(i*200+10,100,i*200+150,300 ,outline="red",img=img)
            canvas.create_text(350,50,text="You win!",font=("Purisa", 50))
for i in range(4):
    if i == numberOfColor:
        canvas.create_rectangle(i*200+10,100,i*200+150,300 ,outline="red",fill="red" ,tags="Target")
    else:
        canvas.create_rectangle(i*200+10,100,i*200+150,300 ,outline="red",fill="red")

######################### VARABLE #########################
canvas.tag_bind("Target" ,"<Button-1>",myEventTrigger)
canvas.pack(expand=True,fill=("both"))
frame.pack(expand=True,fill=("both"))
root.mainloop()

