# # ---1--
# array=[2,3,4,5,6]
# sum=0
# for value in array:
#     sum+=value
# print(sum)

# # # ---2--
# array=[1,2,3,4,5,6,7,8]
# sum=0
# for value in array:
#     if value%2==0:
#         sum+=value
# print(sum)

# # ---3--
array=["Meng Heang","Mey Heang"]
result=0
for value in array:
    for i in value:
        if i=="H":
            result+=1
print(result)