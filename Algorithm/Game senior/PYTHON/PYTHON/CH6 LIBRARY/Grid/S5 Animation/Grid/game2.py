# _____________________________IMPORT____________________________________
import tkinter as tk
import winsound
import random
# _____________________________Constant___________________________________
WIN_WIDTH = 1280
WIN_HEIGHT = 700
NUMBERONE = 1
CHIKEN = 2
# WALL = 0
# MANGO = 3
# CARROT = 5
# STRAWBERRY = 10
# APPLE = 15
FRUITS = 3
SUMFRUIT = 0 

# _____________________________Variables__________________________________






swtict = True
count =10
move = True
Enegy = 50
# _____________________________Function____________________________________



def start(event):
    canvas.delete('all')
    canvas.create_image(0,0 , image=page1 , anchor='nw')

    # enter button
    canvas.create_image(550,300 , image=enter , anchor='nw' , tags='enter')
    canvas.create_text(588,325 , text='ENTER', font=('Zorque', 30) , anchor='nw' , tags='enter')
    # exit button
    canvas.create_image(550,390 , image=exit , anchor='nw' , tags='exit')
    canvas.create_text(608,415 , text='EXIT', font=('Zorque', 30) , anchor='nw' , tags='exit')

def exitfromgame(event):
    canvas.quit()


def chooslevel(event):

    canvas.delete('all')
    global move , count
    if move == False:
        move = True
        count = 10

    # interface page level
    canvas.create_image(0,0 , image=page2 , anchor='nw')

    # show how to play
    canvas.create_image(400,500 , image=detail , anchor='nw')

    # go back
    canvas.create_image(20,20 , image=back , anchor='nw' , tags='back')
    canvas.create_text(65,45 , text='back', font=('Zorque', 30) , anchor='nw' , tags='back')

    # level 1 
    canvas.create_image(300,240 , image = cirle , anchor = 'nw' , tags = 'level1')
    canvas.create_text(368,250 , text='1', font = ('Zorque', 100) , anchor='nw' , tags='level1')
    # level 2
    canvas.create_image(600,240 , image = cirle , anchor='nw' , tags='level2')
    canvas.create_text(658,250 , text='2', font=('Zorque', 100) , anchor='nw' , tags='level2')
    # level 3
    canvas.create_image(900,240 , image=cirle , anchor='nw' , tags='level3')
    canvas.create_text(958,250 , text='3', font=('Zorque', 100) , anchor='nw' , tags='level3')



def gridlevel1(event):
    #  show grid
    grid_level1= [
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 1, 1, 2, 1, 1, 1 ,3 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,1 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 1, 0, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 3, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,3,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,1 ,1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 0, 0, 1, 3, 1, 1, 1, 1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ]
    drawGrid(grid_level1,bglevel1,'blue')
    countTime()


def gridlevel2(event):
    #  show grid
    grid_level2=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 2, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 3 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 3, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 3, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ]

    drawGrid(grid_level2,bglevel2,'white')
    countTime()


def gridlevel3(event):
    #  show grid
    
    grid_level3=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 3, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,1 ,3 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 3, 1, 1, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,3 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 2, 1, 1, 1, 1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 1, 1, 1, 1, 1, 1, 1 ,3 ,1 ,0 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,1 ,1 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],

            ]
    drawGrid(grid_level3,bglevel3,'brown')
    countTime()

    




def drawGrid(grid,bg,color):

    global grid1,bg1,color1,time,gridReset

    if count == 10 :
        gridReset = grid


    grid1  = grid

    bg1 = bg

    color1 = color

    canvas.delete('all')

    # interface page level1

    canvas.create_image(0,0 , image = bg , anchor = 'nw',   tags='cell')

    canvas.create_image(25,5 , image = shap , anchor = 'nw',  tags='cell')

    canvas.create_image(1050,10,image=enter,anchor='nw',  tags='cell')


    time=canvas.create_text(1130 ,60,text='Time: '+str(count)+'s', font=('ubuntu' , 20 ))

    health()
    for row in range(len(grid)):

        for col in range(len(grid[row])):
            
            if grid[row][col] == NUMBERONE:
                canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill=color ,outline="", tags='cell')

            if grid[row][col] == CHIKEN :

                canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill=color , outline="",  tags='cell')
                drawChiken(col,row)

            if grid[row][col] == FRUITS:
                
                canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill=color , outline="",  tags='cell')
                canvas.create_image(40*col,40*row+80, image=random.choice(fruits),anchor='nw', tags='cell')
                
def drawChiken(col,row):
    if swtict:
        canvas.create_image(40*col,40*row+80, image=charight , anchor='nw',  tags='cell')
    else:
        canvas.create_image(40*col,40*row+80, image=charleft , anchor='nw',  tags='cell')






def health():
    healtharray = [8,8,8,8,8,8,8,8,8,8]
    canvas.create_text(64,27, text='Enegy: ',font=(2))
    percentfood = [9,9,9,9,9,9,9,9,9,9]
    canvas.create_text(65,75, text='Health: ',font=(2))
    for i in range(len(healtharray)):
        if healtharray[i] == 8:
            canvas.create_rectangle(20*i+65,85,20*i+103,105 ,fill="red" , outline="")
        if percentfood[i] == 9:
            canvas.create_rectangle(20*i+65,40,20*i+103,60 ,fill="sky blue" , outline="")




