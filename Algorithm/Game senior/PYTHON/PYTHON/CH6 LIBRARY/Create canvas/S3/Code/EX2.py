# from textwrap import fill
# import tkinter as tk
# import random
# root=tk.Tk()
# WIDTH=800
# HIGHT=600
# root.geometry(str(WIDTH)+"x"+str(HIGHT))
# frame=tk.Frame()
# frame.master.title("Nong page")
# canvas=tk.Canvas(frame)
# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1=100
# x2=160
# y1=100
# y2=160  
# for y in range(5):
#     for x in range(5):
#         if x==y:
#             canvas.create_oval(x1,y1,x2,y2,fill="red")
#         else:
#             canvas.create_oval(x1,y1,x2,y2,fill="blue")
#         x1+=60
#         x2+=60
#     y1+=60
#     y2+=60    
#     x1=100
#     x2=160
# canvas.pack(expand=True,fill=("both"))
# frame.pack(expand=True,fill=("both"))
# root.mainloop()