# EX1______________________________________________________
# import tkinter as tk
# import random 
# root=tk.Tk()
# WIDTH=800
# HIGHT=400
# root.geometry(str(WIDTH)+"x" +str(HIGHT))
# frame=tk.Frame()
# frame.master.title("page window")
# canvas=tk.Canvas(frame)
# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1= 250
# y1= 50
# x2= 550
# y2= 350
# for i in range(5):
#     canvas.create_rectangle(x1,y1,x2,y2, fill= random.choice(colors))
#     x1+=30
#     x2-=30
#     y1+=30
#     y2-=30
# # to display all frame
# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill="both")
# root.mainloop()
# EX2______________________________________________________
# import tkinter as tk
# import random 
# root=tk.Tk()
# WIDTH=800
# HIGHT=400
# root.geometry(str(WIDTH)+"x" +str(HIGHT))
# frame=tk.Frame()
# frame.master.title("page window")
# canvas=tk.Canvas(frame)
# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1= 250
# y1= 50
# x2= 550
# y2= 350
# for i in range(5):
#     canvas.create_oval(x1,y1,x2,y2, fill= random.choice(colors))
#     x1+=30
#     y1+=30
#     x2-=30
#     y2-=30
# # to display all frame
# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill="both")
# root.mainloop()


# EX3_____________________________________________________

from re import X
import tkinter as tk
import random 
root = tk.Tk()
WIDTH = 600
HIGHT = 600
root.geometry(str(WIDTH)+"x" +str(HIGHT))
frame = tk.Frame()
frame.master.title("page window")
canvas = tk.Canvas(frame)
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
x1 = 30 #x1 = y1 =30
x2 = 80 #x2 = y2 = x1*2
y1 = 20
y2 = 70
for y in range(9):
    for col in range(9):            
        canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
        x1 = x2+10
        x2 += 60
    y1 = y2+10
    y2 += 60
    x1 = 30
    x2 = 80
#to display all frame
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill="both")
root.mainloop()
