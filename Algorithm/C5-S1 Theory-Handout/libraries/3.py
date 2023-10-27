# import tkinter as tk
# root=tk.Tk()
# root.geometry("600x200")
# # frame=tk.Frame()
# root.title("hllo PNC")

# canvas = tk.Canvas(root)
# canvas.pack()
# canvas.create_rectangle(10, 20, 50, 100)
# canvas.create_oval(10, 20, 50, 100 ,fill="#FFFF00", outline="#FF0000")
# canvas.create_line(10, 20, 50, 100 ,fill="red")
# canvas.create_text(10, 20 ,text="Just do it")


# root.mainloop()

import tkinter as tk
window = tk.Tk()
window.geometry("600x200")
window.title("Clon")
frame = tk.Frame(window)
frame.pack()
canvas = tk.Canvas(frame, width=1480, height=970)
canvas.pack()
rectangle = canvas.create_rectangle(10, 10, 50, 50, fill="red")
oval = canvas.create_oval(500, 500, 550, 550, fill="black")
window.mainloop()