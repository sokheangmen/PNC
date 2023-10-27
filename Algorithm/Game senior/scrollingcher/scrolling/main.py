import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
import random

WIN_WIDTH = 1400
WIN_HEIGHT = 740
SCROLLING_SPEED = 5


root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("img/piture.png")


pic_giant = tk.PhotoImage(file="img/gaint.png")
pic_diamond = tk.PhotoImage(file="img/daimond.png")

image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH, 0,anchor=tk.NW, image=background_image)


def scroll_bg_image():
    
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)

    if canvas.coords(background_image_label_1)[0]< -1400:
        canvas.coords(background_image_label_1, 1400, 0)
    elif canvas.coords(background_image_label_2)[0]< -1400:
        canvas.coords(background_image_label_2, 1400, 0)
    canvas.after(5, scroll_bg_image)
    diamond_positions = [(670, 570),(750, 570),(830, 520),(930, 470),(1000, 470),(1170, 470)]
    goomba_positions = [(470, 550),(1080, 465)]
    player = canvas.create_rectangle(900, 510, 1200, 560, fill="green")
    player = canvas.create_rectangle(800, 560, 1200, 610, fill="brown")

    for position in diamond_positions:
        diamond = canvas.create_image(position[0], position[1], image=pic_diamond)
   
    for position in goomba_positions:
        goomba = canvas.create_image(position[0], position[1], image=pic_giant)
   
    winsound.PlaySound("sound/game-show.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
winsound.PlaySound("sound/gameshow.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
scroll_bg_image()
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()

