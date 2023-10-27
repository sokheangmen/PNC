# _____________ex1______________
array1=[-1]
array2=[-3,2]
sum1=0
sum2=0
for i in range(len(array1)):
    sum1+=i
for j in range(len(array2)):
    sum2+=j
if sum1>sum2:
    result=array1
elif sum1<sum2:
    reuslt=array2
elif sum1==sum2:
    result="Equal"
print(result)