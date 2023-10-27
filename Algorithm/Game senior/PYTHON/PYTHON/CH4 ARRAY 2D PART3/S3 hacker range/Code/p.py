# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# indexOfRow=int(input())
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if indexOfRow==col:
#             array2D[row][indexOfRow] = '*'
#         if indexOfRow==row:
#             array2D[indexOfRow][col] = '*'
# print(array2D)
# _______________________________
# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# indexOfRow=int(input())
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if indexOfRow==col:
#             array2D[row][indexOfRow] = '*'
# print(array2D)
# ________________________________
# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]  
# ]
# indexOfRow=int(input())
# for row in range(len(array2D)):
#     if indexOfRow==row:
#         for col in range(len(array2D[row])):
#             array2D[indexOfRow][col] = '*'
# print(array2D)

# ________________________________
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

# ________________________________
# array2D=[
#     ["A", "B", "C"],
#     ["A", "B", "C"],
#     ["A", "B", "C"]
# ]
# indexOfRow=int(input())
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if array2D[row][col]==array2D[indexOfRow][col]:
#             array2D[indexOfRow][col] = '*'
# print(array2D)