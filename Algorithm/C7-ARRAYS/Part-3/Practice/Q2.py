arr2D = eval(input("input array2D: "))
simpleArr = []
for i in range(len(arr2D)):
    arr = "" 
    for j in range(len(arr2D[i])):
        arr += arr2D[i][j].lower()
    simpleArr.append(arr)
print(simpleArr)