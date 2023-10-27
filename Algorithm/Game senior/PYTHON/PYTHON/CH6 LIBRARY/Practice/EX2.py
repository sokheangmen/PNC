import tkinter as tk
import random
root=tk.Tk()
root.geometry("800x800")
frame=tk.Frame()
frame.master.title("page windows")
canvas=tk.Canvas(frame)

# colors_________________________________
colors= ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 
'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 
'silver', 'teal', 'white', 'yellow']

# fuction_________________________________

def drawCanvas(event):

    size=random.randrange(30,500)
    x=random.randrange(0,800)
    y=random.randrange(0,800)
    canvas.create_oval(x-size/2,y-size/2,x+size/2,y+size/2 ,fill=colors[random.randrange(0,len(colors)-1)])
    canvas.create_text(x,y,text="hello world" ,fill="red" ,font=("Purisa", 30))
    canvas.create_oval(event.x-size/2,event.y-size/2,event.x+size/2,event.y+size/2 ,fill=colors[random.randrange(0,len(colors)-1)])

root.bind("<Button-1>" ,drawCanvas)

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()