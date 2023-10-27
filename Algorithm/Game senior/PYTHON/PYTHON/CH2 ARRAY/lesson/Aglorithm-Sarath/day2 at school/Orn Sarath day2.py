
# 1



# array=eval(input())
# boolan2=True
# boolan1=True
# indexOfZero = 0
# indexOfOne = 0
# for i in range(len(array)):
#     if array[i]==1 and  boolan2:
#         boolan2=False
#         indexOfOne = i

#     elif array[i]==0 and not boolan2 and boolan1:
#         boolan1=False
#         indexOfZero = i
# if boolan2 == boolan1 and boolan1 == False:
#     print(array[indexOfOne+1:indexOfZero])
# else:
    
#     print([])
# 2

# text =input()
# hasLetter=False
# for char in text:
#     if char.upper()=="A" or char.upper()=="B" or char.upper()=="C" or char.upper()=="D":
#         hasLetter=True
# print(hasLetter)

# 3
# newArray=[]
# for i in range(3):
#     number=int(input())
#     if 10<=number<=50:
#         newArray.append(number)
# print(newArray)

# 4

# letter =str(input())
# condition=False
# newStr=""
# for i in range(len(letter)):
#     if letter[i]==" ":
#         condition=True
#         newStr+=letter[i]
#     elif condition or i==0:
#         newStr+=letter[i].upper()
#         condition=False
#     else:
#         newStr+=letter[i]
# print(newStr)




# ------------------------------Extra


# 5

# materials = eval(input())
# result=0
# for i in materials:
#         if i['quality']=='Good':
#             result+=i['quantity']*i['retail_price']
# print(result)



# 6

# listOfNumber=eval(input())
# notFound=True
# for row in range(len(listOfNumber)):
#     for col in range(len(listOfNumber[row])):
#         if listOfNumber[row][col]==listOfNumber[row][col-1] or listOfNumber[col-1][row]==listOfNumber[col][row]:
#             notFound=False
# print(notFound)

# 7

# students=eval(input())
# classOfStudents =input()
# firstStudent=0
# nameOfStuden=""
# for i in students:
#     if classOfStudents==i['class'] and i['score']<firstStudent:
#         nameOfStuden=i['name']
#     firstStudent=i['score']
# print(nameOfStuden)















