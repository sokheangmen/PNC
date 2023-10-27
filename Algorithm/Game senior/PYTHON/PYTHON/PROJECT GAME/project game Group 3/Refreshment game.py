# _____________________________IMPORT____________________________________
import tkinter as tk
import winsound 

# _____________________________Constant___________________________________

WIN_WIDTH = 1280
WIN_HEIGHT = 700
BLOCK = 0
CELL = 1
CHICKEN = 2
MANGO = 3
STRAWBERRY = 10
APPLE = 15
CHERY = 8
BOURGER = 5
PIZZA = 6

# _____________________________Variables__________________________________
levelGrid = []
isreset=[False,False,False]
iswin=[True,False,False]
swtict = True
isAllowtomove = True
countwin = 0
Numstrawberry = 0
Numapple = 0
Numchery = 0
Nummango = 0
Numbourger = 0
Numpizza = 0
colorTime = 'black'

# _____________________________Function____________________________________
#  start game___________
def start(event):

    canvas.delete('all')
    songGame()
    canvas.create_image(0,0 , image=page1 , anchor='nw')

    # enter button
    canvas.create_image(550,300 , image=enter , anchor='nw' , tags='enter')
    canvas.create_text(588,325 , text='ENTER', font=('Zorque', 30) , anchor='nw' , tags='enter')
    # enter button
    canvas.create_image(495,406 , image=infor , anchor='nw' , tags='info')
    canvas.create_text(520,416 , text='Instruction', font=('Zorque', 30) , anchor='nw' , tags='info')
    # exit button
    canvas.create_image(550,480 , image=exit , anchor='nw' , tags='exit')
    canvas.create_text(608,505 , text='EXIT', font=('Zorque', 30) , anchor='nw' , tags='exit')
#  exit game___________
def exitfromgame(event):
    canvas.quit()
#  info___________
def info(event):
    canvas.create_image(0,0 , image=it , anchor='nw')
    # go back
    canvas.create_image(20,20 , image=back , anchor='nw' , tags='back')
    canvas.create_text(65,45 , text='back', font=('Zorque', 30) , anchor='nw' , tags='back')
#  choose level___________
def chooslevel(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]
    # interface page level
    canvas.create_image(0,0 , image=page2 , anchor='nw')
    # show how to play
    canvas.create_image(400,500 , image=detail , anchor='nw')
    # go back
    canvas.create_image(20,20 , image=back , anchor='nw' , tags='back')
    canvas.create_text(65,45 , text='back', font=('Zorque',30) , anchor='nw' , tags='back')
    # level 1 
    canvas.create_image(300,240 , image = cirle , anchor = 'nw' , tags = 'level1')
    canvas.create_text(365,315 , text='Low', font = ('Zorque', 25) , anchor='nw' , tags='level1')
    # level 2
    canvas.create_image(600,240 , image = cirle , anchor='nw' , tags='level2')
    canvas.create_text(632,315 , text='Medium', font=('Zorque', 25) , anchor='nw' , tags='level2')
    # level 3
    canvas.create_image(900,240 , image=cirle , anchor='nw' , tags='level3')
    canvas.create_text(955,315 , text='Hard', font=('Zorque', 25) , anchor='nw' , tags='level3')
