#___________Ex1______________

# def name(array):
#     result=0
#     for i in array:
#         for j in i:
#             if j=="a" or j=="A":
#                 result +=1
#     return result
# string=["Him","Mengheang","Sokhom"]
# print(name(string))

#___________Ex2______________

# def containUpperCase(string):
#     iStrue=False
#     for i in range(len(string)):
#         if string[i].upper()==string[i]:
#             iStrue=True
#     return iStrue
# word=str(input())
# result=containUpperCase(word)
# if result==True:
#     print("Valid")
# else:
#     print("Not valid")

#___________Ex3______________

# def reverseString(string):
#     result=""
#     for i in range(len(string)):
#         result+=string[-(1+i)]
#     return result
# word=str(input())
# print("The reverseString is: "+str(reverseString(word)))

#___________Ex4______________

def averang(listOfNumber):
    result=0
    index=0
    for i in range(list):
        newinput=eval(input())
        for j in range(len(newinput)):
            result+=newinput[j]
            index=i
    return result/index
list=int(input())
print(averang(list))
