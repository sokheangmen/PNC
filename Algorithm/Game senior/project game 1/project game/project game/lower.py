import tkinter as tk
from PIL import Image, ImageTk

WIN_WIDTH = 1400
WIN_HEIGHT = 700
SCROLLING_SPEED = 10
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
root.title('lowerLewel')
frame = tk.Frame()
canvas = tk.Canvas(frame)
pic_mario = tk.PhotoImage(file="img/mario.png")

original_image = Image.open("img/lower.png")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)
background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH, 0,anchor=tk.NW, image=background_image)

def scroll_bg_image():
    player = canvas.create_image(100,500,image=pic_mario )
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)
    

    if canvas.coords(background_image_label_1)[0]< -800:
        canvas.coords(background_image_label_1, 800, 0)
    elif canvas.coords(background_image_label_2)[0]< -800:
        canvas.coords(background_image_label_2, 800, 0)

    canvas.after(5, scroll_bg_image)
    

scroll_bg_image()



canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()