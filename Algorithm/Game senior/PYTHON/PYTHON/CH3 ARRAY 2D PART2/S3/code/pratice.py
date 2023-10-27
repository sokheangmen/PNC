number=eval(input())
allInRange=True
for i in range(len(number)):
    if number[i] <5 or number[i]>10:
        allInRange=False
print(allInRange)

#_______________EX2_______________________
# def createRow(number) :
# 	result = ""
# 	for i in range(len(number)):
# 		result += str(number)
# 	return result
# result = ""
# array = [1,2,4]
# for number in array :
# 	newRow = createRow(array)
# 	result += newRow
# 	result += "\n"
# print(newRow)


#_______________EX3_______________________

# array1 = [2,-5,7,3,4]
# array2 = [1,9,3]
# array3 = []
# sum1 = 0
# sum2 = 0
# sum3 = 0
# # Sum array1
# for number in array1 :
#     sum1 += number
#     if sum1 > sum2 and sum1 > sum3 : # if sum1 is the greatest
#         result = array1
#     elif sum3 > sum1 and sum3 > sum2 : # if sum3 is the greatest
#         result = array3
# # Sum array2
# for number in array2 :
#     sum2 += number
#     if sum3 > sum1 and sum3 > sum2 : # if sum3 is the greatest
#         result = array3
#     elif sum2 > sum1 and sum2 > sum3 : # if sum2 is the greatest
#         result = array2    
# # Sum array3
# for number in array3 :
#     sum3 += number
#     if sum3 > sum1 and sum3 > sum2 : # if sum3 is the greatest
#         result = array3
#     elif sum2 > sum1 and sum2 > sum3 : # if sum2 is the greatest
#         result = array2
# # Print output
#     else : # if there is no greatest sum
#         result = []
# print(result)

#_______________EX3_______________________
# array1 = [2,-5,7,3,4]
# array2 = [1,9,3]
# array3 = []
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for number in array1 :
#     sum1 += number
# for number in array2 :
#     sum2 += number
# for number in array3 :
#     sum3 += number
#     if sum1 > sum2 and sum1 > sum3 : 
#         result = array1
#     elif sum2 > sum1 and sum2 > sum3 :
#         result = array2
#     # elif sum3 > sum1 and sum3 > sum2 : 
#     #     result = array3
#     else :
#         result = []
# print(result)