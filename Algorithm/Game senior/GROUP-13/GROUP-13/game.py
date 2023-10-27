import tkinter as tk
from tkinter import *
import winsound
from random import randrange

# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root)

# ---------------------------------------------------------------------------
#=> VARIABLES
# ---------------------------------------------------------------------------
game_play = tk.PhotoImage(file="image/background.png")
game_start = tk.PhotoImage(file="image/game_start.png")
game_win = tk.PhotoImage(file="image/game_win.png")
game_help = tk.PhotoImage(file="image/game_help.png")
game_over = tk.PhotoImage(file="image/game_over.png")

hero = tk.PhotoImage(file="image/hero.png")
small_Virus = tk.PhotoImage(file="image/virus_small.png")
big_Virus = tk.PhotoImage(file="image/virus_big.png")
died_Virus = tk.PhotoImage(file="image/virus_died.png")
bulletKill = tk.PhotoImage(file="image/bullet.png")
cash_img = tk.PhotoImage(file="image/cash.png")
heard = tk.PhotoImage(file="image/heard.png")
heard_black = tk.PhotoImage(file="image/heard_black.png")

btn_start_game = tk.PhotoImage(file="image/btn_start_game.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit_game.png")
btn_help_game = tk.PhotoImage(file="image/btn_help_game.png")
btn_back = tk.PhotoImage(file="image/btn_back.png")
btn_replay = tk.PhotoImage(file="image/btn_replay.png")
btn_retry = tk.PhotoImage(file="image/btn_retry.png")

player_X = 150
player_Y = 450
enamyX = 1400
listOfDiedVirus = []
listOfBullet = []
listOfLives = []
listOfVirus = []
listOfCash = []
numberOfBullet = 45
numberOfVirus = 30
canLive = 6
createVirusSize = 0
countCreateVirus = 0
killVirus = 0
toConfig = 0
totalCash = 0
isStart = True

# ---------------------------------------------------------------------------
#=> FUNCTIONS GAME
# ---------------------------------------------------------------------------
# ==============> Game Process <==================
def processGame():
    if numberOfVirus == 0 and canLive != 0:
        gameWin()
    if numberOfBullet == 0:
        gameOver()
    canvas.after(100, processGame)

# ==================> Game Show <=================
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")
    canvas.create_image(680,540,image=btn_help_game, tags="help")

# ===============> Game Start <===================
def gameStart(event):
    global player, displayKillVirus, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    player = canvas.create_image(player_X, player_Y, image=hero)
    displayKillVirus = canvas.create_text(1087, 47, text=numberOfVirus, font=("serif", 18 ,'bold'), fill="black")
    displayTotalCash = canvas.create_text(1200, 47, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    displayNumeberBullet = canvas.create_text(1310, 47, text=numberOfBullet, font=("serif", 18 ,'bold'), fill="black")

    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)

    createVirusAndSize()
    createCanLive()
    checkBulletMeetVirus()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# =================> Game Win <===================
def gameWin():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_win)
    canvas.create_text(1200, 143, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=numberOfBullet, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,420, image=btn_replay, tags="replay")
    canvas.create_image(680,550,image=btn_exit_game, tags="exit")

# =================> Game Over <==================
def gameOver():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_over)
    canvas.create_text(1200, 143, text=killVirus, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 293, text=numberOfBullet, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,440, image=btn_retry, tags="replay")
    canvas.create_image(680,570,image=btn_exit_game, tags="exit")

# ==================> Game Help <==================
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 200, image=btn_back, tags="back")

# ==================> Game Exit <==================
def gameExit(event):
    root.destroy()

# ================> Game Restart <=================
def gameRestart(event):
    global player_X,player_Y,numberOfVirus,killVirus,numberOfBullet,createVirusSize,countCreateVirus,canLive,toConfig,totalCash,isStart,listOfVirus,listOfBullet,listOfLives,listOfCash
    isStart = True
    player_X = 150
    player_Y = 450
    numberOfBullet = 45
    numberOfVirus = 30
    canLive = 6
    createVirusSize = 0
    countCreateVirus = 0
    killVirus = 0
    toConfig = 0
    totalCash = 0
    listOfVirus = []
    listOfBullet = []
    listOfLives = []
    listOfCash = []
    gameStart(event)

# =================> Player Up <===================
def movePlayerUp(event):
  global player_Y
  if player_Y > 130:
    player_Y -= 20
    canvas.moveto(player, player_X-80, player_Y-70)

# ================> Player Down <==================
def movePlayerDown(event):
  global player_Y
  if player_Y < 650:
    player_Y += 20
    canvas.moveto(player, player_X-80, player_Y-70)

# =============> Create Virus Size <===============
def createVirusAndSize():
    global createVirusSize, countCreateVirus, enamyX
    createVirusSize += 1
    countCreateVirus += 1
    enamyY = randrange(150, 650)
    samllVirus = canvas.create_image(enamyX, enamyY, image=small_Virus)
    moveSmallVirus(samllVirus)
    if createVirusSize == 9:
        enamyX = 1600
        createVirusSize = 0
        bigVirus = canvas.create_image(enamyX, enamyY, image=big_Virus)
        moveBigVirus(bigVirus)
    if isStart and countCreateVirus < 27:
        canvas.after(1300, lambda:createVirusAndSize())

