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
# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1=30
# x2=80
# y1=20
# y2=70
# for y in range(10):
#     for x in range(10):
#         if (y==0 and x>=0) or (y>=0 and x==0) or (y==9 and x>=1) or (y>=1 and x==9)  :
#             cavas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors) , outline="" )
#         elif (x<=4 and y<=4)and (x>=0 and y>=0):
#             cavas.create_rectangle((x1-45)*2,(y1-40)*2,(x2-39)*2,(y2-35)*2,fill=random.choice(colors) , outline="")

#         x1= x2+10
#         x2+=60
#     y1=y2+10
#     y2+= 60
#     x1=30
#     x2=80
        
    
# to display all frame
cavas.pack(expand=True, fill='both')
fram.pack(expand=True, fill="both")
root.mainloop()




