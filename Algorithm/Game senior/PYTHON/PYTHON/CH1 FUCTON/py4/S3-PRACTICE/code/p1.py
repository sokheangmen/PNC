#%%ex1
# def numberOfUpperCases(string):
#     Upper=0
#     for i in range(len(string)):
#         if string[i].isupper():
#             Upper+=1
#     return Upper
# string=input("Word:")
# print(numberOfUpperCases(string)) 
#%%%EX2
# def getComment(grade):
#     if grade>10:
#         result="Good"
#     else:
#         result="Bad"
#     return result
# grade=int(input("enter number:"))
# print(getComment(grade))
#%%ex3
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
#%%ex4
# def getAbsolute(number):
#     if number<0:
#         result=-1*number
#     else:
#         result=number
#     return result
# number=int(input("enter the number:"))
# print(getAbsolute(number))
#%%ex5
# def max(number1,number2):
#     if number1>number2:
#         result=number1
#     else:
#         result=number2
#     return result
# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# print(max(number1,number2))
#%%ex6
# def reverseString(string):
#   return string[::-1]
# mytxt = reverseString(input ())
# print(mytxt)
#%%6tip2
# def reverseString(string):
#     result = ""
#     lastIndex = len(string) - 1
#     for i in range(len(string)):
#         result += string[lastIndex - i]
#     return result
# string=input()
# print(reverseString(string))
#%%
def n(sritng):
    result=""
    for i in range(len(sritng)):
        result+=sritng[-1-i]
    return result
strign=input()
print(n(strign))