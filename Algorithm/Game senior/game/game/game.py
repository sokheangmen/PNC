import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import winsound
import random
from random import randrange

# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Super runner')
canvas = tk.Canvas(root)

#-------------------
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 15

TIMED_LOOP = 10
#-------------------


# ---------------------------------------------------------------------------

# _________________________________________Images______________________________

icon = tk.PhotoImage(file='image/hero.png')
root.iconphoto(True,icon)
root.resizable(0,0)

game_play = tk.PhotoImage(file="image/background.png")
game_level2 = tk.PhotoImage(file="image/background_l2.png")
game_level3 = tk.PhotoImage(file="image/background_l3.png")


game_start = tk.PhotoImage(file="image/game_start.png")
win_page = tk.PhotoImage(file="image/win_page.png")
game_help = tk.PhotoImage(file="image/help.png")
game_over = tk.PhotoImage(file="image/game_over.png")
#__________hero________
hero = tk.PhotoImage(file="image/hero.png")
hero_left = tk.PhotoImage(file="image/hero_left.png")

#_______________
cash_img = tk.PhotoImage(file="image/cash.png")
heard = tk.PhotoImage(file="image/heard.png")
heard_black = tk.PhotoImage(file="image/heard_black.png")

btn_start_game = tk.PhotoImage(file="image/btn_start_game.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit_game.png")
btn_help_game = tk.PhotoImage(file="image/btn_help_game.png")
btn_back = tk.PhotoImage(file="image/btn_back.png")
btn_back_new = tk.PhotoImage(file="image/back.png")
btn_back_win = tk.PhotoImage(file="image/back_win.png")
btn_replay = tk.PhotoImage(file="image/btn_replay.png")
btn_retry = tk.PhotoImage(file="image/btn_retry.png")
btn_exit_lp = tk.PhotoImage(file="image/btn_exit_lp.png")
btn_next_level = tk.PhotoImage(file="image/next_level.png")

boom_file = Image.open("image/bom.png")
boom_size = boom_file.resize((60, 60))
boom_img = ImageTk.PhotoImage(boom_size)

fire_image = tk.PhotoImage(file="image/fire.png")

#friuts____________________________
apple_img = tk.PhotoImage(file='image/apple.png')
bery_img = tk.PhotoImage(file='image/bery.png')
chery_img = tk.PhotoImage(file='image/chery.png')
mango_img = tk.PhotoImage(file='image/mango.png')

fruits = [apple_img, bery_img, chery_img, mango_img]

#______btn-level_______
level_page = tk.PhotoImage(file='image/levels_page.png')
btn_level1 = tk.PhotoImage(file='image/btn_level1.png')
btn_level2 = tk.PhotoImage(file='image/btn_level2.png')
btn_level3 = tk.PhotoImage(file='image/btn_level3.png')

#___________________________
way_player =tk.PhotoImage(file='image/road.png')

way_player_l2 =tk.PhotoImage(file='image/road_l2.png')
way_car =tk.PhotoImage(file='image/car.png')
parash =tk.PhotoImage(file='image/parash.png')

#_______________________________Variable_____________________________________

player_X = 150
player_Y = 360
enamy_x = 1400
listOfLives = []
listOfCash = []
listOfBom = []
canLive = 6
toConfig = 0
totalCash = 0
totalBom = 0
isStart = True
#___

count_create_fruit = 0
count_create_bom = 0


#____

keyPressed = []

#-----------------------FUNCTIONS GAME-------------------------------------
# ______________________________ Game Process _________________________________
def processGame():  
    if totalCash > 5 :
        win_level1()
    if totalBom == 3:
        gameOver()

    canvas.after(100, processGame)

# ____________________________________ Game Show ______________________________________
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")
    canvas.create_image(680,540,image=btn_help_game, tags="help")
    
