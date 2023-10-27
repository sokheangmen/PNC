# def isEqual(list1, list2):
#     isEqual = True 
#     if len(list1) != len(list2):
#         isEqual = False
#     else:
#         for i in range(len(list1)):
#             if array1[i] != array2[i]:
#                 isEqual = False
#     return isEqual
# array1 = [1,2,3]
# array2 = [1,0,3]
# result = isEqual(array1, array2)
# if result:
#     print("Equal")
# else: 
#     print("Not Equal")
#_____________>EX2_______________
# def isEqual(list1, list2):
#     isEqual="Equal"
#     if len(list1) == len(list2):
#         for i in list1:
#             if not(i in list2):
#                 isEqual="Not equal"
#     else:
#         isEqual="Not equal"
#     return isEqual
# array1 = [3,2,1]
# array2 = [6,3]
# result = isEqual(array1, array2)
# print(result)
#_____________>EX3_______________


# def NunberOfCompare(array):
#     mynumbernew = array[0]
#     for i in array:
#         if mynumbernew> i:
#             newnumber = i
#         mynumbernew = i
#     return newnumber
# number=[5,4,3]
# print(NunberOfCompare(number))

#_____________>EX4_______________

def sumFromTo(startValue,endValue):
    sum=0
    for i in range(startValue,endValue+1):
        sum+=i
    return sum
startValue=int(input("startValue: "))
endValue=int(input("endValue: "))
# print(sumFromTo(startValue,endValue))
result=sumFromTo(startValue,endValue)
print("isEqual : "+str(result))


# def isEqual(list1, list2):
#     isEqual="Equal"
#     if len(list1) == len(list2):
#         for i in list1:
#             if not(i in list2):
#                 isEqual="Not equal"
#     else:
#         isEqual="Not equal"
#     return isEqual
# array1 = [3,2,1]
# array2 = [6,3]
# result = isEqual(array1, array2)
# print(result)
#_____________>EX5_______________

# def sumBetweenNumberTwo(array):
#     result=0
#     iStrue=False
#     for i in range(len(array)):
#         text=array[i]
#         if text==2 and not iStrue:
#             iStrue=True
#         elif text!=2 and iStrue:
#             result+=text
#         elif text==2:
#             iStrue=False
#     return result
# number=[2,3,2,5,2,1]
# # number=eval(input())
# print(sumBetweenNumberTwo(number))

# n="PNC"
# result=""
# for i in range(len(n)):
#     result+=n[-(i+1)]
# print(result)


