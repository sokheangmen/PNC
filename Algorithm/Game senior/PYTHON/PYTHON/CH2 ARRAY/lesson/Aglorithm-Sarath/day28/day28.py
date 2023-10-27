
# import random
# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# canvas = tk.Canvas(fram)
# canvas['bg']='pink'

# colors=["red","orange","yellow","green","purple","blue"]
# def drawCircle():
#     x1=random.randrange(0,600)
#     y1=random.randrange(0,600)
#     size=random.randrange(10,100)
#     x2=x1+size
#     y2=y1+size
#     canvas.create_oval(x1,y1,x2,y2,fill=random.choice(colors))
#     canvas.after(1000,drawCircle)


    
# def waitToDrawCircle(event):
#     print("space is pressed")
#     canvas.after(1000,drawCircle)

# root.bind('<space>',waitToDrawCircle)

# # to display all frame


# canvas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill='both')
# root.mainloop()



# ---------------------------------


# import random
# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# canvas = tk.Canvas(fram)
# canvas['bg']='pink'

# colors=["red","orange","yellow","green","purple","blue"]


    

# def moveCircle():
#     canvas.move(myCircle,10,10)
#     canvas.after(300,moveCircle)
# # to display all frame
# myCircle=canvas.create_oval(10,10,50,50,fill=random.choice(colors))

# moveCircle()

# canvas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill='both')
# root.mainloop()


# ==================================================


import random
import tkinter as tk;
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
canvas = tk.Canvas(fram)
canvas['bg']='pink'

colors=["red","orange","yellow","green","purple","blue"]


x = 0
y = 0
def moveCircle():
    global x 
    global y,  myCircle
    if x < 550:
        canvas.move(myCircle,0,10)
        canvas.after(300,moveCircle)
        x += 10
    elif y < 550:
        canvas.move(myCircle,0,-10)
        canvas.after(100,moveCircle)
        y += 10
        if y == 550:
            x = 0
            y = 0
    print(x,y)

# to display all frame
# myCircle=canvas.create_oval(10,10,50,50,fill=random.choice(colors))
# moveCircle()

def a():
    global myCircle
    myCircle=canvas.create_rectangle(20,20,60,60,fill=random.choice(colors))
    myCircle=canvas.create_oval(10,10,50,50,fill=random.choice(colors))
    moveCircle()
    # moveCircle()
    # canvas.after(500,a)

a()
canvas.pack(expand=True, fill='both')
fram.pack(expand=True, fill='both')
root.mainloop()





# import tkinter as tk
# import time

# def current_iso8601():
#     """Get current date and time in ISO8601"""
#     # https://en.wikipedia.org/wiki/ISO_8601
#     # https://xkcd.com/1179/
#     return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.now = tk.StringVar()
#         self.time = tk.Label(self, font=('Helvetica', 24))
#         self.time.pack(side="top")
#         self.time["textvariable"] = self.now

#         self.QUIT = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
#         self.QUIT.pack(side="bottom")

#         # initial time display
#         self.onUpdate()

#     def onUpdate(self):
#         # update displayed time
#         self.now.set(current_iso8601())
#         # schedule timer to call myself after 1 second
#         self.after(1000, self.onUpdate)

# root = tk.Tk()
# app = Application(master=root)
# root.mainloop()




# import tkinter as tk
# from tkinter import *
# from tkinter import ttk

# class karl( Frame ):
#     def __init__( self ):
#         tk.Frame.__init__(self)
#         self.pack()
#         self.master.title("Karlos")
#         self.button1 = Button( self, text = "CLICK HERE", width = 25,
#                                command = self.new_window )
#         self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
#     def new_window(self):
#         self.newWindow = karl2()
# class karl2(Frame):     
#     def __init__(self):
#         new =tk.Frame.__init__(self)
#         new = Toplevel(self)
#         new.title("karlos More Window")
#         new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
#                                  command = self.close_window )
#         new.button.pack()
#     def close_window(self):
#         self.destroy()
# def main(): 
#     karl().mainloop()
# if __name__ == '__main__':
#     main()
