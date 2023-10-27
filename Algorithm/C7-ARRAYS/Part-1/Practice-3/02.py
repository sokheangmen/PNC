def numberOfCompare(array):
    result=-1
    for i in range(len(array)):
        if array[1]>array[0]:
            result+=1
        elif array[1]<array[0]:
            result=1   
    else:
        result=0
    return result
array=eval(input())
print(numberOfCompare(array))