# 1



# def foundIndexOfChar(text,index):
#     result=""
#     for i in range(len(text)):
#         if i==index:
#             result+=text[i]
#     return result
    

# text =input()
# indexOfChar =int(input())
# if len(text)<indexOfChar:
#     print("Index out of range input  again.")
#     indexOfChar=int(input())
#     foundIndexOfChar(text,indexOfChar)
# else:
#     foundIndexOfChar(text,indexOfChar)

# print(foundIndexOfChar(text,indexOfChar))



# 2



# def cameIToSnake(text):
#     notUpper=True
#     result = ""
#     for char in range(len(text)):
#         if text[char].isalpha():
#             if text[char]==text[char].upper():
#                 result += "_" +text[char].lower()
#                 notUpper=False
#             else:
#                 result+=text[char]
#     if notUpper:
#         result="None"
#     return result

# text = input()
# print(cameIToSnake(text))
        


# 3


amountOfFruits = int(input())
listOfFruits=[]
sumOfMoney=0
notEnought=True
nameFruite=""

for i in range(amountOfFruits):
    storValueOfArrayDis={}
    nameOfFruite=input()
    money=int(input())
    storValueOfArrayDis["name"]=nameOfFruite
    storValueOfArrayDis["price"]=money
    sumOfMoney+=money
    if sumOfMoney<=40:
        listOfFruits.append(storValueOfArrayDis)
    elif notEnought and sumOfMoney>40 :
        nameFruite =  storValueOfArrayDis["name"]
        notEnought=False
if sumOfMoney<=40:
    print(listOfFruits)
else:
    
    print(str(listOfFruits)+ '\n'+ 'Erroe not enought money ' + str(nameFruite))




    


            
        



