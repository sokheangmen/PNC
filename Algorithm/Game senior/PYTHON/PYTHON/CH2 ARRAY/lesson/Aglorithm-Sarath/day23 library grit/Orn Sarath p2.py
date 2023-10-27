import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("360x360")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)
x1=30
x2=80
y1=30
y2=80
for y in range(5):
    for x in range(5):
        if y==x:
            cavas.create_oval(x1,y1,x2,y2,fill="#ff0000")
        else:
            cavas.create_oval(x1,y1,x2,y2,fill="#0000ff")


        x1= x2
        x2+=50
    y1=y2
    y2+=50
    x1=30
    x2=80


# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()



