
# ==========n

# a = [[1,2,3],[4,5,6]]
# print(a[1])

# ========


# a = [[1,2,3],[4,5,6]]
# print(a[1][2])
# # print(a[row][column])
# ====

# number =[
#     column  0 1 2   row

#             [1,2,3], 0
#             [4,5,6], 1
#             [7,8,9]  2

# ]
# print(number[row][column])

# ==================excer1===========
# a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
# l =""
# for i in a[0]:
#     l += str(i)
#     l +="-" 
# print(l)

# --------

# a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
# l =""
# for i in range(len(a[0])):
#     l += str(a[0][i])
#     l +=  "-" 
# print(l)

# ==============n2

# a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
# l =""
# for i in a[2]:
#     l += str(i)
#     l +="-" 
# print(l)

# ----------

# a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
# l =""
# for i in range(len(a[2])):
#     l += str(a[2][i])
#     l +=  "-" 
# print(l)

# =================n3


# a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
# l =""
# for i in range(len(a)):
#     l += str(a[i][3])
#     l +="-" 
# print(l)

# -------------------------  day2

# numbers = [[1,2,1],[4,1,6],[7,8,1]]
# for i in range(len(numbers)):
#     arr = numbers[i]
#     for n in range(len(arr)):
#         if arr[n]==1:
#             arr[n] =  0
# print(numbers)

# ========================append one arrays  2D

# numbers =[]
# arr = []
# arr.append(1)
# arr.append(2)
# numbers.append(arr)
# print(numbers)


# -------------------------hw

# Enter your code here. Read input from STDIN. Print output to STDOUT
# array=eval(input())
# arrayTwoD=[]
# for row in array:
#     arrayOneD=[]
#     for col in row:
#         arrayOneD.append(col.upper())
#     arrayTwoD.append(arrayOneD)
# print(arrayTwoD)


# -------------

# arrays  = ["banana","coconunt","mango"]
# arraysTwoD =  []
# for row in arrays:
#     arraysOneD =[]
#     for col in row:
#         arraysOneD.append(col.upper())
#     arraysTwoD.append(arraysOneD)
# print(arraysTwoD)

# -----------------------------------n2
# arrayTwoD=eval(input())
# arrayOneD=[]
# for row in arrayTwoD:
#      max=row[0]
#      for col in range(1,len(row)):
#         if max<row[col]:
#           max=row[col]
#      arrayOneD.append(max)
# print(arrayOneD)
# --------=======

# arrays = eval(input())
# newArray = []
# for row in arrays:
#     bigNum = row[0]
#     for col in range(len(row)):
#         if bigNum <row[col]:
#             bigNum = row[col]
#     newArray.append(bigNum)
# print(newArray)

# =============================n3

# arrays = [[5,3,8,4],[3,8,7,1],[1,4,6,3]]
# newArray = []
# for row in range(len(arrays)):
#     index =  arrays[row]
#     for col in range(len(index)):
#         if index[col] == 7:
#             newArray.append(row)
#             newArray.append(col)
# print(newArray)

# =======4

# array = [[5,7,8,4],[5,7,8,4],[5,7,8,4]]
# for row in range(len(array)):
#     arrayOneD = array[row]
#     for col in range(len(arrayOneD)):
#         if arrayOneD[col]==7:
#             arrayOneD.pop(col)
#             arrayOneD.insert(col,8)
# print(array)

# ==============================================================================================================================

# arrays = ["banana","cqconcoc","mango"]
# arrays2D = []
# for row in range(len(arrays)):
#     arrays1D = []
#     arr = arrays[row]
#     for col in arr:
#         arrays1D.append(col.upper())
#     arrays2D.append(arrays1D)
# print(arrays2D)


# ===========================n2

# arrays = [[1,7,3],[9,3,6],[4,8,5]]
# newArrays = []
# for row in range(len(arrays)):
#     arr = arrays[0]
#     for col in range(1,len(arr)):
#         if col > (col[arr]):
#             newArrays.append(arrays[col])
# print(newArrays)


# ==========================work it in function===============================================

# def appendCharOnArray2D(array):
#     arrayTwoD =[]
#     for row in array:
#         loopInArrayOneD = row
#         arrayTwoD.append(appendCharOnArray1D(loopInArrayOneD))
#     return arrayTwoD
# def appendCharOnArray1D(loopInArrayOneD):
#     arrayOneD =[]
#     for col in loopInArrayOneD:
#         arrayOneD.append(col.upper())
#     return arrayOneD
# arrays = ["banana","cqconcoc","mango"]
# print(appendCharOnArray2D(arrays))

# ------------------------------n2-------------------

# def appendToNewArray(arrays):
#     newArray =[]
#     for row in arrays:
#         loopInArray1D = row
#         findBigNumber(loopInArray1D)
#         newArray.append(findBigNumber(loopInArray1D))
#     return newArray
# def findBigNumber(loopInArray1D):
#     bigNum = loopInArray1D[0]
#     for col in range(len(loopInArray1D)):
#         if bigNum <loopInArray1D[col]:
#             bigNum = loopInArray1D[col]
#     return bigNum
# arrays = [[1,7,3],[9,3,6],[4,8,5]]
# print(appendToNewArray(arrays))



# ===============================number3


# def findNummber7(arrays):
#     rowOfNumber = 0
#     colOfNumber = 0
#     for row in range(len(arrays)):
#         newArray = []
#         for col in range(len(arrays[row])):
#             if arrays[row][col] ==7:
#                 colOfNumber += col
#                 rowOfNumber += row 
#         newArray.append(rowOfNumber)
#         newArray.append(colOfNumber)           
#     return newArray
# arrays = [[5,3,8,4],[3,8,7,1],[1,4,6,3]]
# print(findNummber7(arrays))

# ==========================num4
# def changeNumber(arrays):
#     for row in  range(len(arrays)):
#         for col in range(len(arrays[row])):
#             if arrays[row][col]==7:
#                 arrays[row].pop(col)
#                 arrays[row].insert(col,8)
#     return arrays
# array = [[5,7,8,4],[5,7,8,4],[5,7,8,4]]
# print(changeNumber(array))



# =================number3 find mix number
# numbers =eval(input())
# def Max(num1,num2):
#     max = num1
#     if num1 < num2:
#         max =num2
#     return max
# for value in numbers:
#     maxNum = value[0]
    















