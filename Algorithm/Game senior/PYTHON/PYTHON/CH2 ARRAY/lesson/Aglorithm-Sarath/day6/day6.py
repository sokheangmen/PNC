
# ===============number1======================

# def compear(arr1,arr2):
#     result = "NOT EQUAL"
#     result1 = ""
#     result2 = ""
#     for i in arr1:
#         result1 += str(i)
#     for n in arr2:
#         result2 += str(n)
#     if result1 == result2:
#         result = "EQUAL"
#     return result
# arr1 = eval(input())
# arr2 = eval(input())
# print(compear(arr1,arr2))



def isEqual(list1,list2):
    return result
list1 = eval(input("Enter array1: "))
list2 = eval(input("Enter array2: "))
check1 = False
check2 = False
for i in range(1,len(list1)):
   fisrtIndex = list1[i-1]
   secondIndex = list1[i]
   if secondIndex>fisrtIndex:
      check1 = True
for i in range(1,len(list2)):
   fisrtIndex = list2[i-1]
   secondIndex = list2[i]
   if secondIndex>fisrtIndex:
      check2 = True
if check1 == check2:
   result = "EQUAL"
else:
   result = "NOT EQUAL"
print(isEqual(list1, list2))


# =======================number2=====================

# def compear(arr):
#     result = 0
#     for i in range(len(arr)):
#         if arr[i]>0 and arr[i] > arr[i-1]:
#             result += 1
#     return result
# arr = eval(input())
# print(compear(arr))

# =============number1===============
# def compear(n1,n2):
#     n =0
#     result = "hello"
#     for i in range(len(n1)):
#         if n1[i]!=n2[n]:
#             result = "NOt hello"
#         n += 1
#     return result
# n1 = eval(input())
# n2 = eval(input())
# print(compear(n1,n2))
