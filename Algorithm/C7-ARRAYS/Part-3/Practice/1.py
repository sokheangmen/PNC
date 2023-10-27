array2d = [[1,2,3],[1,2,3],[1,2,3]]
number = []
for i in range(len(array2d)):
    newNumber=array2d[i]
    result = 0
    for value in range(len(newNumber)):
        result = result+newNumber[value]
    number.append(result)
print(number)