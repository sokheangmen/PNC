room = [
[1, 0, 0],
[0, 0, 0],
[0, 0, 1]
]
print(room)

peopleCount = 0
for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] == 1 :
            peopleCount += 1

if peopleCount < 3 :
    nbOfRow = int(input("Enter number of row :"))
    nbOfCol = int(input("Enter number of column :"))
    if room[nbOfRow][nbOfCol] != 1:
        room[nbOfRow][nbOfCol] = 1
        result = "Can add"
        print(result)
        print(room)
    else:
        result = "Can not add"   
        print(result)
else:
    result = "Can not add"
    print(result)