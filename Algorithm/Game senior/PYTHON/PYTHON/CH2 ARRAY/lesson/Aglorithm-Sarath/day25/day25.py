# import tkinter as tk
# import random

# def changeColorYellow(event):
#     oval = canvas.create_oval(50, 50, 300, 300, fill="yellow", tags="shapeYellow", outline="")
#     print('Key pressed: ', event.char)
#     # message = tk.Label(text='You cliked on: ' + str(event.char))
#     # message.pack()

# def changeColorRed(event):
#     oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags="shapeRed", outline="")
#     print('Key pressed: ', event.char)
#     # message = tk.Label(text='You cliked on: ' + str(event.char))
#     # message.pack()

# # Create window empty
# root = tk.Tk()
# root.geometry("600x600")
# message = tk.Label(text="Hello, Tkinter")
# message.pack()

# canvas = tk.Canvas(root)
# oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags="shape", outline="")


# # canvas.tag_bind("shape", "<Button-1", changeColorYellow)
# # canvas.tag_bind("shape", "<Button-3", changeColorRed)

# root.bind('<Button-3>', changeColorYellow)
# root.bind('<Button-1>', changeColorRed)

# # KeyBoardEvent 
# root.bind('<Key>', changeColorYellow)
# root.bind('<Up>', changeColorRed)

# canvas.pack(expand=True, fill="both")
# root.mainloop()







# import tkinter as tk;
# import random

# root=tk.Tk()
# root.geometry("500x500")

# frame=tk.Frame()

# frame.master.title("PNC")
# canvas=tk.Canvas(frame)




# randR=random.randint(0,10)
# def textResul(event):
#     canvas.create_text(200,200,text="You Win!",font=("Purisa",30))
#     canvas.delete("secret")
#     valueX=0
#     valueY=0
#     for e in range(7):
#         if e==randR:
#             canvas.create_oval(valueX+10,valueY+30,valueX+70,valueY+90,fill="yellow")
#         valueX+=70
    
# valueX=0
# valueY=0
# for i in range(7):
#         if i==randR:
#             canvas.create_oval(valueX+10,valueY+70,valueX+70,valueY+130,fill="blue",tags="secret")
#         else:
#             canvas.create_oval(valueX+10,valueY+70,valueX+70,valueY+130,fill="blue")
#         valueX+=70

# canvas.tag_bind("secret","<Button-1>",textResul)

# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()





# --------------------------------------------



from random import random
import tkinter as tk;
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)
a = cavas.create_text(70,70, text=0, font=("",40), tags="Number")

def incrementScore(event):
    global score 
    score=score+1
    cavas.itemconfig(a, text=score)

score=0


# to display all frame
cavas.create_oval(200,200,450,450,fill="red",tags="Number")

cavas.tag_bind("Number","<Button-1>",incrementScore)
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill='both')
root.mainloop()