#__________________Chose levels______________________
def chose_levels(event):
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom,player,displayTotalCash
    isStart = True
    player_X = 150
    player_Y = 650
    canLive = 6
    toConfig = 0
    totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    canvas.delete("all")
    # interface page level
    canvas.create_image(680, 372, image=level_page)
    
    canvas.create_image(1250,70,image=btn_exit_lp, tags="exit")
    canvas.create_image(140, 70, image=btn_back, tags="back_to_show_game")
    #chose
    canvas.create_image(680,250,image=btn_level1, tags="level_1")
    canvas.create_image(680,400,image=btn_level2, tags="level_2")
    canvas.create_image(680,550,image=btn_level3, tags="level_3")

#__________________________________________
# ___________________________________ Game Start_________________________________
def level_one(event):
    global player, displayTotalCash,totalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    player = canvas.create_image(player_X, player_Y, image=hero)
    canvas.create_image(150, 780, image=way_player,tags="PLATFORM")
    canvas.create_image(700, 780, image=way_player,tags="PLATFORM")
    displayTotalCash = canvas.create_text(1200, 75, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    
    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)
    
    create_fruit()
    create_bom()
    gravity()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    
def level_two(event):
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom,player,displayTotalCash
    isStart = True
    player_X = 150
    player_Y = 650
    canLive = 6
    toConfig = 0
    totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_level2)
    player = canvas.create_image(player_X, player_Y, image=hero)
    
    canvas.create_image(690, 740, image=way_player_l2, tags="PLATFORM")
    canvas.create_image(390, 640, image=way_car, tags="PLATFORM")
    canvas.create_image(1200, 640, image=parash, tags="PLATFORM")
    
    displayTotalCash = canvas.create_text(1200, 75, text=totalCash, font=("serif", 18 ,'bold'), fill="white")

    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)

    create_fruit()
    create_bom()
    gravity()
    
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def level_three(event):
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom,player,displayTotalCash
    isStart = True
    player_X = 150
    player_Y = 650
    canLive = 6
    toConfig = 0
    totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_level3)
    player = canvas.create_image(player_X, player_Y, image=hero)
    canvas.create_image(150, 780, image=way_player,tags="PLATFORM")
    canvas.create_image(700, 780, image=way_player,tags="PLATFORM")
    displayTotalCash = canvas.create_text(1200, 75, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    
    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)
    
    create_fruit()
    create_bom()
    gravity()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    
# _____________________Game Win ____________________________
def win_level1():
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom,player,displayTotalCash
    isStart = True
    player_X = 150
    player_Y = 650
    canLive = 6
    toConfig = 0
    # totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    canvas.delete("all")

    canvas.create_image(680, 372, image=win_page)
    canvas.create_text(810, 366, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    
    canvas.create_image(250,520,image=btn_back_win, tags="back_to_chose_level")    
    canvas.create_image(680,520,image=btn_exit_game, tags="exit")
 
    canvas.create_image(1120,520,image=btn_next_level, tags="next_to_l2")

# _________________________ Game Over _____________________________

def gameOver():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_over)
    canvas.create_text(830, 535, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(120,100, image=btn_back_new, tags="replay")
        
# _______________________Game Help____________________

def bar_help(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(130, 50, image=btn_back, tags="back")

# __________________ Game Exit_______________

def gameExit(event):
    root.destroy()

#________________________________Player Jump______________________________________

def check_movement(dx = 0, dy = 0, checkGround = False):
    global player
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")
    if coord[0] + dx < 46 or coord[0] + dx >= SCREEN_WIDTH-100:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+20+ dx, coord[1] +21+ dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]-dx, coord[1]-hero.width())

    for platform in platforms:
        if platform in overlap:
            return False
    return True

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            root.after(TIMED_LOOP, jump, force-1)

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def move():
    if not keyPressed == []:
        x = 0
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if "Right" in keyPressed:
            x += SPEED
            canvas.itemconfig(hero,image=hero)
        if "Left" in keyPressed:
            
            canvas.itemconfig(hero,image=hero_left)
            x -= SPEED
        if check_movement(x):
            canvas.move(player, x, 0)
        root.after(TIMED_LOOP, move)

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    root.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

# ___________________________ Delete, bom, Cash ________________________
def delete_item(item):
    canvas.delete(item)

