# # 1

# import tkinter as tk
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("700x700")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("Sarath2022")
# def myEventTrigger(event):
#     print("User has clicked on circle")
# def myEventTrigger1(event):
#     print("User has clicked on square")
# def myEventTrigger2(event):
#     print("User has clicked on rectangle")

# canvas = tk.Canvas(fram)
# canvas.create_oval(50, 50, 300, 300, fill="red", tags="PNCTarget")
# canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)

# canvas.create_rectangle(320, 50, 570, 300, fill="blue", tags="PNCTarget1")
# canvas.tag_bind("PNCTarget1","<Button-1>",myEventTrigger1)

# canvas.create_rectangle(50, 350, 570, 600, fill="yellow", tags="PNCTarget2")
# canvas.tag_bind("PNCTarget2","<Button-1>",myEventTrigger2)
# canvas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()




# # 1
# import tkinter as sophim
# import random

# window = sophim.Tk()
# window.geometry("600x600")
# window.title("Hello PNC")
# frame = sophim.Frame()
# canvas = sophim.Canvas(frame)

# def colorRed(event):
#     canvas.itemconfig(oval,fill="yellow")
# def colorGreen(event):
#     canvas.itemconfig(oval,fill="green")
# oval = canvas.create_oval(100,50,300,250,fill="red",tags="true")
# canvas.tag_bind("true","<Button-1>", colorRed) 
# canvas.tag_bind("true","<Button-3>", colorGreen) 
# canvas.pack(expand= True, fill="both")
# frame.pack(expand=True, fill="both")
# window.mainloop()



# ------------------------------------------------------------------------------------------------------
import tkinter as tk
import random

def changeColorYellow(event):
    oval = canvas.create_oval(50, 50, 300, 300, fill="yellow", tags="shapeYellow", outline="")
    print('Key pressed: ', event.char)
    # message = tk.Label(text='You cliked on: ' + str(event.char))
    # message.pack()

def changeColorRed(event):
    oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags="shapeRed", outline="")
    print('Key pressed: ', event.char)
    # message = tk.Label(text='You cliked on: ' + str(event.char))
    # message.pack()

# Create window empty
root = tk.Tk()
root.geometry("600x600")
message = tk.Label(text="Hello, Tkinter")
message.pack()

canvas = tk.Canvas(root)
oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags="shape", outline="")


# canvas.tag_bind("shape", "<Button-1", changeColorYellow)
# canvas.tag_bind("shape", "<Button-3", changeColorRed)

root.bind('<Button-3>', changeColorYellow)
root.bind('<Button-1>', changeColorRed)

# KeyBoardEvent 
root.bind('<Key>', changeColorYellow)
root.bind('<Up>', changeColorRed)

canvas.pack(expand=True, fill="both")
root.mainloop()