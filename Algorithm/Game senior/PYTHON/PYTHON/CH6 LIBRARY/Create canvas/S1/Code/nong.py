# 1
# from random import shuffle
# students=["Chanthy","Bunthoeun","Sreyleak","Nika","Sambo"]
# shuffle(students)
# print(students)

#2
# import random
# for i in range(3):
#     print("Number "+str(i+1)+" : "+str(random.randrange(0, 100)))
# # 3
# import random 
# nameOfinput=str(input("What is your name ? "))
# name=["Chanthy","Bunthoeun","Sreyleak","Nika","Sambo"]
# print(nameOfinput +" secret lover is "+random.choice(name))


# create window#
# import tkinter as tk
# root =tk.Tk()
# root.geometry("300x150")
# frame =tk.Frame()
# frame.master.title("Hello thanna")
# root.mainloop()




# from curses import window
# import tkinter as tk;
# root =tk.Tk()
# root.geometry("850x800")
# frame =tk.Frame()
# frame.master.title("Hello thanna")
# canvas =tk.Canvas(frame)
#                 # (x1,y1,x2,y2)
# canvas.create_oval(200,100,400,200, fill="red")
# canvas.create_oval(290,100,320,200, fill="blue")
# canvas.create_oval(450,100,650,200, fill="blue")
# canvas.create_oval(540,100,570,200, fill="red")
# canvas.create_oval(340,300,500,420, fill="red")
# canvas.create_rectangle(200,600,650,620, fill="red")#
# canvas.create_rectangle(200,550,220,620, fill="red")
#                     # (x1,y1,x2,y2)
# canvas.create_rectangle(630,600,650,570, fill="red")
# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill="both")
# root.mainloop()


import tkinter as tk;
root=tk.Tk()
root.geometry("800x400")
frame=tk.Frame()
frame.master.title("page window")
canvas=tk.Canvas(frame)
                        # (x1,y1,x2,y2)
canvas.create_rectangle(360,170,440,230, fill="#2FF7F1")
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill="both")
root.mainloop()