#===import===
import tkinter as tk
from tkinter import *
import winsound
# from random import randrange


#===Constan===

SCREEN_WIDTH =1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Mario Jumper')
canvas = tk.Canvas(root)

#====Variable===
game_page1 = tk.PhotoImage(file="img/page1.png")
game_introductio = tk.PhotoImage(file="img/introduction.png")
game_level = tk.PhotoImage(file="img/level.png")
game_play = tk.PhotoImage(file="img/play.png")


game_lower = tk.PhotoImage(file="img/lower.png")
pic_mario = tk.PhotoImage(file="img/mario.png")
pic_giant = tk.PhotoImage(file="img/diamond.png")
pic_goomba = tk.PhotoImage(file="img/heart.png")
# pic_Introduction = tk.PhotoImage(file="img/pageintroduction")

btn_back = tk.PhotoImage(file="img/back.png")

player_X = 150
player_Y = 450
enamyX = 1400
listOfDiedVirus = []
listOfBullet = []
listOfLives = []
listOfVirus = []
listOfCash = []



isStart = True
isMario= 1
marioMeetenemy = 0
isGoomba =0
isGiantstick=0
level1 = 0
level2 =0
marioCanLive=0
killVirus = 0
toConfig = 0
totalCash = 0
#===Function===
 
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_page1) 
    canvas.create_image(680,280, image=game_introductio, tags="introduction")
    canvas.create_image(680,410,image=game_level, tags="level")
    canvas.create_image(680,520 ,image=game_play, tags ="play")



def gameIntroduction(event):
    canvas.delete("all")
    canvas.create_image(640, 360, image=game_lower)
    # canvas.create_image(140, 200, image=btn_back, tags="back")




   
   


#===create game show ===

canvas.create_image(640, 372, image=game_page1)
canvas.create_image(870,280, image=game_introductio, tags="introduction")
canvas.create_image(870,410,image=game_level, tags="level")
canvas.create_image(870,520 ,image=game_play, tags ="play")
canvas.tag_bind("introduction","<Button-1>", gameIntroduction)



#===Main roo===
canvas.pack(expand=True, fill='both')
root.mainloop()


