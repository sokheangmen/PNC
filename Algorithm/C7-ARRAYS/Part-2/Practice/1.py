# remove odd nb
numbers=eval(input())
newNb=[]
for value in numbers:
    if value%2==0:
        newNb.append(value)
print(newNb)