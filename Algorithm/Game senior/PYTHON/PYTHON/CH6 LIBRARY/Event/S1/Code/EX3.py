import tkinter as tk
import random
root = tk.Tk()
from PIL import ImageTk, Image
#set the window color

root.geometry("700x600")
frame = tk.Frame()
frame.master.title("EX3")
canvas = tk.Canvas(frame)
numberOfColor=random.randint(0,9)
def myEventTrigger(event):
    canvas.create_text(300,300,text="You win!",font=("Purisa", 50) ,fill="black")
    canvas.delete("PNCTarget")
    x1=30
    x2=80
    y1=60
    y2=110
    for i in range(10):
        if i==numberOfColor:
            canvas.create_oval(x1,y1,x2,y2 ,fill="red")
        x1=x2+10 #(x1 = 80 and + spac10)
        x2+=60
x1=30
x2=80
y1=130
y2=180
for j in range(10):
    if j == numberOfColor:
        canvas.create_oval(x1,y1,x2,y2, fill="blue", tags="PNCTarget")
    else:
        canvas.create_oval(x1,y1,x2,y2, fill="blue")
    x1=x2+10
    x2+=60
canvas.tag_bind("PNCTarget" ,"<Button-1>",myEventTrigger)
canvas.pack(expand=True,fill=("both"))
frame.pack(expand=True,fill=("both"))
root.mainloop()




# import tkinter as tk
# import random
# root = tk.Tk()
# root.geometry("700x600")
# frame = tk.Frame()
# frame.master.title("EX3")
# canvas = tk.Canvas(frame)

# numberOfColor=random.randint(0,9)
# print(numberOfColor)
# def myEventTrigger(event):
#     canvas.create_text(300,300,text="You win!",font=("Purisa", 50) ,fill="black")
#     canvas.itemconfig(numberOfColor, fill="red")
#     canvas.move(numberOfColor, 0, -20)
    # canvas.delete("PNCTarget")
    # x1=30
    # x2=80
    # y1=60
    # y2=110
    # for i in range(10):
    #     if i==numberOfColor:
    #         canvas.create_oval(x1,y1,x2,y2 ,fill="red" ,tags="click")
#     #     x1=x2+10 #(x1=80 and +spac10)
#     #     x2+=60
# x1=30
# x2=80
# y1=60
# y2=110
# for j in range(10):
#     if j == numberOfColor:
#         canvas.create_oval(x1,y1,x2,y2, fill="blue", tags="PNCTarget")
#     else:
#         canvas.create_oval(x1,y1,x2,y2, fill="blue")
#     x1=x2+10
#     x2+=60
# canvas.tag_bind("PNCTarget" ,"<Button-1>",myEventTrigger)
# canvas.pack(expand=True,fill=("both"))
# frame.pack(expand=True,fill=("both"))
# root.mainloop()
