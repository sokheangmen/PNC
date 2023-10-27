# ===================nu1

# array2D = [['B','A','N','A','N','A'],['C','O','C','O','N','U','T']]
# valueInArray2D =[]
# for row in array2D:
#     valueInArray1D = ""
#     for col in range(len(row)):
#         valueInArray1D += row[col]
#     valueInArray2D.append(valueInArray1D.lower()) 
# print(valueInArray2D)
        
# ===============================nu2

# array2D = [[1,2,3],[4,5,6],[7,8,9]]
# arrayOfCol = []
# for col in range(len(array2D[0])):
#     sumOfcol = 0
#     for row in range(len(array2D)):
#         sumOfcol += array2D[row][col]
#     arrayOfCol.append(sumOfcol)
# print(arrayOfCol)


# array2D = [[1,2,3],[4,5,6],[7,8,9]]
# amo=0
# for col in range(len(array2D[0])):
#     for row in range(len(array2D)):
#         if array2D[row][col]%2==1:
#             amo+=1
# print(amo)

array2D = [[10,2,3],[4,5,6],[7,8,9]]
for col in range(len(array2D[0])):
    for row in range(len(array2D)):
        if array2D[row][col]==2:
            array2D[row][col] =3
print(array2D)

# array2D = [[1,2,3],[4,5,6],[7,8,9]]
# d =[]
# for row in range(len(array2D)):
#     a = 0
#     for col in range(len(array2D)):
#         if array2D[row][col]>a:
#             a = array2D[row][col]
#     d.append(a)
# print(d)
        








# ===================n3
# arrays = eval(input())
# newArray = []
# for col in range(len(arrays[0])):
#     num = arrays[0][col]
#     for row in range(len(arrays)):
#         if num > arrays[row][col]:
#             num = arrays[row][col]           
#     newArray.append(num)
# print(newArray)














# n4======================================

# array = eval(input())
# age = int(input())
# fisrtName = ""
# for row in range(len(array)):
#     if age == array[row][2]:
#         fisrtName += array[row][0] + "\n"
# print(fisrtName)


        
    




# Teacher================================================
# 1
# chars = eval(input())
# words =[]

# for value in chars:
#     word =""
#     for char in value:
#         word += char.lower()
#     words.append(word)
# print(words)



# 2=======================

# array2D =  eval(input())
# arrayOfCol = []
# if len(array2D) >0:
#     for col in range(len(array2D[0])):
#         sumOfcol = 0
#     for row in range(len(array2D)):
#         sumOfcol += array2D[row][col]
#     arrayOfCol.append(sumOfcol)
# print(arrayOfCol)

# ===========4
# persons = eval(input())
# age = int(input())
# for i in range(len(persons)):
#     if age == persons[i][2]:
#         print(persons[i][0])


