#>>>>>>>>>>>>>>>>>>>EX1
# def numberOfUpperCases(string):
#     Upper=0
#     for i in range(len(string)):
#         if string[i].isupper():
#             Upper+=1
#     return Upper
# string=input("Word:")
# print(numberOfUpperCases(string)) 
#>>>>>>>>>>>>>>>>>>>EX2
# def getComment(grade):
#     if grade>10:
#         result="Good"
#     else:
#         result="Bad"
#     return result
# grade=int(input("enter number:"))
# print(getComment(grade))
#>>>>>>>>>>>>>>>>>>>EX3
# def getPrice(fruitName):
#     if fruitName=="banana":
#         result=2
#     elif fruitName=="apple":
#         result=5
#     elif fruitName=="orange":
#         result=1
#     return result
# fruitName=input("inter string:")
# print(getPrice(fruitName),"$")
#>>>>>>>>>>>>>>>>>>>EX4
# def getAbsolute(number):
#     if number<0:
#         result=-1*number
#     else:
#         result=number
#     return result
# number=int(input("enter the number:"))
# print(getAbsolute(number))
#>>>>>>>>>>>>>>>>>>>EX5
# def max(number1,number2):
#     if number1>number2:
#         result=number1
#     else:
#         result=number2
#     return result
# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# print(max(number1,number2))
#>>>>>>>>>>>>>>>>>>>EX6
# def n(sritng):
#     result=""
#     for i in range(len(sritng)):
#         result+=sritng[-1-i]
#     return result
# strign=input()
# print(n(strign))