#  grid level low___________
def gridLevelLow(event):
    global levelGrid , isreset , iswin , Enegy ,isAllowtomove , count , healthred ,Numapple, Numchery , Nummango, Numbourger, Numpizza, Numstrawberry
    #  show grid
    winsound.PlaySound(None, winsound.SND_PURGE)
    if isAllowtomove == False:
        isAllowtomove = True
    count = 13
    Enegy =40
    healthred = 60
    levelGrid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 1, 1, 1, 1, 6, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,15 ,1 ,1 ,0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,10,0 ,0 ,1 ,0 ,0],
            [0, 1, 0, 0, 0, 0, 0, 1, 1 ,3 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,3 ,0 ,0 ,0 ,3 ,1 ,1 ,5 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,10 ,0],
            [0, 1, 1, 1, 1, 1, 6, 1, 1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 8 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,6 ,0],
            [0, 1, 1, 1, 5, 1, 1, 1, 1 ,0 ,0 ,0 ,5 ,0 ,0 ,3 ,1 ,1 ,2 ,1 ,1 ,5 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,0],
            [0, 10, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,5 ,1 ,1 ,1 ,5 ,1 ,0 ,0],
            [0, 1, 1, 1, 15, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,15 ,0 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,1 ,6 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 0, 0, 1, 6, 1, 1, 1, 1 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ] 
    Numstrawberry = 0
    Numapple = 0
    Numchery = 0
    Nummango = 0
    Numbourger = 0
    Numpizza = 0
    isreset[0] = True
    iswin[1] = True
    drawGrid(levelGrid,bglevel1,wall)
    countTime()
#  grid level Medium ___________
def gridLevelMedium(event):
    global levelGrid , isreset , iswin , Enegy ,isAllowtomove , count , healthred,Numapple, Numchery , Nummango, Numbourger, Numpizza, Numstrawberry
    #  show grid
    winsound.PlaySound(None, winsound.SND_PURGE)
    if isAllowtomove == False:
        isAllowtomove = True
    count = 10
    Enegy =30
    healthred = 40
    levelGrid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 2, 1, 1, 1, 1, 1, 6, 1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,3 ,1 ,1 ,5 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,10 ,0],
            [0, 1, 1, 1, 1, 1, 6, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 8 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,6 ,0],
            [0, 1, 1, 1, 5, 1, 1, 1, 1 ,0 ,0 ,0 ,5 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 10, 0, 0, 0, 0, 0, 0, 1 ,1 ,8 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,5 ,1 ,1 ,1 ,10 ,1 ,1 ,0],
            [0, 1, 1, 1, 15, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,1 ,6 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 0, 0, 1, 6, 1, 1, 1, 1 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ]    
    Numstrawberry = 0
    Numapple = 0
    Numchery = 0
    Nummango = 0
    Numbourger = 0
    Numpizza = 0
    isreset[1] = True
    iswin[2] = True
    drawGrid(levelGrid,bglevel2,wall2)
    countTime()
#  grid level hard___________
def gridLevelHard(event):
    global levelGrid , isreset , iswin , Enegy ,isAllowtomove , count , healthred,Numapple, Numchery , Nummango, Numbourger, Numpizza, Numstrawberry
    #  show grid
    winsound.PlaySound(None, winsound.SND_PURGE)
    if isAllowtomove == False:
        isAllowtomove = True
    count = 13
    Enegy = 15
    healthred = 30
    levelGrid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 1, 6, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,0],
            [0, 10, 0, 0, 0, 0, 3, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,15 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,15 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1 ,5 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,8 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 3, 1, 1, 1, 1, 1, 1 ,0 ,0 ,0 ,6 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,5 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,15 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,10 ,1 ,1 ,1 ,1,0],
            [0, 5, 0, 0, 0, 0, 0, 0, 1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 2, 1, 1, 1, 1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 8, 1, 1, 1, 1, 1, 1, 1 ,3 ,1 ,0 ,1 ,10 ,1 ,1 ,1 ,1 ,1 ,1 ,6 ,1 ,1 ,1 ,1 ,1 ,1 ,15 ,1 ,1 ,1 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],

            ]
    Numstrawberry = 0
    Numapple = 0
    Numchery = 0
    Nummango = 0
    Numbourger = 0
    Numpizza = 0
    isreset[2] = True

    drawGrid(levelGrid,bglevel3,wall3)
    countTime()
