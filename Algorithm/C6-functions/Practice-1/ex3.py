def sumNumber(num):
    total = 0
    for i in range(num):
        value = int(input("..."))
        total += value
    return total
num = int(input())
print(sumNumber(num))