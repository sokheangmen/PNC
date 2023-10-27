array2D=[
    [5,3,5],
    [4,7,8],
    [3,5,6]
]
# result=[]
arr=[]
for row in range(len(array2D)):
    result=0
    for col in range(len(array2D[row])):
        result+=array2D[col][row]
    arr.append(result)
print(arr)