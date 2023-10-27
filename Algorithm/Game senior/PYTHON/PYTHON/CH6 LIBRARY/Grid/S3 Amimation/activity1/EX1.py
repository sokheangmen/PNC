# import tkinter as tk


# def displayHelloWorld():
#     canvas.create_text(300,300, text = "Hello world")


# # Create an empty window
# root = tk.Tk() 
# root.geometry("600x600")
# frame = tk.Frame() 
# canvas = tk.Canvas(frame)



# canvas.after(5000, lambda:displayHelloWorld())



# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')
# root.mainloop()




import tkinter as tk


def displayHelloWorld():
    for row in range(10):
        for col in range(10):
            canvas.create_oval(50*col,50*row,(50*col)+50,(50*row)+50 ,fill="red")
    # canvas.create_text(300,300, text = "Hello world")


# Create an empty window
root = tk.Tk() 
root.geometry("600x600")
frame = tk.Frame() 
canvas = tk.Canvas(frame)



canvas.after(5000, lambda:displayHelloWorld())



canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()