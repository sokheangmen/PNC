# --1--
# arrays= [1,2,3,5,6,9]
# result=0
# for i in range(len(arrays)-1):
#     if arrays[i]<arrays[i+1]:
#         result=arrays[i+1]
# print(result)


# --2--
# arrays= [1,2,3]
# result=1
# for value in arrays:
#    result=result*value
# print(result)

# --3--
arrays= ["Banana"]
for i in range(len(arrays)):
    count=0
    for j in range(len(arrays[i])):
        count +=1
print(count)
