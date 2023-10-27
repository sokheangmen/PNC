#===import===
import tkinter as tk
from tkinter import *
import winsound
from PIL import Image, ImageTk
import random
from random import randrange,choice


#===Constan===
vertical_velocity = 0

WIN_WIDTH =1400
WIN_HEIGHT = 740
SCROLLING_SPEED = 10
ENEMY_SPEED = 5

root = tk.Tk()
root.geometry(str(WIN_WIDTH)+"x"+str(WIN_HEIGHT))
root.title('Mario Jumper')
canvas = tk.Canvas(root, scrollregion= (0,0,4000,5000)) 
frame = tk.Frame()

#====Variable===
game_page1 = tk.PhotoImage(file="img/page1.png")
game_lower = tk.PhotoImage(file="img/lower.png")

btn_introductio = tk.PhotoImage(file="img/btn_introduction.png")
btn_level = tk.PhotoImage(file="img/btn_level.png")
btn_play = tk.PhotoImage(file="img/btn_play.png")
btn_choose=tk.PhotoImage(file="img/btn_choose.png")
btn_lower= tk.PhotoImage(file="img/btn_lower.png")
btn_high= tk.PhotoImage(file="img/btn_high.png")
btn_meduim= tk.PhotoImage(file="img/btn_medium.png")



pic_mario = tk.PhotoImage(file="img/mario.png")
pic_introduction = tk.PhotoImage(file="img/introduction.png")
pic_level= tk.PhotoImage(file="img/level.png")
background_lower= tk.PhotoImage(file="img/lower.png")
background_high= tk.PhotoImage(file="img/high.png")
background_medium= tk.PhotoImage(file="img/medium.png")

diamond= tk.PhotoImage(file="img/diamond.png")
goomba= tk.PhotoImage(file="img/goomba.png")
giant_stick= tk.PhotoImage(file="img/Giant Stick.png")
heart= tk.PhotoImage(file="img/heart.png")
game_over_image=tk.PhotoImage(file="img/game-over.png")

btn_back = tk.PhotoImage(file="img/btn_back.png")


listOfDm = []
 


isStart = True
count_create_dm = 0
enamy_x = 450
enamy_x = 1350

score = 0
#===Function===
 
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_page1)
    canvas.create_image(870,280, image=btn_introductio, tags="introduction")
    canvas.create_image(870,410,image=btn_level, tags="level")
    canvas.create_image(870,520 ,image=btn_play, tags ="play")
    # winsound.PlaySound("sound/game-show.wav", winsound.SND_ASYNC)



#================================back ================================
def back():
    canvas.create_image(120, 50, image=btn_back, tags="back")
back()
#===introduction===
def gameIntroduction(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=pic_introduction)
    back()

    
#===lavel===
def gameLevel(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=pic_level)
    canvas.create_image(700,150, image=btn_choose, tags="choose")
    canvas.create_image(300,300, image=btn_lower, tags="lower")
    canvas.create_image(700,300, image=btn_high, tags="high")
    canvas.create_image(1100,300, image=btn_meduim, tags="medium")
    back()



#================================ Lower Level ================================


   
def lowerLevel(event):
    global player
    canvas.delete("all")
    background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_lower)
    background_image_label_2= canvas.create_image(1400, 0,anchor=tk.NW, image=background_lower)
    

    def scroll_bg_image():
        
        canvas.move(background_image_label_1, -1, 0)
        canvas.move(background_image_label_2, -1, 0)

        if canvas.coords(background_image_label_1)[0]<-1400:
            canvas.coords(background_image_label_1, 1400, 0)
        elif canvas.coords(background_image_label_2)[0]<-1400:
            canvas.coords(background_image_label_2, 1400, 0)
        canvas.after(10, scroll_bg_image)
   
    scroll_bg_image()
    
#==============================player=========================
    player = canvas.create_image(100, 500, image=pic_mario)
    back()

# ================== Play Game =============================

player = canvas.create_image(100, 500, image=pic_mario)

enemies = []
game_over_flag = False  

diamond_count = tk.IntVar()
diamond_count_label = tk.Label(root, textvariable=diamond_count)
diamond_count_label.place(x=10, y=10)


# ============= Create Enemy ================================

def create_enemy():
    if not game_over_flag: 
        x = WIN_WIDTH + 100
        y = random.randint(100, WIN_HEIGHT - 100)
        enemy_type = random.choice(["goomba", "giant_stick", "diamond"])  
        if enemy_type == "goomba":
            enemy_image = goomba
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        elif enemy_type == "giant_stick":
            enemy_image = giant_stick
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        elif enemy_type == "diamond": 
            enemy_image = diamond
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        enemies.append((enemy, enemy_type))
        canvas.after(random.randint(2000, 5000), create_enemy)

#  ============ Move Enemy ================================

