def isEqual(array1,array):
    result="Equal"
    for value in array:
        if array1!=array2:
            result="No Equal"
    return result
array1=eval(input())
array2=eval(input())
print(isEqual(array1,array2))