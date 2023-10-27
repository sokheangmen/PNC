# def countNbOfX(text):
#     count=0
#     for i in range(len(text)):
#         if text[i]=="X":
#             count+=1
#     return count
# print(countNbOfX("XXACCXXX"))


def countNbOfX(text):
    count=0
    for i in range(len(text)):
        if text[i]=="X":
            count+=1
    return count
input=input()
print(countNbOfX(input))