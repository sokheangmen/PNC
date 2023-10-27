
# remove even nb
numbers=eval(input())
newNb=[]
for value in numbers:
    if value%2==1:
        newNb.append(value)
print(newNb)