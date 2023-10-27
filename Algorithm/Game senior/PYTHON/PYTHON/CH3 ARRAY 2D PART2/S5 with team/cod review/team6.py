array1 =eval(input("array1: "))
array2 =eval(input("array2: "))
sum1 = 0
sum2 = 0

for i in array1 :
    sum1 += i
for i in  array2 :
    sum2 += i

if sum1 > sum2 :
    result = array1
elif sum2 > sum1 :
    result = array2
else :
    result = "Equal"

print(result)
