#practice1
# def removeMinuses(word):
#     newWord=""
#     for i in range(len(word)):
#         if word[i]!="-":
#             newWord+=word[i]
#     return newWord
# Y=True
# while Y==True:
#     word=input("Enter Your String:")
#     print(removeMinuses(word))
#     restart=input()
#     if restart=="N":
#         Y=False

#practice2
# def sum(number1,number2):
#     return number1+number2
# number1=int(input())
# number2=int(input())
# print("The sum is:"+str(sum(number1,number2)))

#practice3
# def sum(sumValue): 
#     count=0
#     for i in range(inputNumber):
#         count+=1
#         inputValue=int(input("Value"+str(count)+ ":"))
#         sumValue+=inputValue
#     return sumValue
# sumValue=0
# inputNumber=int(input())
# print("The sum is: "+str(sum(sumValue)))


#4
def sum(value1,value2):
   return value1+value2
start = int(input())
end = int(input())
total = 0
for i in range(start,end+1):
      if start > end:
         total =0
      else:
         total += i
value1 = total
value2 = 0
print(sum(value1, value2))