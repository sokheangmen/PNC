# case 1 :
Array2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
newArray=[]
for row in range(len(Array2D[0])):
    result=0
    # print(row)
    for col in range(len(Array2D)):
        result+=Array2D[col][row]
        # print(row)
    newArray.append(result)
print(newArray)
