# =======================number2====================

# array2D  = [[1,7,3],[9,3,6],[4,8,5]]
# arrayOfOddNum =[]
# for row in range(len(array2D)):
#     oddNum = 0
#     for col in range(len(array2D[row])):
#         if array2D[row][col] %2==1:
#             oddNum +=1
#     arrayOfOddNum.append(oddNum)
# print(arrayOfOddNum)

# =========================nu3==============================

# array2D = [[1,7,3],[9,3,6],[4,8,5]]
# newArray = []
# for col in range(len(array2D[0])):
#     sum =0
#     amountOfNumCol = 0
#     for row in range(len(array2D)):
#         sum += array2D[row][col]
#         amountOfNumCol +=1
#     average = sum//amountOfNumCol
#     newArray.append(average)
# print(newArray)
        
# ==============n4=====================

# array2D =[ ['A', 'B', 'C'],['H', 'D', 'Z'], ['Y', 'R', 'Y'],]
# numOfCol = 3
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if numOfCol == col:
#             array2D[row][col] = "*"
#         elif (len(array2D)-1) < numOfCol:
#             array2D = "Out of range"
# print(array2D)

# ===================n1===========================
# array =[ [3, 3],[1, 2],[4, 0] ]


def hasMonsterOnCell (monsterPosition, cellX, cellY):
    # Write your code here !
    hasMonster = False
    for a in range(len(monsterPosition)):
        if monsterPosition[a][0]==cellX  and monsterPosition[a][1] == cellY:
            hasMonster = True
    return hasMonster
# MAIN CODE 
values = [ [3, 3],[1, 2],[4, 0] ]
results = ""
# Write your code here !
for i in range(5):
    result = ""
    for n in range(5):
        if hasMonsterOnCell (values, i, n):
            result += "*"
        else:
            result += "0"
    results += result + "\n"
print(results)
