def sumFormTo(start,end):
    total=0
    for i in range(start,end+1):
        total+=i
    return total
start=int(input())
end=int(input())
print(sumFormTo(start,end))