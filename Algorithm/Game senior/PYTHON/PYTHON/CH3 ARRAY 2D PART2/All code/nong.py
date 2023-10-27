##_____________________ S3
# EX1
# array=[6,5,10,8]
# iStrue=True
# for arr in range(len(array)):
#     if array[arr]<5 or array[arr]>10:
#         iStrue=False
# print(iStrue)
##_____________________ S6
# Ex1
# array=[9,4,9,5,10]
# result=""
# for arr in range(len(array)):
#     if array[arr]<10:
#         array[arr]=10
#     result+=str(array[arr])+" "
# print(result)
#Ex2
# words=["ronan","rady"]
# newword=str(input())
# words.append(newword)
# print(words)
#Ex3
# array=[1,2,3,4,5,6,7,8]
# newarray=[]
# for arr in range(len(array)):
#     array[arr]+=1
#     newarray.append(array[arr])
# print(newarray)
#Ex4
# def remove7(array):
#     for arr in range(len(array)):
#         if array[arr] == 7:
#             Index=arr
#     return Index
# array=[4,5,7]
# array.pop(remove7(array))
# print(array)
#Ex5

# def replaceOne(array):
#     result=""
#     for arr in range(len(array)):
#         if array[arr]==1:
#             array.pop(arr)
#             array.insert(arr,0)
#     return array
# array=[5,7,8,1]
# print(replaceOne(array))
##_____________________ S7
#Ex1
# array=["0","x","0"]
# hasx = True
# for i in range(len(array)):
#     if array[-1]=="x" and hasx:
#         hasx = False
#     if array[i] =="x" and hasx:
#         array[i] ="0"
#         array[i+1] ="x"
#         hasx = False
# print(array)

#Ex2
# array=[1,1,2,2]
# newarray=[]
# for arr in array:
#     if arr not in newarray:
#         newarray.append(arr)
# print(newarray)

#Ex3

# array2D=[
#     [1,7,3],
#     [1,0,3],
#     [1,0,3]
# ]
# for row in range(len(array2D)):
#     for column in range(len(array2D[row])):
#         if array2D[row][column] == 7:
#             indexrow=row
#             indexcolumn=column
# print("row: "  +str( indexrow) + " and " +"column: "+str(indexcolumn))
##_____________________ S8