# _______________________________Create Cash___________________________________
def create_fruit():
    global count_create_fruit, enamy_x 
    count_create_fruit += 1
    enamy_y = randrange(360,655)
    speed_create = randrange(2100,4800)
    cash =canvas.create_image(enamy_x,enamy_y, image=fruits[random.randrange(0,4)] )
    move_fruit(cash)
    if isStart and count_create_fruit < 300:
        canvas.after(speed_create, lambda:create_fruit())
# ====================> Move Cash <========================
def move_fruit(fruit):
    global totalCash
    canvas.move(fruit, -3, 0)
    listOfCash.append(fruit)
    positionCash = canvas.coords(fruit)
    positionPlayer = canvas.coords(player)
    score = randrange(3,9)
    if len(positionCash) > 0:
        if (positionPlayer[0]+10 >= positionCash[0] and positionPlayer[0]-30 <= positionCash[0]) and (positionPlayer[1] <= positionCash[1]+20 and positionPlayer[1] >=  positionCash[1]-80):
            totalCash += score
            delete_item(fruit)
            canvas.itemconfig(displayTotalCash, text=totalCash)
            winsound.PlaySound("sound/cash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif positionCash[0] < 0:
            delete_item(fruit)
    canvas.after(30, lambda:move_fruit(fruit))  

# _____________________________________Create Boom______________________________________
def create_bom():
    global count_create_bom, enamy_x
    count_create_bom += 1
    enamy_y = randrange(500,655)
    speed_create = randrange(4500,9000)
    bom =canvas.create_image(enamy_x,enamy_y, image=boom_img )
    move_bom(bom)
    if isStart and count_create_bom < 50:
        canvas.after(speed_create, lambda:create_bom())

# _____________________________________Move Boom ______________________________________
def move_bom(bom):
    global totalBom, is_allow
    canvas.move(bom, -3, 0)
    listOfBom.append(bom)
    positionBom = canvas.coords(bom)
    positionPlayer = canvas.coords(player)
    if len(positionBom) > 0:
        if (positionPlayer[0] +20 >= positionBom[0] and positionPlayer[0]-20 <= positionBom[0]) and (positionPlayer[1]-20 <= positionBom[1]+20 and positionPlayer[1]+40 >=  positionBom[1]-20):
            totalBom += 1
            fire = canvas.create_image(positionBom[0],positionBom[1], image = fire_image)
            canvas.after(900, lambda:delete_item(fire))
            delete_item(bom)
            winsound.PlaySound("sound/cash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif positionBom[0] < 0:
            delete_item(bom)
    canvas.after(50, lambda:move_bom(bom))  

# _______________________Draw Can Live _____________________
def createCanLive():
    for i in range(canLive):
        live = canvas.create_image(i*37+40, 40, image=heard)
        delete_item(live)

    for i in range(canLive):
        live = canvas.create_image(i*37+40, 40, image=heard)
        delete_item(live)

#_____________________________CREATE GAME SHOW______________________________

canvas.create_image(680, 372, image=game_start)
canvas.create_image(680,280, image=btn_start_game, tags="startgame")
canvas.create_image(680,410,image=btn_exit_game, tags="exit")
canvas.create_image(680,540,image=btn_help_game, tags="help")
winsound.PlaySound("sound/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

#___________________________AUTO PLAY_____________________________________
processGame()

#_________________________ALLOW WINDOWS KEYS AND TAGES BIND____________________________

root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)

#______________________________________________________

canvas.tag_bind("replay","<Button-1>", chose_levels)

canvas.tag_bind("back_to_show_game","<Button-1>", gameShow)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", bar_help)

canvas.tag_bind("startgame","<Button-1>", chose_levels)#___________________

canvas.tag_bind("level_1","<Button-1>", level_one)
canvas.tag_bind("level_2","<Button-1>", level_two)
canvas.tag_bind("level_3","<Button-1>", level_three)

canvas.tag_bind("back_to_chose_level","<Button-1>", chose_levels)

canvas.tag_bind('next_to_l2', '<Button-1>',level_two)

canvas.tag_bind('next_to_l3', '<Button-1>',level_three)

#__________________________Display ROOT________________________________

canvas.pack(expand=True, fill='both')
root.mainloop()
