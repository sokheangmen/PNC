array=[
    [1,0,0,0,0,0,0],
    [1,0,0,0,5,0,0],
    [1,0,2,0,0,0,0]
]
result ="lost"
for row in range(len(array)):
    for column in range(len(array)):
        if array[row][column]==2:
            result ="winner"
print(result)