def countTime():
    global count ,move
    if move:
        canvas.itemconfig(time,text='Time: '+str(count)+'s')
        if count < 10:
            canvas.itemconfig(time,fill='red')
        if count > 0:
            count-=1
        if count == 0 :
            gameover()
            move = False
        canvas.after(1000,lambda:countTime())

def reset(event):
    global move , count ,gridReset
    if move == False:
        move = True
        count = 10
    canvas.delete('all')
    countTime()
    drawGrid(gridReset,bg1,color1)


# def sumOfFruits():
#     if 
# _____________________________Function Move____________________________________


def FindindexChiken(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == CHIKEN :
                return [row,col]


def moveLeft(event):
    global swtict
    swtict = False
    if move:
        index = FindindexChiken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row][col-1] == NUMBERONE or grid1[row][col-1] ==  FRUITS and col != 0 :
            grid1[row][col] = NUMBERONE
            grid1[row][col-1] = CHIKEN
        canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def moveRight(event):
    global swtict
    swtict = True
    if move:
        index = FindindexChiken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row][col+1] == NUMBERONE  or grid1[row][col+1] ==  FRUITS and col != len(grid1[row])-1:
            grid1[row][col] = NUMBERONE
            grid1[row][col+1] = CHIKEN
        canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def moveUp(event):
    if move:
        index = FindindexChiken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row-1][col] == NUMBERONE  or grid1[row-1][col] ==  FRUITS and row != 0:
            grid1[row][col] = NUMBERONE
            grid1[row-1][col] = CHIKEN
        canvas.delete('all')
        drawGrid(grid1,bg1,color1)

def moveDown(event):
    if move:
        index = FindindexChiken(grid1)
        row = index[0]
        col = index[1]
        if grid1[row+1][col] == NUMBERONE  or grid1[row+1][col] ==  FRUITS and row != len(grid1)-1:
            grid1[row][col] = NUMBERONE
            grid1[row+1][col] = CHIKEN
        canvas.delete('all')
        drawGrid(grid1,bg1,color1)

# ____________________countscore Function_________________________________________
# def countEnegy(event):
#     score = -50




# ____________________Gameover Function_________________________________________
def gameover():

    canvas.create_image(270, 200, image= game , anchor='nw')
    canvas.create_text(510,250, text='Game Over', font=('Zorque', 50))

        # canvas.create_image(30,400, image = enter, anchor = 'nw' )
    canvas.create_text(920,515, text='Restart', font=('Zorque', 20) , tags='Restart')
    canvas.create_text(842,510, text='i', font=('Zorque', 30))
    canvas.create_text(780,515, text='Menu', font=('Zorque', 20),  tags='Menu')
        




# ____________________Main_________________________________________
root = tk.Tk()
root.geometry(str(WIN_WIDTH)+ 'x' + str(WIN_HEIGHT))
frame = tk.Frame(root)
canvas = tk.Canvas(frame)

root.title('Refreshment')


icon = tk.PhotoImage(file='img/chikenred1.png')
root.iconphoto(True,icon)
root.resizable(0,0)




# time=canvas.create_text(1130 ,60,text='Time '+str(count)+'s', font=('ubuntu' , 20 ))


# _____________________________Image_________________________________________



page1 = tk.PhotoImage(file='img/page1.png')
enter = tk.PhotoImage(file='img/enter.png')
exit = tk.PhotoImage(file='img/exit.png')
page2 = tk.PhotoImage(file='img/page2.png')
cirle = tk.PhotoImage(file='img/circle.png')
back = tk.PhotoImage(file='img/back.png')
game = tk.PhotoImage(file='img/gameover.png')


bglevel1 = tk.PhotoImage(file='img/bg5.png')
bglevel2 = tk.PhotoImage(file='img/bg1.png')
bglevel3 = tk.PhotoImage(file='img/bg4.png')

charight = tk.PhotoImage(file='img/chikenred1.png')
charleft = tk.PhotoImage(file='img/chikenred2.png')
detail = tk.PhotoImage(file='img/detail.png')
shap = tk.PhotoImage(file='img/voo.png')

fruit1 = tk.PhotoImage(file='img/fruit1.png')
fruit2 = tk.PhotoImage(file='img/fruit2.png')
fruit3 = tk.PhotoImage(file='img/fruit2.png')
fruit4 = tk.PhotoImage(file='img/fruits01.png')






fruits=[fruit3, fruit1, fruit2, fruit4, fruit2, fruit1, fruit2, fruit1, fruit3]
# _____________________________Call function__________________________________
# 




start(event=start) 

# chooslevel(event=chooslevel)
# gridlevel2(event=gridlevel2)


# _____________________________button Bind___________________________________________

canvas.tag_bind('enter', '<Button-1>',chooslevel)
canvas.tag_bind('back', '<Button-1>',start)
canvas.tag_bind('level1', '<Button-1>',gridlevel1)
canvas.tag_bind('Restart', '<Button-1>',reset)

canvas.tag_bind('level2', '<Button-1>',gridlevel2)
canvas.tag_bind('Menu', '<Button-1>',chooslevel)
canvas.tag_bind('level3', '<Button-1>',gridlevel3)
canvas.tag_bind('exit', '<Button-1>',exitfromgame)


# _____________________________key bind Bind___________________________________________

root.bind('<a>',moveLeft)
root.bind('<d>',moveRight)
root.bind('<w>',moveUp)
root.bind('<s>',moveDown)



# _____________________________Display________________________________________
frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()
