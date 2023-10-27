# import tkinter as tk
# import random
# root=tk.Tk()
# root.geometry("700x600")
# frame=tk.Frame()
# frame.master.title("Events")
# canvas=tk.Canvas(frame)

# numberOfColor=random.randint(0,9)
# def myEventTrigger(event):
#     canvas.create_text(350,200,text="You win!",font=("Purisa", 50))
# x1=30
# x2=80
# y1=20
# y2=70
# for i in range(10):
#     if i==numberOfColor:
#         canvas.create_oval(x1 ,y1 ,x2 ,y2 ,fill="blue" ,tags="click")
#     else:
#         canvas.create_oval(x1 ,y1 ,x2 ,y2 ,fill="blue")
#     x1=x2+10 #(x1=80 and +spac10)                                   
#     x2+=60
# canvas.tag_bind("click" ,"<Button-1>",myEventTrigger)
# canvas.pack(expand=True,fill=("both"))
# frame.pack(expand=True,fill=("both"))
# root.mainloop()


n=[1,1,2,2]
j=[]
for i in n:
    if i not in j:
        j.append(i)
for r in j:
    print(r ,end=" ")
