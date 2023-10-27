def sum(array):
    value=0
    odd=0
    for arr in array:
        if arr%2==0:
            value+=1
        else:
            odd+=1
    return value ,odd
number=eval(input())
result=sum(number)
print("even:"+str(result[0]))
print("odd:"+str(result[1]))