# ==============> Move Small Virus <==================
def moveSmallVirus(smallVirus):
    global listOfVirus, canLive, toConfig, numberOfVirus
    canvas.move(smallVirus,-8, 0)
    listOfVirus.append(smallVirus)
    positionSmallVirus = canvas.coords(smallVirus)
    if len(positionSmallVirus) > 0:
        if positionSmallVirus[0] < 20:
            deleteItem(smallVirus)
            numberOfVirus -= 1
            toConfig -= 1
            canLive -= 1
            canvas.itemconfig(listOfLives[toConfig], image=heard_black)
            canvas.itemconfig(displayKillVirus, text=numberOfVirus)
            winsound.PlaySound("sound/live.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    if canLive <= 0:
        gameOver()
        winsound.PlaySound("sound/over.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    if numberOfVirus == 0 and canLive != 0:
        winsound.PlaySound("sound/win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    if isStart:
        canvas.after(100, lambda:moveSmallVirus(smallVirus))

# ===============> Move Big Virus <==================
def moveBigVirus(bigVirus):
    global listOfVirus, canLive
    canvas.move(bigVirus, -8, 0)
    listOfVirus.append(bigVirus)
    positionBigVirus = canvas.coords(bigVirus)
    if len(positionBigVirus) > 0:
        if positionBigVirus[0] < 50:
            deleteItem(bigVirus)
            canLive -= 6
    if isStart:
        canvas.after(20, lambda:moveBigVirus(bigVirus))

# ====================> Create Bullet <==================
def createBullet(event):
    global numberOfBullet
    if isStart:
        numberOfBullet -= 1
        canvas.itemconfig(displayNumeberBullet, text=numberOfBullet)
        bullet = canvas.create_image(player_X+28, player_Y+10, image=bulletKill)
        moveBullet(bullet)
        winsound.PlaySound("sound/bullet.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    if numberOfBullet == 0:
        winsound.PlaySound("sound/over.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ====================> Move Bullet <====================
def moveBullet(bullet):
    canvas.move(bullet,+120, 0)
    listOfBullet.append(bullet)
    canvas.after(100, lambda:moveBullet(bullet))

# =============> Check Bullet Meet Virus <===============
def checkBulletMeetVirus():
    global listOfVirus, listOfBullet
    for bullet in listOfBullet:
        positionBulllet = canvas.coords(bullet)
        for virus in listOfVirus:
            positionVirus = canvas.coords(virus)
            if len(positionVirus) > 0 and len(positionBulllet) > 0:
                if (positionBulllet[0]+80 >= positionVirus[0]-80 and positionBulllet[0]-80 <= positionVirus[0]+80) and (positionBulllet[1]-20 <= positionVirus[1]+20 and positionBulllet[1]+20 >=  positionVirus[1]-20):
                    toDeleteVirus(bullet, virus, positionVirus[0], positionVirus[1])
                elif positionBulllet[0] > 1150:
                    deleteItem(bullet)

    listOfVirus = []
    listOfBullet = []
    canvas.after(100, lambda:checkBulletMeetVirus())

# ==========> Delete Bullet, Virus, And Cash <============
def deleteItem(item):
    canvas.delete(item)

# ==============> Delete Virus Meet Bullet <==============
def toDeleteVirus(bullet, virus, virus_X, virus_Y):
    global numberOfVirus, killVirus
    numberOfVirus -= 1
    killVirus += 1
    deleteItem(bullet)
    deleteItem(virus)
    canvas.itemconfig(displayKillVirus, text=numberOfVirus)
    createVirusDied(virus_X, virus_Y)
    winsound.PlaySound("sound/virus.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ==================> Create Virus Died <==================
def createVirusDied(virus_X, virus_Y):
    global listOfDiedVirus
    Virus_died = canvas.create_image(virus_X, virus_Y, image=died_Virus)
    listOfDiedVirus.append(Virus_died)
    if len(listOfDiedVirus) > 2:
        createCash()
        deleteItem(listOfDiedVirus[0])
        listOfDiedVirus.remove(listOfDiedVirus[0])

# ====================> Create Cash <====================== 
def createCash():
    positionCash = canvas.coords(listOfDiedVirus[2])
    cash = canvas.create_image(1400, positionCash[1], image=cash_img)
    moveCash(cash)

# ====================> Move Cash <========================
def moveCash(cash):
    global totalCash
    canvas.move(cash, -5, 0)
    listOfCash.append(cash)
    positionCash = canvas.coords(cash)
    if len(positionCash) > 0:
        if (player_X +20 >= positionCash[0] and player_X-20 <= positionCash[0]) and (player_Y-20 <= positionCash[1]+20 and player_Y+40 >=  positionCash[1]-20):
            totalCash += 25
            deleteItem(cash)
            canvas.itemconfig(displayTotalCash, text=totalCash)
            winsound.PlaySound("sound/cash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif positionCash[0] < 0:
            deleteItem(cash)
    canvas.after(50, lambda:moveCash(cash))

# ====================> Draw Can Live <====================
def createCanLive():
    for i in range(canLive):
        live = canvas.create_image(i*37+40, 40, image=heard)
        deleteItem(live)

# ---------------------------------------------------------------------------
#=> CREATE GAME SHOW
# ---------------------------------------------------------------------------
canvas.create_image(680, 372, image=game_start)
canvas.create_image(680,280, image=btn_start_game, tags="startgame")
canvas.create_image(680,410,image=btn_exit_game, tags="exit")
canvas.create_image(680,540,image=btn_help_game, tags="help")
winsound.PlaySound("sound/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ---------------------------------------------------------------------------
#=> AUTO PLAY
# ---------------------------------------------------------------------------
processGame()

# ---------------------------------------------------------------------------
#=> ALLOW WINDOWS KEYS AND TAGES BIND
# ---------------------------------------------------------------------------
root.bind("<w>", movePlayerUp)
root.bind("<s>", movePlayerDown)
root.bind("<Button-3>", createBullet)
canvas.tag_bind("startgame","<Button-1>", gameStart)
canvas.tag_bind("replay","<Button-1>", gameRestart)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", gameHelp)

# ---------------------------------------------------------------------------
#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
root.mainloop()