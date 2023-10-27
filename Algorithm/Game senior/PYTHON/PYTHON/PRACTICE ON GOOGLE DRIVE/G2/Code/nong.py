# Ex4
words=[
    ["A,A,A"],
    ["B,B,A"],
    ["B,B,B"]
]
resultA=0
# resultB=0
# resultC=0
for row in range(len(words)):
    for column in range(len(words[row])):
        if words[column]=="A":
            resultA+=1
            print("A")
#         if words[column]=="B":
#             resultB+=1
#         if words[column]=="C":
#             resultC+=1
# if resultA==3:
#     print("A")
# if resultA==3:
#     print("B")
# if resultA==3:
#     print("C")
# else:
#     print("no winer")