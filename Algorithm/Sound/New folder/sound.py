import tkinter as tk
import random
import winsound
def create_random_oval():
    winsound.PlaySound("mixkit.wav",winsound.SND_ASYNC)
    oval_height = oval_width= random.randint(10, 100)
    oval_x = random.randint(0, 400)
    oval_y = random.randint(0, 300)
    oval_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    canvas.create_oval(oval_x, oval_y, oval_x + oval_width, oval_y + oval_height, fill=oval_color)
    window.after(1000, create_random_oval)
window = tk.Tk()
window.title("Random Oval")
window.geometry("500x400")
canvas = tk.Canvas(window, width=500, height=400)
canvas.pack()
window.after(1000, create_random_oval)
window.mainloop()