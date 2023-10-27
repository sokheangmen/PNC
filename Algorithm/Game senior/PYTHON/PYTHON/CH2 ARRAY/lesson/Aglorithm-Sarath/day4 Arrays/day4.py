# 1

# myArray = [14, 15, 18, 20, 3]
# myElement = myArray[2]
# print(myElement)

# # or
# print(myArray[1])

# 2

# array = [1, 2, 3, 4, 5]
# for index in range(len(array)):
#     value = array[index]
#     print("hello " + str(value))

# array = [1, 2, 3, 4, 5]
# for value in array:
#     print("hello " + str(value))

# excercies========================
# 1=======

# def countNumber(arr):
#     result = 0
#     for i in range(len(arr)):
#         if arr[i] == 7:
#             result += 1
#     return result
# arr =  eval(input())
# print(countNumber(arr))

# nuber2=============================

# def compareOfNumber(arr):
#     result = 0
#     for i in range(len(arr)):
#         if i > 0 and (arr[i] > arr[i-1]):
#             result += 1
#     return result
# arr = eval(input("enter number:"))
# print(compareOfNumber("Result is: ", arr))

# number3=====================================
def fruitNames(words):
   countA = 0
   for value in words:
      for i in range(len(value)):
         if value[i] == "a" or value[i]=="A":
            countA +=1
   return countA
words = eval(input("Enter words: "))
print("Total number of A is: "+str(fruitNames(words)))



