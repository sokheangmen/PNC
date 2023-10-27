# SESSION1>>>>>>>>>>>>>>>>>>>>>>
#______________EX1________________
# def CounNegative(array):
#     value=0
#     for i in range(len(array)):
#         if array[i]<0:
#             value+=1
#     if value == 0:
#         value = -1
#     return value
# number= [2,-12,-4,10,-9]
# print(CounNegative(number))

#______________EX2________________

# def indexOfMin(myArray):
#     num = 0
#     indexOfMin = 0
#     for index in range(len(myArray)):
#         if num > myArray[index]:
#             indexOfMin+=1
#     if len(myArray)==0:
#         indexOfMin="None"
#     return indexOfMin
# number=[]
# print(indexOfMin(number))
#______________EX3________________

# def countNumber(array):
#     result=0
#     iStrue=True
#     for i in range(len(array)):
#         if array[i]==5 and iStrue:
#             result=i
#             iStrue=False
#     return result
# number=[1,2,3,4,5,5]
# print("number is:"+str(countNumber(number)))

#______________EX4________________


# def sumEventNumber(array):
#     Even=0
#     Odd=0
#     for arr in array:
#         if array[arr]%2==0:
#             Even+=array[arr]
#         else:
#             Odd+=array[arr]
#     return Even,Odd
# number=[2,3,4,5,2,3]
# result=(sumEventNumber(number))
# print("Even:"+str(result[0]) + "_Odd:"+str(result[1]))

#______________EX5________________

# def replaceNumber(array):
#     for i in range(len(array)):
#         if array[i]==9:
#             array[i]=168
#     return array
# number=[1,3]
# print(replaceNumber(number))
#______________EX6________________

# def replaceLetter(arrayName):
#     for i in range(len(arrayName)):
#         name = arrayName[i]
#         result=""
#         for j in range(len(name)):
#             if name[j].upper() == "A":
#                 result+="$"
#             else:
#                 result+=name[j]
#     # arrayName[i]=result
#     return result
# number=["ronan","rody"]
# print(replaceLetter(number))

# SESSION2>>>>>>>>>>>>>>>>>>>>>>

#______________EX1________________
# def sum(arryOfNumber):
#     value=0
#     for i in range(len(arryOfNumber)):
#         value+=arryOfNumber[i]
#     return value
# number=[10,11]
# print(sum(number))
#______________EX2________________
# def numberOfEight(arry):
#     value=0
#     for i in range(len(arry)):
#         if arry[i] == 8:
#             value+=1
#     if value == 0:
#         value+=-1
#     return value
# number=[3,6,7,8,8,8]
# print(numberOfEight(number))
#______________EX3________________

# def countname(arry):
#     value=0
#     for i in range(len(arry)):
#         if arry[i]=="rady":
#             value+=i
#     return value
# string=['ronan','PNC','rady']
# print(countname(string))

#______________EX4________________
# def countEvne(arry):
#     even=0
#     odd=0
#     for i in range(len(arry)):
#         if arry[i] %2==0:
#             even+=1
#         else:
#             odd+=1
#     return [even,odd]
# number=[3,5,1,9,7,2,0]
# # number=eval(input())
# result=countEvne(number)
# print("EVEV:"+str(result[0]))
# print("ODD:"+str(result[1]))

# SESSION3>>>>>>>>>>>>>>>>>>>>>>
#_____________>EX1 _______________
# def isEqual(list1, list2):
#     isEqual = True 
#     if len(list1) != len(list2):
#         isEqual = False
#     else:
#         for i in range(len(list1)):
#             if array1[i] != array2[i]:
#                 isEqual = False
#     return isEqual
# array1 = []
# array2 = []
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
# array1 = [3,5,1]
# array2 = [5,1]
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
# number=[3,1,4]
# print(NunberOfCompare(number))

#_____________>EX4_______________

# def sumFromTo(startValue,endValue):
#     sum=0
#     for i in range(startValue,endValue+1):
#         sum+=i
#     return sum
# startValue=int(input("startValue: "))
# endValue=int(input("endValue: "))
# # print(sumFromTo(startValue,endValue))
# result=sumFromTo(startValue,endValue)
# print("isEqual : "+str(result))
#_____________>EX5_______________

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
#_____________>EX6_______________

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
# number=eval(input())
# print(sumBetweenNumberTwo(number))

