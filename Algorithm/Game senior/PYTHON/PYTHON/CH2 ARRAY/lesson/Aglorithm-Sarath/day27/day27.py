# import tkinter as tk

# root = tk.Tk()
# # set TK window size 
# root.geometry("900x900")
# frame=tk.Frame()
# frame.master.title('fprm Array to Graphics - Step 1')
# canvas = tk.Canvas(root)

# grid=[0,0,1,0,0,0,0,0,0]

# def getIndexOf1(grid):
#     # input: grid = array of integers
#     # output: indexOf1=integer
#     # get the index of the 1 inside grid
#     # in the example, return 2
#     getIndexOf1 = 0
#     for i in range(len(grid)):
#         if grid[i]==1:
#             getIndexOf1=i
#     return getIndexOf1
# print(getIndexOf1(grid))
# def moveRight(event):
    
#     index=getIndexOf1(grid)
#     print('move to the right')
#     # for r in range(len(grid)):
#     if grid[index]==1 and (index)<len(grid)-1:
#         grid[index]=0
#         grid[index+1]=1
#     arrayToDrawong()
#     print(grid)

            

    
# def moveLeft(event):

#     index=getIndexOf1(grid)
#     print('move to the left')
#     if grid[index]==1 and getIndexOf1(grid)>0:
#         grid[index]=0
#         grid[index-1]=1
#     arrayToDrawong()
#     print(grid)






# def arrayToDrawong():
#     global grid
#     size=100
#     x1=10
#     x2=x1+size
#     y1=200
#     y2=290
#     # Draw a fow of squares from grrid:
#     for i in range(len(grid)):
#         if grid[i]==0:
#             canvas.create_rectangle(x1,y1,x2,y2, fill="white")
#         elif grid[i]==1:
#             canvas.create_rectangle(x1,y1,x2,y2, fill="black",tags="blackColor")
#         x1+=size
#         x2+=size

#     #  white if 0, black if 1

#     print('hello')

# arrayToDrawong()
# # root.bind("<Button-1>",arrayToDrawong)
# root.bind("<r>",moveRight)
# root.bind("<l>",moveLeft)

# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")

# root.mainloop()














# -------------------------------------------------------------

import tkinter as tk

root = tk.Tk()
# set TK window size 
root.geometry("650x1000")
frame=tk.Frame()
canvas = tk.Canvas(width=1200,height=700, bg='pink')
frame.master.title('fprm Array to Graphics - Step 1')
canvas = tk.Canvas(root)

# photo=tk.PhotoImage(file='/home/koompstudentpnc/Desktop')

grid=[[1,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,2],

    
]

def getIndexOf1(grid):
    # input: grid = array of integers
    # output: indexOf1=integer
    # get the index of the 1 inside grid
    # in the example, return 2
    getIndexOf1 = 0
    for i in range(len(grid)):
        for e in range(len(grid)):
            if grid[i][e]==1:
                getIndexOf1=i


    return getIndexOf1
print(getIndexOf1(grid))

def getIndexOf2(grid):
    # input: grid = array of integers
    # output: indexOf1=integer
    # get the index of the 1 inside grid
    # in the example, return 2
    getIndexOf2 = 0
    for i in range(len(grid)):
        for e in range(len(grid)):
            if grid[i][e]==1:
                getIndexOf2=e


    return getIndexOf2
print(getIndexOf2(grid))






def moveRight(event):
    
    indexrow=getIndexOf1(grid)
    indexcol=getIndexOf2(grid)
    print('move to the right')
    # for r in range(len(grid)):
    if grid[indexrow][indexcol]==1 and (indexcol)<len(grid)-1:
        grid[indexrow][indexcol]=0
        grid[indexrow][indexcol+1]=1
    arrayToDrawong()
    print(grid)

            

    
def moveLeft(event):

    indexrow=getIndexOf1(grid)
    indexcol=getIndexOf2(grid)
    print('move to the left')
    if grid[indexrow][indexcol]==1 and indexcol>0:
        grid[indexrow][indexcol]=0
        grid[indexrow][indexcol-1]=1

    arrayToDrawong()
    print(grid)

def moveUp(event):
    indexrow=getIndexOf1(grid)
    indexcol=getIndexOf2(grid)
    print('move to the Up')
    if grid[indexrow][indexcol]==1 and indexrow>0:
        grid[indexrow][indexcol]=0
        grid[indexrow-1][indexcol]=1
    arrayToDrawong()
    print(grid)


def moveDown(event):

    indexrow=getIndexOf1(grid)
    indexcol=getIndexOf2(grid)
    print('move to the Down')
    if grid[indexrow][indexcol]==1 and (indexrow)<len(grid)-1:
        grid[indexrow][indexcol]=0
        grid[indexrow+1][indexcol]=1
    arrayToDrawong()
    print(grid)














def arrayToDrawong():

    global grid
    size=100
    y1=10
    y2=100
    # Draw a fow of squares from grrid:
    for i in range(len(grid)):
        x1=10
        x2=x1+size
        for e in range(len(grid[i])):
            if grid[i][e]==0:
                canvas.create_rectangle(x1,y1,x2,y2, fill="white")
            elif grid[i][e]==1:
                canvas.create_rectangle(x1,y1,x2,y2, fill="black",tags="blackColor")
            elif grid[i][e]==2:
                canvas.create_rectangle(x1,y1,x2,y2, fill="red")


                


            x1+=size
            x2+=size
        y1=y2
        y2+=size
    #  white if 0, black if 1

arrayToDrawong()
# root.bind("<Button-1>",arrayToDrawong)
root.bind("<r>",moveRight)
root.bind("<l>",moveLeft)
root.bind("<u>",moveUp)
root.bind("<d>",moveDown)



# canvas.create_image(0,0, image=photo, anchor=NW)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")

root.mainloop()