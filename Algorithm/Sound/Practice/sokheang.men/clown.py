import tkinter as tk
window = tk.Tk()
window.geometry("600x600")
window.title("PNC UI GAME")
canvas = tk.Canvas()
canvas.pack()
canvas.create_oval(50, 100, 150, 50, fill="white")
canvas.create_oval(75, 50,125, 100, fill="blue")

canvas.create_oval(340, 100, 240, 50, fill="white")
canvas.create_oval(315, 50,265, 100, fill="blue")

canvas.create_oval(170, 200, 225, 150, fill="red")

canvas.create_rectangle(70, 310, 50, 220, fill="red")
canvas.create_rectangle(70, 310, 310, 250, fill="red")
canvas.create_rectangle(330, 280, 310, 230, fill="red")


window.mainloop()