#  grid level impossible___________
def gridLevelImpossible(event):
    global levelGrid , Enegy ,isAllowtomove , count , healthred,Numapple, Numchery , Nummango, Numbourger, Numpizza, Numstrawberry
    #  show grid
    winsound.PlaySound(None, winsound.SND_PURGE)
    if isAllowtomove == False:
        isAllowtomove = True
    count = 10
    Enegy =15
    healthred = 25
    levelGrid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 2, 1, 1, 1, 1, 1, 6, 1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,3 ,1 ,1 ,5 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,10 ,0],
            [0, 1, 1, 1, 1, 1, 6, 1, 1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 8 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,6 ,0],
            [0, 1, 1, 1, 5, 1, 1, 1, 1 ,0 ,0 ,0 ,5 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1],
            [0, 10, 0, 0, 0, 0, 0, 0, 1 ,1 ,8 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,5 ,1 ,1 ,1 ,10 ,1 ,1 ,0],
            [0, 1, 1, 1, 15, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,5 ,1 ,1 ,1 ,1 ,8 ,1 ,1 ,1 ,6 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 0, 0, 1, 6, 1, 1, 1, 1 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ] 
    Numstrawberry = 0
    Numapple = 0
    Numchery = 0
    Nummango = 0
    Numbourger = 0
    Numpizza = 0
    drawGrid(levelGrid,bglevel2,wall4)
    countTime()
# Drawing interface grid
def drawGrid(grid,bg,wallTo):
    global grid1,bg1,color1,time, isAllowtomove
    grid1  = grid
    bg1 = bg
    color1 = wallTo
    canvas.delete('all')
    # interface page grid level=
    canvas.create_image(0,0 , image = bg , anchor = 'nw',   tags='cell')
    canvas.create_image(25,5 , image = shap , anchor = 'nw',  tags='cell')
    canvas.create_image(1050,10,image=enter,anchor='nw',  tags='cell')
    time=canvas.create_text(1130 ,60,text='Time: '+str(count)+'s', font=('ubuntu' , 20 ) , fill=colorTime)
    if count <= 0:
        canvas.itemconfig(time,text='Time: '+str(0)+'s')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == BLOCK:
                drawImg(row,col,wallTo)
            elif grid[row][col] == CHICKEN :
                drawChicken(col,row)
            elif grid[row][col] == APPLE:
                drawImg(row,col,apple)
            elif grid[row][col] == STRAWBERRY:
                drawImg(row,col,bery)
            elif grid[row][col] == BOURGER:
                drawImg(row,col,burger)
            elif grid[row][col] == PIZZA:
                drawImg(row,col,pizza)
            elif grid[row][col] == MANGO:
                drawImg(row,col,mango)      
            elif grid[row][col] == CHERY:
                drawImg(row,col,chery)
    health() 
    if Enegy >=100 and healthred >= 100:
        isAllowtomove = False
        if countwin == len(iswin)-1:
            gameFinish()
        else:
            gameWon() 
# drawimage
def drawImg(row,col,img):
    canvas.create_image(40*col,40*row+130, image=img ,anchor='nw', tags='cell')  
#drawChicken          
def drawChicken(col,row):
    if swtict:
        canvas.create_image(40*col,40*row+130, image=charight , anchor='nw',  tags='cell')
    else:
        canvas.create_image(40*col,40*row+130, image=charleft , anchor='nw',  tags='cell')

# ____________________count Function_________________________________________

# function countEnegy _____
def countEnegy():
    global Enegy , healtharray, percentfood , isAllowtomove
    if  0 >= Enegy:
        percentfood = [0,0,0,0,0,0,0,0,0,0]
    elif 10< Enegy <=19:
        percentfood = [9,0,0,0,0,0,0,0,0,0]
    elif 20<= Enegy <=29:
        percentfood = [9,9,0,0,0,0,0,0,0,0]
    elif 30<= Enegy <=39:
        percentfood = [9,9,9,0,0,0,0,0,0,0]
    elif 40<= Enegy <=49:
        percentfood = [9,9,9,9,0,0,0,0,0,0]
    elif 50<= Enegy <=59:
        percentfood = [9,9,9,9,9,0,0,0,0,0]
    elif 60<= Enegy <=69:
        percentfood = [9,9,9,9,9,9,0,0,0,0]
    elif 70<= Enegy <=79:
        percentfood = [9,9,9,9,9,9,9,0,0,0]
    elif 80<= Enegy <=89:
        percentfood = [9,9,9,9,9,9,9,9,0,0]
    elif 90<= Enegy <=99:
        percentfood = [9,9,9,9,9,9,9,9,9,0]
    elif Enegy >= 100 :
        percentfood = [9,9,9,9,9,9,9,9,9,9]
        Enegy = 100

