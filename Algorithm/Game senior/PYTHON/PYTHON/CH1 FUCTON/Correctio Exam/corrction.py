# def reverseString(string):
#     textString1=""#
#     textString2=""#
#     for i in range(len(string)):#
#         for j in range(len(i)):#
#             if i:
#                 textString1+=j
#             return textString1#return 
#         for k in range(i+1):
#             if i:
#                 textString2+=k
#             return textString2
# string=("Mengo","Coconut")
# print(reverseString(string))

# correction


def reverseOfString(string):
    result=0
    for i in range(len(string)):
        for j in string[i]:
            if j =="A" or j== "a":
                result+=1
            # print(j,end="")
    return result
string=["AMengoa","Coconut"]
print(reverseOfString(string))



# def reverseString(word):
#     newText = ""
#     for i in range(len(word)):
#         newText += word[len(word) - 1 - i]
#     return newText

# itemsList = eval(input("Enter list: "))

# for item in itemsList:
#     print("The reverse of " + str(item) + " is " + str(reverseString(item)))