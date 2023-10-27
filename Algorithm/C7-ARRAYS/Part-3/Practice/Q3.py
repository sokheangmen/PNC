
# array = [9,9,9,8,8,8,1,2,2,]
# number = []
# for i in range(len(array) - 1):
#     if array[i] == array[i+1]:
#           if array[i] not in number:
#             number.append(array[i])
# print(number)

# def find_duplicate_numbers(arr):
#     count_dict = {}
#     result = []
#     for value in arr:
#         if value in count_dict:
#             count_dict[value] += 1
#         else:
#             count_dict[value] = 1
#     for value, count in count_dict.items():
#         if count > 1:
#             result.append(value)
#     return result
# arr = [9, 9,9, 8, 8, 8, 3 , 1, 3]
# output = find_duplicate_numbers(arr)
# print(output)


arr2d = [9, 8, 1,8,3,9,2,3,2]
arr = []
for i in range(len(arr2d)):
    a = arr2d[i]
    count = 0
    for i in range(len(arr2d)):
        if a == arr2d[i]:
            count +=1
        if count > 1 and a not in arr:
            arr.append(a)
print(arr)