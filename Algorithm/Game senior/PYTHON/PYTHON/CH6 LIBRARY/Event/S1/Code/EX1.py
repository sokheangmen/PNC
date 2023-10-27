import tkinter as tk
root = tk.Tk()
root.geometry("700x600")
frame = tk.Frame()
frame.master.title("even")

def myEventTrigger1(event):
    print("User cliked on Cricle" )#,event.y ,event.x
def myEventTrigger2(event):
    print("User cliked on Square")
def myEventTrigger3(event):
    print("User cliked on Rectangle")

canvas=tk.Canvas(frame)

canvas.create_oval(50,50,200,200 ,fill = "red" ,tags = "click1")
canvas.tag_bind("click1" ,"<Button-1>",myEventTrigger1)

canvas.create_rectangle(230,50,430,200 ,fill = "red" ,tags = "click2")
# root.bind("<l>",myEventTrigger2)
canvas.tag_bind("click2" ,"<Button-1>",myEventTrigger2)

canvas.create_rectangle(30,230,430,430 ,fill = "red" ,tags = "click3")
canvas.tag_bind("click3" ,"<Button-1>",myEventTrigger3)
 
canvas.pack(expand = True,fill = ("both"))
frame.pack(expand = True,fill = ("both"))
root.mainloop()


# # # # set color on window
# from tkinter import *   
# gui = Tk()  
# gui.geometry('200x200')  
# #set the window color
# gui['bg']='yellow'
  
# gui.mainloop()