def move_enemies():
    if not game_over_flag:  
        for enemy, enemy_type in enemies:
            if enemy_type == "goomba":
                canvas.move(enemy, -ENEMY_SPEED, 0)
            elif enemy_type == "giant_stick":
                canvas.move(enemy, -ENEMY_SPEED - 2, 0)
            elif enemy_type == "diamond":  
                canvas.move(enemy, -ENEMY_SPEED, 0)
            enemy_coords = canvas.coords(enemy)
            player_coords = canvas.coords(player)
            if collision_check(enemy_coords, player_coords):
                if enemy_type == "diamond": 
                    canvas.delete(enemy)
                    enemies.remove((enemy, enemy_type))
                    
                    diamond_count.set(diamond_count.get() + 1)
                else:
                    game_over()
                    return
            if enemy_coords[0] < -100:
                canvas.delete(enemy)
                enemies.remove((enemy, enemy_type))
        canvas.after(30, move_enemies)


def game_over():
    global game_over_flag
    game_over_flag = True
    canvas.delete(player)
    canvas.unbind("<Key>")
    # canvas.itemconfig(background_image_label_1, image=pic_game_over)
    # canvas.itemconfig(background_image_label_2, image=pic_game_over)

# ============= Check position Enemy ==============================

def collision_check(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    if abs(x1 - x2) < 50 and abs(y1 - y2) < 50:
        return True
    return False



#================move Plaer==================================
def move(event):
    global diamonds
    if event.keysym == "Left" and canvas.coords(player)[0] > 0:
        canvas.move(player, -10, 0)  # Move left (-10 in the x-axis)
    elif event.keysym == "Right" and canvas.coords(player)[0] < canvas.winfo_width():
        canvas.move(player, 10, 0)  # Move right (10 in the x-axis)
    elif event.keysym == "Down" and canvas.coords(player)[1] < canvas.winfo_height():
        canvas.move(player, 0, 10)  # Move down (10 in the y-axis)
    elif event.keysym == "Up" and canvas.coords(player)[1] > 0:
        canvas.move(player, 0, -10)  # Move up (-10 in the y-axis)
    
    player_coords = canvas.coords(player)
    for diamond in diamonds:
        diamond_coords = canvas.coords(diamond)
        if player_coords[0] == diamond_coords[0] and player_coords[1] == diamond_coords[1]:
            canvas.delete(diamond)  # Remove the picked up diamond from the canvas
            diamonds.remove(diamond)  # Remove the picked up diamond from the list
            print("Picked up a diamond!")
    
    print(canvas.coords(player))

root.bind("<Key>", move)



#================================ High Level ================================
def highLevel(event):
    global player
    canvas.delete("all")
    background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_high)
    background_image_label_2= canvas.create_image(1400, 0,anchor=tk.NW, image=background_high)

    def scroll_bg_image():
        
        canvas.move(background_image_label_1, -1, 0)
        canvas.move(background_image_label_2, -1, 0)

        if canvas.coords(background_image_label_1)[0]<-1400:
            canvas.coords(background_image_label_1, 1400, 0)
        elif canvas.coords(background_image_label_2)[0]<-1400:
            canvas.coords(background_image_label_2, 1400, 0)
        canvas.after(10, scroll_bg_image)
   
    scroll_bg_image()
#=====================player====================
    player = canvas.create_image(100, 500, image=pic_mario)
    back()

#================================ Medium Level ================================
def mediumLevel(event):
    global player
    canvas.delete("all")
    background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_medium)
    background_image_label_2= canvas.create_image(1400, 0,anchor=tk.NW, image=background_medium)

    def scroll_bg_image():
        
        canvas.move(background_image_label_1, -1, 0)
        canvas.move(background_image_label_2, -1, 0)

        if canvas.coords(background_image_label_1)[0]<-1400:
            canvas.coords(background_image_label_1, 1400, 0)
        elif canvas.coords(background_image_label_2)[0]<-1400:
            canvas.coords(background_image_label_2, 1400, 0)
        canvas.after(10, scroll_bg_image)
   
    scroll_bg_image()
#=====================player====================
    player = canvas.create_image(100, 500, image=pic_mario) 

    back()

    

#===create game show ===

canvas.create_image(680, 372, image=game_page1)
canvas.create_image(870,280, image=btn_introductio, tags="introduction")
canvas.create_image(870,410,image=btn_level, tags="level")
canvas.create_image(870,520 ,image=btn_play, tags ="play")
canvas.tag_bind("introduction","<Button-1>", gameIntroduction)
canvas.tag_bind("back","<Button-1>",gameShow)
canvas.tag_bind("level","<Button-1>",gameLevel)
canvas.tag_bind("lower","<Button-1>",lowerLevel)
canvas.tag_bind("high","<Button-1>",highLevel)
canvas.tag_bind("medium","<Button-1>",mediumLevel)
canvas.tag_bind("play","<Button-1>",lowerLevel)



#===Main roo===
canvas.pack(expand=True, fill='both')

root.mainloop()