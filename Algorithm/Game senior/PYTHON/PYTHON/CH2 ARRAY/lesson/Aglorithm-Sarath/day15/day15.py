# ----------------------number2=======

# array2D = [["A", "B", "C"], ["D", "F", "C"], ["A", "A", "F"], ["V", "B", "C"]]
# rowOfInput = 1

# for row in range(len(array2D)):
#     if rowOfInput == row:
#         for col in range(len(array2D[row])):     
#             array2D[row][col]= "*"
# print(array2D)

# ==========================n3===================

# array = ["0", "X", "0", "0"]
# index = 0
# hasX = True
# while hasX and (index+1)<len(array):
#     if array[index]=="X":
#         array[index] = "0" 
#         array[index+1]="X"
#         hasX =False
#     index += 1
# print(array)

# ============num4

personsInRoom = eval(input())      # it's an array 2D !
newPersonRow = int(input())        # row of the new person to add
newPersonColumn = int(input())     # column of the new person to add
numOne = 0
l= False
for row in range(len(personsInRoom)):
    for col in range(len(personsInRoom[row])):
        if personsInRoom[row][col]==0:
            if newPersonRow==row and newPersonColumn==col:
                l = True       
        elif personsInRoom[row][col] == 1:
            numOne += 1
if l and numOne <3:
    result = "CAN ADD"
else:
    result = "CANNOT ADD"
print(result)


# =========================number1=================
            
# array2D = [["A", "B", "C"], ["D", "F", "C"], ["A", "A", "F"], ["V", "B", "C"]]
# columnOfInput = int(input())

# for col in range(len(array2D[0])):
#     loopOnArray1D = array2D[0][col]
#     for row in range(len(loopOnArray1D)):
#         if row == columnOfInput:
#             loopOnArray1D[row]="*"
# print(array2D)
    
    
    