# function show minusHealth_____
def minusHealth():
    global healthred ,healtharray , isAllowtomove
    if healthred <=0:
        healtharray = [0,0,0,0,0,0,0,0,0,0]
        isAllowtomove = False
        gameover()
    elif 10<= healthred <=19:
        healtharray = [8,0,0,0,0,0,0,0,0,0]
    elif 20<= healthred <=29:
        healtharray = [8,8,0,0,0,0,0,0,0,0]
    elif 30<= healthred <=39:
        healtharray = [8,8,8,0,0,0,0,0,0,0]
    elif 40<= healthred <=49:
        healtharray = [8,8,8,8,0,0,0,0,0,0]
    elif 50<= healthred <=59:
        healtharray = [8,8,8,8,8,0,0,0,0,0]
    elif 60<= healthred <=69:
        healtharray = [8,8,8,8,8,8,0,0,0,0]
    elif 70<= healthred <=79:
        healtharray = [8,8,8,8,8,8,8,0,0,0]
    elif 80<= healthred <=89:
        healtharray =[8,8,8,8,8,8,8,8,0,0]
    elif 90<= healthred <=99:
        healtharray = [8,8,8,8,8,8,8,8,8,0]
    elif healthred >= 100:
        healtharray = [8,8,8,8,8,8,8,8,8,8]

# function show health bar_____
def health():
    global Enegy , healtharray, percentfood
    canvas.create_text(64,27, text='Enegy: ')
    canvas.create_text(65,75, text='Health: ')
    countEnegy()
    minusHealth()
    for i in range(len(healtharray)):
        if healtharray[i] == 8:
            canvas.create_rectangle(20*i+65,85,20*i+103,105 ,fill="red" , outline="")
        if percentfood[i] == 9:
            canvas.create_rectangle(20*i+65,40,20*i+103,60 ,fill="sky blue" , outline="")

