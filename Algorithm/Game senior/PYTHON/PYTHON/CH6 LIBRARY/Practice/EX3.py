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
'silver']
#canvas
for row in range(10):
    for col in range(10):
        if row == 0 or row == 9 or col == 0 or col == 9:
            canvas.create_rectangle(50+60*col,50+60*row,100+60*col,100+60*row ,fill=colors[random.randrange(0,len(colors)-1)])
        # elif (col and row<=4) and (col>=0 and row>=0):
        elif row%2==1 and col%2==1:
            canvas.create_rectangle((50+60*col)*2,(50+60*row)*2,(100+60*col)*2,(100+60*row)*2 ,fill=colors[random.randrange(0,len(colors)-1)])
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill="both")
root.mainloop() 