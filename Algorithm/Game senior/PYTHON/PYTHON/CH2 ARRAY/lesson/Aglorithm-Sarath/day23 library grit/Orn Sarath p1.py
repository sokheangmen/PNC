

import tkinter as tk;
import random
# import function from TK
root = tk.Tk()
# set TK window size 
root.geometry("640x100")

fram = tk.Frame()
# set title of frame
fram.master.title("PNC UI GAME")
cavas = tk.Canvas(fram)

numOfColor=random.randint(0,10)
x1=30
x2=80
y1=20
y2=70
for i in range(10):
    if i == numOfColor:
        cavas.create_oval(x1,y1,x2,y2, fill="red")
    else:
        cavas.create_oval(x1,y1,x2,y2, fill="blue")


    x1=x2
    x2+=50



# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()




# ==============================

# import tkinter as tk;
# import random
# # import function from TK
# root = tk.Tk()
# # set TK window size 
# root.geometry("640x600")

# fram = tk.Frame()
# # set title of frame
# fram.master.title("PNC UI GAME")
# cavas = tk.Canvas(fram)
# color=["red","blue","blue","blue","blue","blue","blue","blue","blue","blue"]
# random.shuffle(color)
# x1=30
# x2=80
# y1=20
# y2=70
# for i in color:
#     cavas.create_oval(x1,y1,x2,y2, fill=i)
#     x1=x2+10
#     x2+=60



# # to display all frame
# cavas.pack(expand=True, fill='both')
# fram.pack(expand=True, fill="both")
# root.mainloop()

