def nbOfEight(array):
    result=0
    for i in array:
        if i==8:
            result+=1
        elif 8 not in array:
            result=-1
    return result
array=eval(input())
print(nbOfEight(array))