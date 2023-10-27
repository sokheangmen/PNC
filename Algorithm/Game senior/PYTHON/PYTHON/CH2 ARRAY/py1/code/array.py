#>>>>>>>>>>>>>>EX1
def sum(arryOfNumber):
    value=0
    for i in range(len(arryOfNumber)):
        value+=arryOfNumber[i]
    return value
number=[5,6]
print(sum(number))
## arryOfNumberE=eval(input())
# print(sum(arryOfNumberE))
#>>>>>>>>>>>>>>EX2
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
#>>>>>>>>>>>>>>EX3
# def countname(arry):
#     value=0
#     for i in range(len(arry)):
#         if arry[i]=="rady":
#             value+=1
#     return value
# string=['ronan','rady','PNC']
# print(countname(string))
#>>>>>>>>>>>>>>EX4
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

# def n(arry):
#     e=0
#     o=0
#     for arr in arry:
#         if arr %2==0:
#             e+=1
#         else:
#             o+=1
#     return e,o
# number=eval(input())
# result=n(number)
# print("e:"str(result[0]))
# print("e:"str(result[0]))