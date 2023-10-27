import tkinter as tk
import random
import winsound

root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Durring game")
canvas = tk.Canvas(frame)

def create_randdom_circle(event):
    colors = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    size = random.randint(20,200)
    x = event.x - size // 2
    y = event.y - size // 2
    canvas.create_oval(x, y, x + size, y + size, fill=colors)
    winsound.PlaySound("game.wav",winsound.SND_ASYNC)


canvas.bind("<Button-1>", create_randdom_circle)

canvas.pack(expand=True , fill="both")
frame.pack(expand=True, fill='both')

root.mainloop()