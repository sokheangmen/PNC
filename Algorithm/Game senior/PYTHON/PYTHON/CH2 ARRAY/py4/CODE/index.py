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

# def toContains(word,string):
#     iStrue=False
#     for i in range(len(word)):
#         if word[i].lower()== string.lower():
#             iStrue=True
#     return iStrue
# word=["Ronan"]
# string=["A"]
# letter=toContains(word,string)
# if letter==True:
#     print("yes")
# else:
#     print("no")