# -----------------h3----------------------------------------------


# import tkinter as tk;
# import random
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("640x640")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")

# cavas = tk.Canvas(fram)


# numOfColor=random.randint(0,10)


# def myEventTrigger(event):
#     x1=30
#     x2=80
#     y1=120
#     y2=170
#     cavas.create_text(300,300,text="You win!",font=("Purisa", 26))
#     cavas.delete("PNCTarget1")
#     for e in range(10):
#         if e == numOfColor:
#             cavas.create_oval(x1,y1-40,x2,y2-40, fill="yellow",)
#         x1=x2+10
#         x2+=60    
    
# x1=30
# x2=80
# y1=120
# y2=170
# for i in range(10):
#     if i == numOfColor:
#         cavas.create_oval(x1,y1,x2,y2, fill="blue", tags="PNCTarget1")
    
#     else:
#         cavas.create_oval(x1,y1,x2,y2, fill="blue")

#     x1=x2+10
#     x2+=60


# cavas.tag_bind("PNCTarget1","<Button-1>",myEventTrigger)

# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()






import tkinter as tk;
import random

root=tk.Tk()
root.geometry("500x500")

frame=tk.Frame()

frame.master.title("PNC")
canvas=tk.Canvas(frame)




randR=random.randint(0,10)
def textResul(event):
    canvas.create_text(200,200,text="You Win!",font=("Purisa",30))
    canvas.delete("secret")
    valueX=0
    valueY=0
    for e in range(7):
        if e==randR:
            canvas.create_oval(valueX+10,valueY+30,valueX+70,valueY+90,fill="yellow")
        valueX+=70
    
valueX=0
valueY=0
for i in range(7):
        if i==randR:
            canvas.create_oval(valueX+10,valueY+70,valueX+70,valueY+130,fill="red",tags="secret")
        else:
            canvas.create_oval(valueX+10,valueY+70,valueX+70,valueY+130,fill="blue")
        valueX+=70

canvas.tag_bind("secret","<Button-1>",textResul)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()