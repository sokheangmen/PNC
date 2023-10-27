# ex3

from textwrap import fill
import tkinter as tk
import random
root=tk.Tk()
WIDTH=800
HIGHT=600
root.geometry(str(WIDTH)+"x"+str(HIGHT))
frame=tk.Frame()
frame.master.title("Nong page")
canvas=tk.Canvas(frame)
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 
'purple','cyan','pink','teal','navy','gray','aqua','#7FFF00']
y1=50
y2=100 
for y in range(10):
    x1=100
    x2=150
    for x in range(10):
        if (y==0 and x>=0) or (y>=0 and x==0) or (y==9 and x>=0) or (y>=0 and x==9)  :
            canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
        elif (x<=4 and y<=4)and (x>=0 and y>=0):
            canvas.create_rectangle((x1-80)*2,(y1-55)*2,(x2-75)*2,(y2-50)*2,fill=random.choice(colors))
        x1=x2+10
        x2=x1+50
    y1=y2+10
    y2=y1+50
canvas.pack(expand=True,fill=("both"))
frame.pack(expand=True,fill=("both"))
root.mainloop()