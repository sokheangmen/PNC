# total=0
# def sum(arg1,arg2):
#     total=arg1+arg2
#     print("Inside",total)
# sum(10,20)
# print("Outside: ",total)

# ---------------------------------


# total=0
# def sum(arg1,arg2):
#     global total
#     total=arg1+arg2
#     print("Inside",total)
# sum(10,20)
# print("Outside: ",total)


# ---------------------------------
# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)

# points=[]
# def drawCircle(event):
#     points.append(event.x)
#     points.append(event.y)
#     print(points)
# def drawShape(event):
#     points=[]
#     print(points)

# #Left click
# root.bind("<Button-1>",drawCircle)
# # Right click
# root.bind("<Button-3>",drawShape)


# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()



# ----------------------------------------------

# import tkinter as tk;
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)

# points=[]
# def drawCircle(event):
#     points.append(event.x)
#     points.append(event.y)
#     print(points)
# def drawShape(event):
#     global points
#     points=[]
#     print(points)

# #Left click
# root.bind("<Button-1>",drawCircle)
# # Right click
# root.bind("<Button-3>",drawShape)


# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()

# --------------------------------------------

# a=0

# def myFunction():
#     global a
#     a=a+2
#     print("Inside",a)
# myFunction()
# print("Outside",a)

# ---------------------------------------------------------------------------

# 1=============================================

# import tkinter as tk;
# import random
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)

# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1=30
# x2=80
# y1=20
# y2=70
# for y in range(9):
#     for x in range(9):
#         cavas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
#         x1= x2+10
#         x2+=60
#     y1=y2+10
#     y2+= 60
#     x1=30
#     x2=80




# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()


# 2=========================================

import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("670x680")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
x1=30
x2=80
y1=20
y2=70
for y in range(10):
    # if y==0 or y==9
    for x in range(10):
        if (y==0 and x>=0) or (y>=0 and x==0) or (y==9 and x>=1) or (y>=1 and x==9)  :
            cavas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors) , outline="" )
        elif (x<=4 and y<=4)and (x>=0 and y>=0):
            cavas.create_rectangle((x1-45)*2,(y1-40)*2,(x2-39)*2,(y2-35)*2,fill=random.choice(colors) , outline="")

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




# 3=====================================



import tkinter as tk;
# import function from TK
import random
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)


color=['#ed1811','#56d10f','#11f5c0','#11bcf5','#118ef5','#5211f5','#c711f5','#f511da','#f5112f']
def change(event):
    # width=random.randrange(-50,300)
    y1=x1=random.randint(0,600)
    y2=x2=random.randint(0,600)

    cavas.create_oval(x1,y1,x2,y2,fill=random.choice(color), outline="")


# Right click
root.bind("<Button-1>",change)


# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()









# # 4

# import tkinter as tk;
# # import function from TK
# import random
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)


# color=['#ed1811','#56d10f','#11f5c0','#11bcf5','#118ef5','#5211f5','#c711f5','#f511da','#f5112f']
# def change(event):
#     width=random.randrange(1,300)
#     cavas.create_oval(event.x-width,event.y-width,event.x+width,event.y+width,fill=random.choice(color), outline="")


# # Right click
# root.bind("<Button-1>",change)


# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()



# ===================================5



import tkinter as tk;
# import function from TK
import random
root = tk.Tk()
# set TK window size 
root.geometry("600x600")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)


color=['#ed1811','#56d10f','#11f5c0','#11bcf5','#118ef5','#5211f5','#c711f5','#f511da','#f5112f']
point=[]
def draw(event):
    global point
    point.append(event.x)
    point.append(event.y)
    cavas.create_oval(event.x+5,event.y+5,event.x-5,event.y-5,tags="delete",outline = 'blue')
    


def add(event):   
    global point
    cavas.create_polygon(point, outline = '',fill =random.choice(color))
    cavas.delete("delete")
    point=[]
# Right click
root.bind("<Button-1>",draw)
root.bind("<Button-3>",add)


# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()







# ====================teacher1==========================================================

# import tkinter as tk;
# # import function from TK
# import random
# root = tk.Tk()
# # set TK window size 
# root.geometry("600x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)


# color=['#ed1811','#56d10f','#11f5c0','#11bcf5','#118ef5','#5211f5','#c711f5','#f511da','#f5112f']
# def drawCircle(event):
#     print('event triggered')
#     randomColor=random.choice(color)
#     print(randomColor)
#     randomNumber=random.randrange(1,10)
#     print(randomNumber)
#     x1=random.randrange(1,600)
#     y1=random.randrange(1,600)


#     size=random.randrange(20,100)
#     x2=x1+size
#     y2=y1+size


#     cavas.create_oval(x1,y1,x2,y2,fill=randomColor, outline="")






# # Right click
# root.bind("<Button-1>",drawCircle)


# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()




