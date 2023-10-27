# # _____________________________IMPORT____________________________________
# import tkinter as tk
# import winsound
# import random
# # _____________________________Constant___________________________________
# WIN_WIDTH = 1280
# WIN_HEIGHT = 700
# NUMBERONE = 1

# MANGO = 3
# CARROT = 5
# STRAWBERRY = 15
# APPLE = 15
# CHIKEN = 2
# SUMFRUITS = 10

# # _____________________________Variables__________________________________

grid_level1=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            [0, 1, 1, 2, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 3, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,1 ,5 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,3 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,15 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,15 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 5, 1, 1, 1, 1, 1, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,3 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,0],
            [0, 5, 0, 0, 0, 0, 0, 0, 1 ,1 ,15 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0],
            [0, 3, 1, 1, 1, 1, 1, 1, 1 ,5 ,1 ,0 ,1 ,3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,15 ,1 ,1 ,1 ,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
            ]








# # _____________________________Function____________________________________

# def drawGridLevle1():
#     global grid_level1
#     for row in range(len(grid_level1)):
#         for col in range(len(grid_level1[row])):
#             if grid_level1[row][col]==NUMBERONE:
#                 canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill="red")
#             if grid_level1[row][col]==MANGO:
#                 canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill="red")
#                 canvas.create_image(40*col+5,40*row+85, image=fruit01 , anchor='nw')
#             if grid_level1[row][col] == CHIKEN :
#                 canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 )
#             if grid_level1[row][col]==CARROT:
#                 canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill="red")
#                 canvas.create_image(40*col+5,40*row+85, image=carrot , anchor='nw')
#             if grid_level1[row][col]==APPLE:
#                 canvas.create_rectangle(40*col,40*row+80,40*col+40,40*row+120 ,fill="red")
#                 canvas.create_image(40*col+5,40*row+85, image=apple , anchor='nw')

# def drawChiken(col,row):
#     if swtict:
#         canvas.create_image(40*col,40*row+80,   anchor='nw',  tags='cell')
#     else:
#         canvas.create_image(40*col,40*row+80, anchor='nw',  tags='cell')

# def FindindexChiken(grid):
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if grid[row][col] == CHIKEN :
#                 return [row,col]


# def moveLeft(event):
#     global swtict
#     swtict = False
#     if move:
#         index = FindindexChiken(grid_level1)
#         row = index[0]
#         col = index[1]
#         if grid_level1[row][col-1] == NUMBERONE or grid_level1[row][col-1] ==  FRUITS and col != 0 :
#             grid_level1[row][col] = NUMBERONE
#             grid_level1[row][col-1] = CHIKEN
#         canvas.delete('all')
# def moveRight(event):
#     global swtict
#     swtict = True
#     if move:
#         index = FindindexChiken(grid1)
#         row = index[0]
#         col = index[1]
#         if grid1[row][col+1] == NUMBERONE  or grid1[row][col+1] ==  FRUITS and col != len(grid1[row])-1:
#             grid1[row][col] = NUMBERONE
#             grid1[row][col+1] = CHIKEN
#         canvas.delete('all')
#         drawGrid(grid1,bg1,color1)

# def moveUp(event):
#     if move:
#         index = FindindexChiken(grid1)
#         row = index[0]
#         col = index[1]
#         if grid1[row-1][col] == NUMBERONE  or grid1[row-1][col] ==  FRUITS and row != 0:
#             grid1[row][col] = NUMBERONE
#             grid1[row-1][col] = CHIKEN
#         canvas.delete('all')
#         drawGrid(grid1,bg1,color1)

# def moveDown(event):
#     if move:
#         index = FindindexChiken(grid1)
#         row = index[0]
#         col = index[1]
#         if grid1[row+1][col] == NUMBERONE  or grid1[row+1][col] ==  FRUITS and row != len(grid1)-1:
#             grid1[row][col] = NUMBERONE
#             grid1[row+1][col] = CHIKEN
#         canvas.delete('all')
#         drawGrid(grid1,bg1,color1)
# # _____________________________Main_________________________________________
# root = tk.Tk()
# root.geometry(str(WIN_WIDTH)+ 'x' + str(WIN_HEIGHT))
# frame = tk.Frame(root)
# canvas = tk.Canvas(frame)

# root.title('Refreshment')



# fruit01 = tk.PhotoImage(file='images/fruits01.png')
# carrot = tk.PhotoImage(file='images/carrot.png')
# apple = tk.PhotoImage(file='images/apple.png'












# frame.pack(expand=True, fill='both')
# canvas.pack(expand=True, fill='both')



# # _____________________________Call function__________________________________
# drawGridLevle1()



# # _____________________________Bind___________________________________________






# # _____________________________Display________________________________________
# root.mainloop()
