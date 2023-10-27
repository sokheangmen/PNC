def sumBetweenNbTwo(numbers):
    isFoundNbtwo=False
    total=0
    for value in numbers:
        if value==2:
            isFoundNbtwo= not(isFoundNbtwo and total!=0)
        elif isFoundNbtwo:
            total+=value
    return total
numbers=eval(input())
print(sumBetweenNbTwo(numbers))
