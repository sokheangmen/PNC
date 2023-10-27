###Ex1>>>>>>>>>>>>>>>>
# def removeMinuses(string):
#     result=""
#     for i in range(len(string)):
#         if string[i] !="-":
#             result+=string[i]
#     return result
# isContinue=True
# while isContinue:
#     string=str(input("Enter a word:"))
#     print(removeMinuses(string))
#     Question =str(input("Do you want to continue?(yes/no): "))
#     Question =Question.upper()
#     if Question != "Y" and Question !="YES":
#         print("program finished successfully")
#         isContinue=False
##Ex2>>>>>>>>>>>>>>>>
# def sum(number1, number2):
#     return number1+number2
# number1=int(input())
# number2=int(input())
# print(sum(number1, number2))
###Ex3>>>>>>>>>>>>>>>>
# def sum():
#     value=0
#     for i in range(myresult):
#         mysum=int(input("value"+str(i+1)+str(": ")))
#         value+=mysum
#     return value
# myresult=int(input("internumber:"))
# print(sum())
##EX4>>>>>>>>>>>>>>>>
def sumFromTo(startValue,endValue):
    sum=0
    for i in range(startValue,endValue+1):
        sum+=i
    return sum
startValue=int(input("startValue:"))
endValue=int(input("endValue:"))
# print(sumFromTo(startValue,endValue))
print("between"+str(startValue)+"and"+str(endValue)+"is: "+sumFromTo(startValue,endValue))