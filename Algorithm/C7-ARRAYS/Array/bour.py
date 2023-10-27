# --1--
# array = [1,2,3,5,0,6]
# reult = False
# res = []
# for i in range(len(array)):
#     if array[i] == 0:
#         reult = False
#     if reult :
#         res.append(array[i])
#     if array[i] == 1:
#         reult = True
# print(res)

# --2--
# array = [1,2,3,4,5,0]
# reult = False
# sum=0
# for i in range(len(array)):
#     if array[i] == 0:
#         reult = False
#     if array[i] == 1:
#         reult = True
#     sum+=i
# print(sum)

# --3--
array = [0,1,2,3,4,5]
result = 0
for value in array:
    if value==2:
        result+=value
print(result)
