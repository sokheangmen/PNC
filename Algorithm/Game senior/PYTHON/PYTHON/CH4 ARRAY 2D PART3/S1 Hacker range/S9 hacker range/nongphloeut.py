# EX1
# array=[
#     [5,3,8,4],
#     [3,8,7,1],
#     [1,4,6,3]
# ] 
# index=[]
# for row in range(len(array)):
#     for culumn in range(len(array[row])):
#         if array[row][culumn]==7:
#             index.append(row)
#             index.append(culumn)
# print(index)


# EX2

# array2D=[
#     [5,7,8,4],
#     [5,7,8,4],
#     [5,7,8,4],
# ]
# for row in range(len(array2D)):
#     newarray2D=""
#     for culumn in range(len(array2D[row])):
#         if array2D[row][culumn]==7:
#             array2D[row][culumn]=8
# print(array2D)

# EX3
# array2D=[
#     [1,2,3,8],
#     [4,5,6,7],
#     [7,8,8,5]
# ] 
# result=[]
# for row in range(len(array2D[0])):
#     sum=0
#     for col in range(len(array2D)):
#         sum+=array2D[col][row]
#     result.append(sum)
# print(result)




array2D=[
    [5,6,0,4],
      [5,6,7,4],
        [5,6,8,4],
          [5,6,6,4],
]
position=[]
for row in range(len(array2D)):
    sum=0
    for col in range(len(array2D[row])):
        sum+=array2D[col][row]
    position.append(sum)
print(position)