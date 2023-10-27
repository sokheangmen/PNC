#_______________Ex1__________________
# total = 0
# def sum( arg1, arg2 ):
#     total = arg1 + arg2
#     print("Inside : ", total)
# sum(10,20)
# print("Outside : ", total)
#_______________Ex1__________________
# total = 0
# def sum( arg1, arg2 ):
#     total = arg1 + arg2
#     print("Inside : ", total)
# sum(10,20);
# print("Outside : ", total)

#_______________Ex1__________________
# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("GAME")
# cavas = tk.Canvas(fram)
# points = []
# def drawCircle(event):
#     points.append(event.x)
#     points.append(event.y)
#     print(points)
# def drawShape(event):
#     points = []
#     print(points)
# root.bind("<Button-1>", drawCircle) #LEFT CLICK
# # root.bind("<Button-3>", drawShape)
# cavas.pack(expand=True, fill="both")
# fram.pack(expand=True, fill="both")
# root.mainloop()
#_______________Ex1__________________


import tkinter as tk;
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("GAME")
cavas = tk.Canvas(fram)
points = []
points = []
def drawCircle(event):
    points.append(event.x)
    points.append(event.y)
    print(points)
def drawShape(event):
    global points
    points = []
print(points)

root.bind("<Button-1>", drawCircle) #LEFT CLICK
root.bind("<Button-3>", drawShape)
cavas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()

#_______________Ex1__________________
#_______________Ex1__________________
#_______________Ex1__________________