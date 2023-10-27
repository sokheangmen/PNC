def sumFromTo(numbers):
    if numbers[0]<numbers[1]:
        total=0
        for i in range(numbers[0],numbers[1]+1,1):
            total+=i
    return total
numbers=eval(input())
print(sumFromTo(numbers))