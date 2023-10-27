# ----------------h2==============


import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("640x640")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")

cavas = tk.Canvas(fram)
numOfColor=random.randint(0,10)

def myEventTrigger(event):
    cavas.create_text(300,300,text="You win!",font=("Purisa", 26))  
x1=30
x2=80
y1=20
y2=70
for i in range(10):
    if i == numOfColor:
        cavas.create_oval(x1,y1,x2,y2, fill="blue", tags="PNCTarget1")
          
    else:
        cavas.create_oval(x1,y1,x2,y2, fill="blue")

    x1=x2+10
    x2+=60

cavas.tag_bind("PNCTarget1","<Button-1>",myEventTrigger)

# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()




