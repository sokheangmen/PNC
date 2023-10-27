#EX2
array2D=[
    [1,2,5],
    [10,2,8],
    [1,8,9]
]
array1D=[]
for arr in array2D:
    max=0
    for col in arr:
        if col>max:
            max=col
    array1D.append(max)
print(array1D)
#EX3
# array2D=["A", "B", "C"]
# number=int(input())
# result=[]
# for row in range(len(array2D)):
#     if number==row:
#         array2D[row]="*"
#     result.append(array2D[row])
# print(result)
# EX3

# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# indexOfRow=int(input())
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if indexOfRow==row:
#             array2D[indexOfRow][col] = '*'
# print(array2D)


# tip2

# array2D=[
#     [1,4,2],
#     [1,8,2],
#     [10,9,2]
# ]
# # indexOfRow=int(input())
# indexOfRow=3
# for row in range(len(array2D)):
#     if indexOfRow==row:
#         for col in range(len(array2D[row])):
#             array2D[row][col] = array2D[row][col]
#             array2D[row][col]="*"
# print(array2D)
# tip3


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
