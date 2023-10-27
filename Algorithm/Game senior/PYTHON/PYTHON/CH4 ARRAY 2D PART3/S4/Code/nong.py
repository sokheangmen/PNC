# Ex1
# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# array=int(input())
# for row in range(len(array2D)):
#     if row==array:
#         for col in range(len(array2D[row])):
#             array2D[col][row]="*"
# if array>row:
#     array2D="column error"
# print(array2D)

# array2D=[

#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# array=int(input())
# if len(array2D[0])-1<array:
#     array2D="column error"
# for row in range(len(array2D)):
#         array2D[array][row]="*"
# print(array2D)
# Ex2

# array=["B", "A", "B", "N", "A", "N","A"],["B", "A", "B", "N", "A", "N","A"]
# array2D=[]
# for row in array:
#     sum=""
#     for col in row:
#         sum+=col.lower()
#     array2D.append(sum)
# print(array2D)


# Ex3

# array = [1,5,1,8,8,9,9] 
# newArray=[]
# for arr in range(len(array)):
#     index=array[arr]
#     num=0
#     for cha in range(len(array)):
#         if array[cha]==index:
#             num+=1
#     if num>1 and index not in newArray:
#         newArray.append(index)
# print(newArray)


# Ex4

# array1=[
# [0,1,0],
# [0,0,0]
# ]
# array2=[
# [0,0,0],
# [0,2,0]
# ]
# result="Not Equal"
# if array1==array2:
#     result="Equal"
# print(result)
# tip2
# array1 =[[1,9,7],[0,9,7]] 
# array2 =[[1,8,7],[0,9,7]] 
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

# Ex5
# array2D=[
#         [0, 0, 0], 
#         [0, 1, 0],
#         [0, 0, 1]
#         ] 
# newRow = 0       # row of the new person to add
# newColumn = 0    # column of the new person to add
# numOne = 0
# isTrue = False
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if array2D[row][col]==0:
#             if newRow==row and newColumn==col:
#                 isTrue = True       
#         elif array2D[row][col] == 1:
#             numOne += 1
# if isTrue and numOne <3:
#     result = "CAN ADD"
# else:
#     result = "CANNOT ADD"
# print(result)

  


