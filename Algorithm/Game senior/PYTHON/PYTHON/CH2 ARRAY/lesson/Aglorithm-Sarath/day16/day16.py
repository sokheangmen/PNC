# =============================nu1==============

# numbers = [[0,0,0],[7,7,7],[0,0,0]]
# result ="lost"
# for row in range(len(numbers)):
#     hasNumber = 0
#     for col in range(len(numbers[row])):
#         if numbers[row][col] == 7:
#             hasNumber += 1
#     if hasNumber == 3:
#         result = "win"
# print(result)




# ==========NUM2
# array1 = eval(input())
# array2 = eval(input())
# result = "equal"
# if len(array1)==len(array2):
#     for row in range(len(array1)):
#         equal = 0
#         for col in range(len(array1[row])):
#             if array1[row][col]==array2[row][col]:
#                 equal += 1
#         if equal == len(array1[row]):
#             result ="equal"
#         else:
#             result = "not equal"
# else:
#     result="not equal"
        
# print(result)

# ===============================num3================


# #   @param grid   (an array 2D)
# #   @param rowIndex  (integer)
# #   @param sign  (string)
# #   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
# def signOnRow(grid, rowIndex, sign):
#     bool = True
#     for rowIndex in range(len(grid)):
#         if grid[rowIndex] != sign:
#             bool = False       
#     return bool   # TO CHANGE !!
    

# #   @param grid   (an array 2D)
# #   @param columnIndex  (integer)
# #   @param sign  (string)
# #   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
# def signOnColumn(grid, columnIndex, sign):
#     bool = True
#     for i in range(len(grid)):
#         if grid[i][columnIndex] != sign:
#             bool = False       
#     return bool 
#     # TODO !!
    



# #   @param grid   (an array 2D)
# #   @param sign  (string)
# #   @return True if a DIAGONAL is composed ONLY of the given sign
# def signOnDiagonal(grid, sign):
#      # TODO !!   
     
    

# #   @param grid   (an array 2D)
# #   @param sign  (string)
# #   @return True if the given sign has WON
# def hasSignWon(grid, sign):
#     # TODO ! 
#     #  It true if : 
#     #  - one of the 2 diagonal is composed of this sign
#     #  - or if 1 of the 3 rows is composed of this sign
#     #  - or if 1 of the 3 columns is composed of this

    
# # MAIN PROGRAM (nothing to change here !)
# grid = eval(input())
# if hasSignWon(grid, "A"):
#     print("A WON")

# elif hasSignWon(grid, "B"):
#     print("B WON")

# else:
#     print("NO WINNER")

    # ======================================

#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
def signOnRow(grid, rowIndex, sign):
    result=False
    countSign=0
    for col in range(len(grid[rowIndex])):
        if grid[rowIndex][col]==sign:
            countSign+=1
    if countSign==3:
        result=True
    return result
    

#   @param grid   (an array 2D)
#   @param columnIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
def signOnColumn(grid, columnIndex, sign):
    result=False
    countSign=0
    for row in range(len(grid)):
        if grid[row][columnIndex]==sign:
            countSign+=1
    if countSign==3:
        result=True
    return result

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if a DIAGONAL is composed ONLY of the given sign
def signOnDiagonal(grid, sign):
    result=False
    countDiagnolRight=0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col==row and grid[row][col]==sign):
                countDiagnolRight+=1
    countDiagonalLeft=0
    col=len(grid[0])
    for row in range(len(grid)):
        col-=1
        if grid[row][col]==sign:
            countDiagonalLeft+=1
    if countDiagonalLeft==3 or countDiagnolRight==3:
        result=True
    return result   

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if the given sign has WON
def hasSignWon(grid, sign):
    ticTacToe=False
    for i in range(len(grid)):
        if signOnRow(grid, i, sign) or signOnColumn(grid,i,sign) or signOnDiagonal(grid,sign):
            ticTacToe=True
    return ticTacToe

    #  It true if : 
    #  - one of the 2 diagonal is composed of this sign
    #  - or if 1 of the 3 rows is composed of this sign
    #  - or if 1 of the 3 columns is composed of this

    
# MAIN PROGRAM (nothing to change here !)
grid =[['A', 'A', 'A'],['B', 'A', 'B'],['B', 'B', 'A']]
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")