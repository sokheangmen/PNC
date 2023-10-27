import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)

colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
x1=30
x2=80
y1=20
y2=70
for y in range(9):
    for x in range(9):
        cavas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
        x1= x2+10
        x2+=60
    y1=y2+10
    y2+= 60
    x1=30
    x2=80




# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()