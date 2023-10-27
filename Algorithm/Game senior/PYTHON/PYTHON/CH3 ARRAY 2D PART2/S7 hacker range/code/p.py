array=["0","X","0","0"]
iStue=True
for i in range(len(array)):
    if array[i-1] =="X" and iStue:
        iStue=False
    elif  array[i]=="X" and iStue:
        array[i]="0"
        array[i+1]="X"
        iStue=False
print(array)