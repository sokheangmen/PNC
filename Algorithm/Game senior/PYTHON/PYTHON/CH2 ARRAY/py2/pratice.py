#ex1
# def countNegative(array):
#     result=0
#     for arr in array:
#         if arr > 0:
#             result+=1
#     return result
# number=[12,-1,20,-4,10,-29]
# # print(countNegative(number))
# print("Thee number of Neagtive number is:" +str(countNegative(number)))
#ex2


# def indexOfMin(myArray):
#     num = myArray[0]
#     indexOfMin = 0
#     for index in range(len(myArray)):
#         value = myArray[index]
#         if value < num :
#             num = value 
#             indexOfMin = index
#     return indexOfMin
# number=[]
# print(indexOfMin(number))


#ex3
# def getindexOfNumberFive(array):
#     result=0
#     iStrue=True
#     for i in range(len(array)):
#         if array[i] == 5 and iStrue:
#             iStrue=False
#             result=i
#     return result
# number=[1,7,6,5,3,4]
# print(getindexOfNumberFive(number))

#ex4

# def sumOdd_EvenNumber(array):
#     OddNumber=0
#     EvenNumber=0
#     for i in range(len(array)):
#         if array[i] %2==0:
#             EvenNumber+=array[i]
#         else:
#            OddNumber+=array[i]
#     return [ OddNumber,EvenNumber]
# number=[1,2,3,4]
# result=sumOdd_EvenNumber(number)
# print("Sum of Even is:" +str(result[0])+ "!Sum of Odd is:" +str(result[1]))

#ex5

# def replaceNumber(array):
#     for i in range(len(array)):
#         if array[i]==9:
#             array[i]=168
#     return array
# number=[1,9,9,3,9]
# print(replaceNumber(number))

#Ex6

# def replaceLetter(array):
#     result=""
#     for index in array:
#         result+=" "
#         for i in range(len(index)):
#             if index[i]=="a":
#                 result += "$"
#             else:
#                 result +=index[i]
#         result+=  "'"
#         result+=  ","
#     return result
# arrayName = [ "ronan","rady","him","ratha", "mengheang"]
# result=replaceLetter(arrayName)
# print("[",result,"]")

# Tip2

def replaceLetter(arrayName):
    for i in range(len(arrayName)):
        name = arrayName[i]
        result=""
        for j in range(len(name)):
            if name[j].upper() == "A":
                result+="$"
            else:
                result+=name[j]
    # arrayName[i]=result
    return result
number=["ronan","rady"]
print(replaceLetter(number))