# show game win_____
def gameWon():
    global countwin
    countwin +=1
    winsound.PlaySound("sound\\tadaa-47995.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(270, 200, image= game , anchor='nw')
    canvas.create_text(490,250, text='You Won', font=('Zorque', 50))
    canvas.create_text(910,515, text='Next Level', font=('Zorque', 20) , tags='next')
    canvas.create_text(815,510, text='i', font=('Zorque', 30))
    canvas.create_text(755,515, text='Menu', font=('Zorque', 20),  tags='Menu')
    showResult()

# show game Finish_____
def gameFinish():
    global countwin
    winsound.PlaySound("sound\\tadaa-47995.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(270, 200, image= game , anchor='nw')
    canvas.create_text(610,250, text='Oh wow You finis all level', font=('Zorque', 30))
    canvas.create_text(930,510, text='Next', font=('Zorque', 25) , tags='next1')
    if countwin == len(iswin):
        canvas.create_text(610,250, text='Damm you so good!', font=('Zorque', 30))
        canvas.create_text(930,510, text='Next', font=('Zorque', 25) , tags='next1')
        countwin = 0
    showResult()

# congra Function_________________________________________
def Congra(event):
    winsound.PlaySound("sound/untitled-123636 (1).wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    canvas.create_image(0, 0, image= congra , anchor='nw')
    canvas.create_image(20,20 , image=back , anchor='nw' , tags='back')
    canvas.create_text(62,45 , text='Home', font=('Zorque', 30) , anchor='nw' , tags='back')
    canvas.create_image(1052,20 , image=back , anchor='nw' , tags='bonus')
    canvas.create_text(1085,45 , text='Bonus', font=('Zorque', 30) , anchor='nw' , tags='bonus')

# Gameover Function_________________________________________
def gameover():
#show game over screen
    # background
    winsound.PlaySound("sound\\negative_beeps-6008.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(270, 200, image= game , anchor='nw')
    # text
    canvas.create_text(510,250, text='Game Over', font=('Zorque', 50))
    canvas.create_text(920,515, text='Restart', font=('Zorque', 20) , tags='Restart')
    canvas.create_text(842,510, text='i', font=('Zorque', 30))
    canvas.create_text(780,515, text='Menu', font=('Zorque', 20),  tags='Menu')
    showResult()

# showResult_____
def showResult():
    # show result 
    number = [Numapple,Numstrawberry,Numchery,Nummango,Numbourger,Numpizza]
    ximg =  320
    yimg = 300
    xtext = 390
    ytext = 313
    n = 0
    for cha in range(len(img)):
        canvas.create_image(ximg, yimg , image=img[cha] , anchor='nw')
        canvas.create_text(xtext,ytext, text='x'+str(number[cha]), font=('verdana', 15),  tags='Menu')
        yimg += 50
        ytext += 52
        n +=1
        if n == 4:
            ximg =  550
            yimg = 300
            xtext = 620
            ytext = 313

# countTime_____
def countTime():
    global count ,isAllowtomove , colorTime
    if isAllowtomove:
        canvas.itemconfig(time,text='Time: '+str(count)+'s', fill=colorTime)
        if count < 10:
            colorTime = 'red'
            winsound.PlaySound("sound/timeout-90320.wav", winsound.SND_ASYNC)
        if count >= 10:
            colorTime = 'black'
        if count > 0:
            count-=1
        if count <= 0 :
            count=0
            canvas.itemconfig(time,text='Time: '+str(count)+'s')
            isAllowtomove = False
            gameover()
        canvas.after(1000,lambda:countTime())

# reset play again_____
def reset(event):
    global isAllowtomove,isreset
    canvas.delete('all')
    if isreset[0]:
        isreset[0] = False 
        gridLevelLow(event)
    elif isreset[1]:
        isreset[1] = False
        gridLevelMedium(event)
    elif isreset[2]:
        isreset[2] = False
        gridLevelHard(event)

# for click to next level-----------------------
def nextlevel(event):
    global iswin , isAllowtomove , count , Enegy,isreset
    canvas.delete('all')
    if iswin[1]:
        isreset[0] = False 
        iswin[1] = False
        gridLevelMedium(event)
    elif iswin[2]:
        isreset[1] = False 
        gridLevelHard(event)

# _____________________________Function isAllowtomove____________________________________

# for find index chiCken ----------------------
def FindindexChiCken(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == CHICKEN :
                return [row,col]

def condistionmove(grid_row,grid_col,direction):
    if 'Left' == direction:
        grid1[grid_row][grid_col] = CELL
        grid1[grid_row][grid_col-1] = CHICKEN
    elif 'Right' == direction:
        grid1[grid_row][grid_col] = CELL
        grid1[grid_row][grid_col+1] = CHICKEN
    elif 'Up' == direction:
        grid1[grid_row][grid_col] = CELL
        grid1[grid_row-1][grid_col] = CHICKEN
    elif 'Down' == direction:
        grid1[grid_row][grid_col] = CELL
        grid1[grid_row+1][grid_col] = CHICKEN

def sumItem(food):
    global swtict , Enegy , count, Numapple, Numchery , Nummango, Numbourger, Numpizza, Numstrawberry, healthred
    if food == APPLE:
        count += 3
        Enegy +=15
        Numapple +=1
        healthred += 10
    elif food == STRAWBERRY:
        count += 1
        Enegy +=5
        Numstrawberry +=1
        healthred +=3
    elif food == CHERY:
        Enegy +=8
        count += 2
        Numchery +=1
        healthred += 6
    elif food == MANGO:
        Enegy +=8
        count += 4
        Nummango +=1
        healthred += 5     
    elif food == BOURGER:
        count -= 5
        Enegy -=10
        Numbourger +=1
        healthred -= 15
    elif food == PIZZA:
        count -= 5
        Enegy -=5
        Numpizza +=1
        healthred -=10

def moveLeft(event):
    global swtict , Enegy , count
    swtict = False
    if isAllowtomove:

        index = FindindexChiCken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row][col-1] == APPLE:
            condistionmove(row,col,'Left')
            sumItem(APPLE)
        elif grid1[row][col-1] == STRAWBERRY:
            condistionmove(row,col,'Left')
            sumItem(STRAWBERRY)
        elif grid1[row][col-1] == CHERY:
            condistionmove(row,col,'Left')
            sumItem(CHERY)
        elif grid1[row][col-1] == MANGO:
            condistionmove(row,col,'Left')
            sumItem(MANGO)
        elif grid1[row][col-1] == BOURGER:
            condistionmove(row,col,'Left')
            sumItem(BOURGER)
        elif grid1[row][col-1] == PIZZA:
            condistionmove(row,col,'Left')
            sumItem(PIZZA)
        elif grid1[row][col-1] == CELL and col != 0 :
            condistionmove(row,col,'Left')
        drawGrid(grid1,bg1,color1)

def moveRight(event):
    global swtict , Enegy , count
    swtict = True
    if isAllowtomove:

        index = FindindexChiCken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row][col+1] == APPLE:
            condistionmove(row,col,'Right')
            sumItem(APPLE)
        elif grid1[row][col+1] == MANGO:
            condistionmove(row,col,'Right')
            sumItem(MANGO)
        elif grid1[row][col+1] == STRAWBERRY:
            condistionmove(row,col,'Right')
            sumItem(STRAWBERRY)
        elif grid1[row][col+1] == CHERY:
            condistionmove(row,col,'Right')
            sumItem(CHERY)            
        elif grid1[row][col+1] == BOURGER:
            condistionmove(row,col,'Right')
            sumItem(BOURGER)
        elif grid1[row][col+1] == PIZZA:
            condistionmove(row,col,'Right')
            sumItem(PIZZA)
        elif grid1[row][col+1] == CELL and col != len(grid1[row])-1:
            condistionmove(row,col,'Right')

        # canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def moveUp(event):
    global Enegy , count
    if isAllowtomove:

        index = FindindexChiCken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row-1][col] == APPLE:
            condistionmove(row,col,'Up')
            sumItem(APPLE)
        elif grid1[row-1][col] == STRAWBERRY:
            condistionmove(row,col,'Up')
            sumItem(STRAWBERRY)
        elif grid1[row-1][col] == MANGO:
            condistionmove(row,col,'Up')
            sumItem(MANGO)            
        elif grid1[row-1][col] == CHERY:
            condistionmove(row,col,'Up')
            sumItem(CHERY)            
        elif grid1[row-1][col] == BOURGER:
            condistionmove(row,col,'Up')
            sumItem(BOURGER)
        elif grid1[row-1][col] == PIZZA:
            condistionmove(row,col,'Up')
            sumItem(PIZZA)
        elif grid1[row-1][col] == CELL and row != 0:                         
            condistionmove(row,col,'Up')
        # canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def moveDown(event):
    global Enegy , count
    if isAllowtomove:

        index = FindindexChiCken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row+1][col] == APPLE:
            condistionmove(row,col,'Down')
            sumItem(APPLE)
        elif grid1[row+1][col] == STRAWBERRY:
            condistionmove(row,col,'Down')
            sumItem(STRAWBERRY)
        elif grid1[row+1][col] == CHERY:
            condistionmove(row,col,'Down')
            sumItem(CHERY)
        elif grid1[row+1][col] == MANGO:
            condistionmove(row,col,'Down')
            sumItem(MANGO)            
        elif grid1[row+1][col] == BOURGER:
            condistionmove(row,col,'Down')
            sumItem(BOURGER)
        elif grid1[row+1][col] == PIZZA:
            condistionmove(row,col,'Down')
            sumItem(PIZZA)
        elif grid1[row+1][col] == CELL and row != len(grid1)-1:            
            condistionmove(row,col,'Down')

        # canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def songGame():
    winsound.PlaySound("sound/untitled-123636 (1).wav", winsound.SND_ASYNC | winsound.SND_LOOP )


# ____________________Main_________________________
root = tk.Tk()
root.geometry(str(WIN_WIDTH)+ 'x' + str(WIN_HEIGHT))
frame = tk.Frame(root)
canvas = tk.Canvas(frame)
root.title('Refreshment')

icon = tk.PhotoImage(file='img/chikenred2.png')
root.iconphoto(True,icon)
root.resizable(0,0)


# _____________________________Image_________________________________________
page1 = tk.PhotoImage(file='img/page1.png')
enter = tk.PhotoImage(file='img/enter.png')
exit = tk.PhotoImage(file='img/exit.png')
page2 = tk.PhotoImage(file='img/page2.png')
cirle = tk.PhotoImage(file='img/circle.png')
back = tk.PhotoImage(file='img/back.png')
game = tk.PhotoImage(file='img/gameover.png')
infor = tk.PhotoImage(file='img/info.png')
congra = tk.PhotoImage(file='img/congra.png')

bglevel1 = tk.PhotoImage(file='img/bg5.png')
bglevel2 = tk.PhotoImage(file='img/bg1.png')
bglevel3 = tk.PhotoImage(file='img/bg4.png')

charight = tk.PhotoImage(file='img/chikenred1.png')
charleft = tk.PhotoImage(file='img/chikenred2.png')
detail = tk.PhotoImage(file='img/detail.png')
shap = tk.PhotoImage(file='img/voo.png')

wall = tk.PhotoImage(file='img/wall1.png')
wall2 = tk.PhotoImage(file='img/wall2.png')
wall3 = tk.PhotoImage(file='img/wall3.png')
wall4 = tk.PhotoImage(file='img/wall4.png')

apple = tk.PhotoImage(file='img/apple.png')
bery = tk.PhotoImage(file='img/bery.png')
chery = tk.PhotoImage(file='img/chery.png')
it = tk.PhotoImage(file='img/int.png')
mango = tk.PhotoImage(file='img/mango.png')
burger = tk.PhotoImage(file='img/burger.png')
pizza = tk.PhotoImage(file='img/pizza.png')

img = [apple,bery,chery,mango,burger,pizza]

# _____________________________Call function__________________________________

start(event=start) 

# _____________________________button Bind___________________________________________

canvas.tag_bind('enter', '<Button-1>',chooslevel)
canvas.tag_bind('back', '<Button-1>',start)
canvas.tag_bind('info', '<Button-1>',info)
canvas.tag_bind('level1', '<Button-1>',gridLevelLow)
canvas.tag_bind('Restart', '<Button-1>',reset)
canvas.tag_bind('level2', '<Button-1>',gridLevelMedium)
canvas.tag_bind('Menu', '<Button-1>',chooslevel)
canvas.tag_bind('level3', '<Button-1>',gridLevelHard)
canvas.tag_bind('exit', '<Button-1>',exitfromgame)
canvas.tag_bind('next', '<Button-1>',nextlevel)
canvas.tag_bind('bonus', '<Button-1>',gridLevelImpossible)
canvas.tag_bind('next1', '<Button-1>',Congra)

# _____________________________key bind Bind___________________________________________

root.bind('<a>',moveLeft)
root.bind('<d>',moveRight)
root.bind('<w>',moveUp)
root.bind('<s>',moveDown)
root.bind('<A>',moveLeft)
root.bind('<D>',moveRight)
root.bind('<W>',moveUp)
root.bind('<S>',moveDown)
root.bind('<Left>',moveLeft)
root.bind('<Right>',moveRight)
root.bind('<Up>',moveUp)
root.bind('<Down>',moveDown)
# _____________________________Display________________________________________

frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()