############EX1
# array=["0", "x", "0", "0",]
# iStrue=True
# for i in range(len(array)):
#     if array[-1] == "x" and iStrue:
#         iStrue=False
#     elif array[i] == "x" and iStrue:
#         array[i] = "0"
#         array[i+1] = "x"
#         iStrue =False
# print(array)
# tip2
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
############EX2

# array=[1,1,3,3,4,4,5,5]
# result=[]
# value=True
# for arr in array:
#     if value:
#         result.append(array[0])
#         value=False
#     for newarr in result:
#         if  newarr!= arr:
#             result.append(newarr)
# print(result)
# tip2
# array = [1,1,2,3,4,5,5,6,7,8, 8,9]
# newArray = []
# for arr in array:
#     if arr not in newArray:
#         newArray.append(arr)
# print(newArray)

############EX3

# array=eval(input())
# newarr=str(input())
# array.append(newarr)
# print(array)

############EX4

# def findindexOfSeven(array):
#     Index=0
#     for arr in range(len(array)):
#         if array[arr]==7:
#             Index=arr
#     return Index
# number=[2,3,4,7,6]
# number.pop(findindexOfSeven(number))
# print(number)

############EX5

# array2D=[
#     [1,3,3],
#     [4,7,6],
#     [1,8,9]
# ]
# for row in range(len(array2D)):
#     newcl=array2D[row]
#     for column in range(len(newcl)):
#         if newcl[column] == 7:
#             indexrow=row
#             indexcolumn=column
# print("row: "  +str( indexrow) + " and " +"column: "+str(indexcolumn))

