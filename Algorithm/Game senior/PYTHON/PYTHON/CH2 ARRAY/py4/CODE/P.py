#____________EX1______________
# def toContains(word,text):
#     iStrue=False
#     for i in range(len(word)):
#         if word[i].lower()== text.lower():
#             iStrue=True
#     return iStrue
# word=input()    
# text=input()
# iSfound=toContains(word,text)#cna write
# if iSfound==True:
#     print("Valid")
# else:
#     print("Not valid")

#____________EX2______________


# def toReverse(string):
#     result=""
#     for i in range(len(string)):
#         result += string[-(i+1)]
#     return result
# value=toReverse(input())
# print(value)

#____________EX3______________

# def multplyArray(array):
#     result=1
#     if len(array)==0:
#         result=result*0
#     for i in range(len(array)):
#             result*=array[i]
#     return result
# number=eval(input())
# print(multplyArray(number))


#____________EX4______________


def countChar(array,letter):
    result = 0
    for arr in range(len(array)):
        for index in range(len(array[arr])):
            text = array[arr]
            if text[index].upper()==letter.upper():
                result+=1
    return result 
# array=eval(input())
array=["hello","hi"]
letter="H"
# letter=str(input())
print(countChar(array,letter))

#____________EX5______________

# number=[8, 16]
# numStart = 0
# numEnd = number[0]
# if len(number) == 2:
#     numStart = number[0]
#     numEnd = number[1]
# loopOfSum = numEnd - numStart + 1
# value=0
# for i in range(loopOfSum):
#     value+=numStart + i
# result = value / loopOfSum
# conVert = str(result)
# for i in range(len(conVert)):
#     if conVert[-1] == "0":
#         result = int(result)
# print(result)
