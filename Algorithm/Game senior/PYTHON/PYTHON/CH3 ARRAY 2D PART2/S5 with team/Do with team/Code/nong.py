#++++++++++++++EX1+++++++++++++++++

# array = [54,48,134]
# iSTrue = True
# for arr in array:
#     if arr < 8 and arr <= 12:
#         iSTrue = False
# print(iSTrue)

#++++++++++++++EX2+++++++++++++++++

array=[]
iSOne = False
iSZero = True
result = []
for i in array:
    if i == 1 and not iSOne:
        iSOne = True
    elif i != 0 and iSOne and iSZero:
        result.append(i)
    elif i == 0 and iSOne and iSZero:
        iSZero = False
if iSZero != True:
    iSResult = result      
else:
    iSResult = []
print(iSResult)


#++++++++++++++EX3+++++++++++++++++

# array =eval(input("arrayOfNumber:"))
# sumOfNmber = 0
# index = 0
# averangeOfSum = 0
# if len(array) > 0:
#     for i in range(len(array)):
#         sumOfNmber += array[i]
#         index += 1
#         averangeOfSum = sumOfNmber/index
# if  averangeOfSum >= 50 :
#     result = "Pass"
# else:   
#     result = "Fail"
# print(result)

#++++++++++++++EX4+++++++++++++++++

# stringOfArray = eval(input("Enter string: "))
# result = 0
# for arr in stringOfArray:
#     if arr == True:
#         result += 1
# print(result)

#++++++++++++++EX5+++++++++++++++++

# number = int(input("Enter The Number: "))
# for i in range(number + 1):
#     if i %2 == 0:
#         print(i,end=" ")


