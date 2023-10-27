import tkinter as tk
import random

WIDTH=900
HIGHT=600
root=tk.Tk()
root.geometry(str(WIDTH)+"x"+str(HIGHT))
frame=tk.Frame()
frame.master.title("page windows")
canvas=tk.Canvas(frame)
colors= ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 
'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 
'silver', 'teal', 'white', 'yellow']
for row in range(10):
    for col in range(10):
        canvas.create_rectangle(50+60*col,50+60*row,100+60*col,100+60*row ,fill=colors[random.randrange(0,len(colors)-1)])
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill="both")
root.mainloop()