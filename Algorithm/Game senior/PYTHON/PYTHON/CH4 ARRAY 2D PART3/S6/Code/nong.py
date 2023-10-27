def hasMonsterOnCel(position,row,col):
    iSTrue=False
    for arr in position:
        if arr[0]==row and arr[1]==col:
            iSTrue=True
    return iSTrue
array2D=[
        [3,3],
        [1,2],
        [4,0]
]  
result=""
for newrow in range(5):
    for newcol in range(5):
        if hasMonsterOnCel(array2D,newcol,newrow):
            arr="*"
        else:
            arr="0"
        result+=arr
    result+="\n"
print(result)

# EX2###########################################################

# def isInfected(grid, r, c ) :
#     return grid[r][c]==1  
        

# def willBeInfected(grid, r, c) :
#     verticalCont = False
#     horizontalCont = False
#     rowNb = len(grid)-2
#     columnNb = len(grid[0])-2
#     if c < columnNb:
#         if grid[r][c]==grid[r][c+2]:
#             horizontalCont=True
#     if r < rowNb:
#         if grid[r][c]==grid[r+2][c]:
#             verticalCont=True
#     return horizontalCont,verticalCont



# def getNextInfectedCells(grid):
#     result = []
#     for row in range(len(grid)):
#         for colunm in range(len(grid[row])):
#             person=isInfected(grid,row,colunm) 
#             if person:
#                 positiveCovid= willBeInfected(grid,row,colunm) 
#                 if positiveCovid[0]:
#                     result.append([row,colunm+1])
#                 if positiveCovid[1]:
#                     result.append([row+1,colunm])
#     return result     
           
# grid= [ [0,1,0,1,0],
#     [0,1,0,1,0],
#     [0,0,0,0,0],
#     [0,1,0,1,0],
#     [0,0,0,0,0]
#     ]
# newInfectedCells = getNextInfectedCells(grid) 
# for index in range(len(newInfectedCells)):
#    row=newInfectedCells[index][0]
#    colunm=newInfectedCells[index][1]
#    grid[row][colunm]=1
# print(grid)




#@######### Instruction

# # Return True if the cell at given position (row, colum) is infected
# def isInfected(grid, r, c ) :
#     return grid[r][c] == 1

# # Return True if the cell at given position (row, colum) will be infected after contamination
# def willBeInfected(grid, r, c) :

#     # 1- Check if any VETICAL CONTAMINATION   (top cell and buttom cells are  infected)
#     verticalCont = False
#     # TODO  !!!!
    
#     # 2- Check if any HORIZONTA CONTAMINATION  (left cell and right cells are  infected)
#     horizontalCont = False
#      # TODO  !!!!
    
#     # 3- cell infected if vertical or horizontal contamination
#     return verticalCont or horizontalCont

# # Return the list of cell that  WILL BE  infected after contamination
# # Return is an array of cell positions, each position is an array  [row, column]
# def getNextInfectedCells(grid) :
#     rowNb = len(grid)
#     columnNb = len(grid[0])
#     result = []
   
#      # TODO  !!!!
    
#     return result


# # MAIN CODE
# grid = eval(input())

# # Step 1 : we get the list of the cell that will be infected
# newInfectedCells = getNextInfectedCells(grid) 

# # Step 2 : we update the grid (cell infected will be set to 1)
# # TODO  !!!!

# # Step 3 : print the new grid)

# print(grid)






# import calendar
# year=2023
# month=12
# print(calendar.month(year,month))