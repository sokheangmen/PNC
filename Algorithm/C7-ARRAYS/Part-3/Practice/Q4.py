array2D1 = [[1,2,3],[4,5,6,7]]
array2D2 = [[1,2,3],[4,5,6,7,9,6,8]]
res = "not equal"
if len(array2D1)==len(array2D2):
    res = "equal"
    for i  in range(len(array2D1)):
        if len(array2D1[i]) == len(array2D2[i]):
            j = 0
            while res != "not equal" and j < len(array2D1[i]):
                if array2D1[i][j]==array2D2[i][j]:
                    res = "equal"
                else:
                    res = "not equal"
                j+=1
        else:
            res = "unequal"
print(res)