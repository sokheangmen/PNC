
# def sum(array,array1):
#     result = 0
#     result1 = 0
#     for i in range(len(array)):
#         result += array[i]
#     for i in range(len(array1)):
#         result1 = result1 + array1[i]
#     return result , result1
# array=[3,5,7,8,2] 
# array1=[3,5,7,8,45] 
# print(sum(array,array1))  


# array = [2,2,3,5]
# result = 0
# for i in range(len(array)):
#     result += array[i]
# print(result)



# def sum(array, array1):
#     merged_array = array + array1
#     result = 0
    
#     for i in range(len(merged_array)):
#         result += merged_array[i]
    
#     return result 

# array = [3, 5, 7, 8, 2]
# array1 = [3, 5, 7, 8, 45]
# print(sum(array, array1))

# ================================================================ex3
# arrayOfSting = ['ronan', 'hello', 'PNC','rady']

# indexOfSting = 0
# for i in range(len(arrayOfSting)):
#     if arrayOfSting[i] == "rady":
#         indexOfSting = i
# print(indexOfSting)

# ================================================================ex3

# def findIndexOfArray(arrayOfSting):
#     indexOfSting = 0
#     for i in range(len(arrayOfSting)):
#         indexOfSting = i
#     return indexOfSting
# arrayOfSting = ['ronan', 'hello', 'PNC','rady']
# print(findIndexOfArray(arrayOfSting))

# ================================================================ex4

arrayOfInteger = [3,5,1,9,7,2,0]
countEven = 0
countOdd = 0
for i in range(len(arrayOfInteger)):
    if arrayOfInteger[i] % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print("Even number : " + str (countEven) + '\n' + "Odd number : " + str (countOdd))



# arrayOfInteger = [3, 5, 1, 9, 7, 2, 0]

# arrayOfInteger = "hello world"
# count = 0

# for num in arrayOfInteger:
#     count += 1

# print(count)






