# # Ex1
# array2D=[
#     [4,5,6],
#     [4,2,7],
#     [6,7,5]
# ]
# iSTrue=False
# result=[]
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if array2D[row][col]==7  and not iSTrue:
#             result.append(row)
#             result.append(col)
#             iSTrue=True
# print(result)

# Ex2

# array2D=[
#     [5,7,8,9],
#      [5,7,8,9],
#       [5,7,8,9],
#        [5,7,8,9],
# ]

# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if array2D[row][col]==7:
#             array2D[row][col]=8
# print(array2D)

# Ex3

# array2D=[
#    [5,6,0,4],
#       [5,6,7,4],
#         [5,6,8,4],
#           [5,6,6,4],
# ]
# result=[]
# for row in range(len(array2D)):
#     arr=0
#     for col in  range(len(array2D[row])):
#         arr+=array2D[col][row]
#     result.append(arr)
# print(result)

# Ex4

# array=['banana', 'cococnut', 'mango']
# arr=[]
# for row in range(len(array)):
#     result=[]
#     for col in range(len(array[row])):
#         result.append(array[row][col].upper())
#     arr.append(result)
# print(arr)

# Ex5



# array2D=[
#     ["A","B","C"],
#     ["A","B","C"],
#     ["A","B","C"],
#     ["A","B","C"],
# ]
# index=int(input())
# result=[]
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if row==index:
#             array2D[row][col]="*"
# print(array2D)


# Ex6


# array2D=[
#     [1,7,3],
#     [1,9,3],
#     [8,7,3],
# ]
# result=[]
# for arr in array2D:
#     maxnumber=0
#     for col in arr:
#         if col>maxnumber:
#             maxnumber=col
#     result.append(maxnumber)
# print(result)



# Ex7

# array2D=[
#     ["A","B","C"],
#     ["A","B","C"],
#     ["A","B","C"],
#     ["A","B","C"],
# ]
# index=int(input())
# result=[]
# for row in range(len(array2D)):
#     if row==index:
#         for col in range(len(array2D[row])):
#             array2D[col][row]="*"
# print(array2D)

# EX8

from array import array


def hasMonsterOnCel(position,row,col):
    iSTrue=False
    for arr in position:
        if arr[0]==row and arr[1]==col:
            iSTrue=True
    return iSTrue
array2D=[
    [3,3]
    [3,3]
    [4,0]
]