# def signOnRow(grid, rowIndex, sign):
#     result=False
#     countSign=0
#     for col in range(len(grid[rowIndex])):
#         if grid[rowIndex][col]==sign:
#             countSign+=1
#     if countSign==3:
#         result=True
#     return result
# def signOnColumn(grid, columnIndex, sign):
#     result=False
#     countSign=0
#     for row in range(len(grid)):
#         if grid[row][columnIndex]==sign:
#             countSign+=1
#     if countSign==3:
#         result=True
#     return result
# def signOnDiagonal(grid, sign):
#     result=False
#     countDiagnolRight=0
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if (col==row and grid[row][col]==sign):
#                 countDiagnolRight+=1
#     countDiagonalLeft=0
#     col=len(grid[0])
#     for row in range(len(grid)):
#         col-=1
#         if grid[row][col]==sign:
#             countDiagonalLeft+=1
#     if countDiagonalLeft==3 or countDiagnolRight==3:
#         result=True
#     return result 
# def hasSignWon(grid, sign):
#     ticTacToe=False
#     for i in range(len(grid)):
#         if signOnRow(grid, i, sign) or signOnColumn(grid,i,sign) or signOnDiagonal(grid,sign):
#             ticTacToe=True
#     return ticTacToe
# grid =[['A', 'B', 'A'],
#        ['B', 'B', 'B'],
#        ['B', 'B', 'A']]
# if hasSignWon(grid, "A"):
#     print("A WON")

# elif hasSignWon(grid, "B"):
#     print("B WON")
# else:
#     print("NO WINNER")



