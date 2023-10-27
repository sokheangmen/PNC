import tkinter as tk
window=tk.Tk()
canvas=tk.Canvas(window,width=800,height=600)
canvas.pack()
background_image=tk.PhotoImage(file="page.png")
def scroll_background(canvas,dx,dy):
    canvas.move(background_image, dx,dy)
    canvas.after(50, scroll_background, canvas, dx, dy)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
scroll_background(canvas, 1, 0)
window.mainloop()
    