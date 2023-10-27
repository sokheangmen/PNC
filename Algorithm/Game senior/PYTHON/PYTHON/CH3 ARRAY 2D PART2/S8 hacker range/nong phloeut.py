#############ex1
# def numberOfEight(array):
#     result = 0
#     for arr in array:
#         if arr == 8:
#             result += 1
#     if result == 0:
#         result = "NOT FOUND"
#     return result
# number = eval(input())
# print(numberOfEight(number))  
#############ex2

# def splitBySpace(words):
#     result=[]
#     newArray=""
#     for i in range(len(words)):
#         if words[i] != " ":
#             newArray+=words[i]
#         if words[i]==" ":
#             result.append(newArray)
#         if i==len(words[i])-1:
#             result.append(words)
#     return result
# words = "hello world hi"
# print(splitBySpace(words))
#############ex3
# array=[1,2,6,7,9,3]
# result=[]
# for arr in range(len(array)) :
#     if array[arr] % 2 == 1:
#         result .append(array[arr])
# newArray=[]
# for new in range(len(result)):
#     newArray.append(result[-new-1])
# print(newArray)

# tip2
# array=[2,4,6,8]
# result=[]
# newArray=[]
# for arr in range(len(array)):
#     if array[arr]%2==1:
#         result.append(array[arr])
#     newArray=result[::-1]
# print(newArray)

#############ex4
# array=[
#     [0,0,0],
#     [0,0,0],
#     [7,7,7]
#     ]
# result="lost"
# for row in range(len(array)):
#     hasarray = 0
#     for culum in range(len(array[row])):
#         if array[row][culum]==7:
#             hasarray +=1
#     if hasarray == 3:
#         result = "win"
# print(result)

#############ex5

# array = [8,9,4,1,1]
# max = array[0]
# for index in range(len(array)):
#     if array[index] > max :
#         max = array[index]
# for i in range(len(array)):
#     if array[i] < 5 :
#         array[i] = max
# print(array)
# tipe2
# array = [8,0,4,1,1]
# max = array[0]
# for index in range(len(array)):
#     if array[index] > max :
#         max = array[index]
#     if array[index] < 5 :
#         array[index] = max
# print(array)


# arr=[[0,1,0,0,0],
#     [0,1,0,0,0],
#     [0,1,0,0,0]
#     ]
# for i in range(len(arr)):
#     for j in range(len(arr[i])-1):
#         if arr[i][j]==1:
#             arr[i][j] =0
#             arr[i][j+1] = 1
# print(arr[0])