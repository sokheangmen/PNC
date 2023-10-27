# --1--
# arrays= [1,2,3,5,6,9,10,15]
# result=0
# for i in range(len(arrays)-1):
#     if arrays[i]<arrays[i+1]:
#         result=arrays[i+1]
# print(result)

# --2--
# arrays= [1,2,3,5,6,9]
# for i in range(len(arrays)):
#     if arrays[i]==5:
#         arrays[i]=10
# print(arrays)

# --3--
arrays = [2,4,5,7,8]
result = 0
for i in range(len(arrays)):
    result = arrays[0] + arrays[4]
print(result)