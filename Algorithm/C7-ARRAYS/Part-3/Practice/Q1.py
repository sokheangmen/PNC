arrays = [["A","B","C"],["C","D","E"],["E","R","X"]]
indexOfcolum = int(input("Enter here :"))
for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        if indexOfcolum == j:
            arrays[i][j] = "*"
if indexOfcolum > j:
    arrays = "Error code"
print(arrays)