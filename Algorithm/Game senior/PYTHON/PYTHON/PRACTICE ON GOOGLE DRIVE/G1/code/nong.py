#EX1
# words=["ronan","rady"]
# newwords=str(input())
# words.append(newwords)
# print(words)
#EX2
# def removenumber7(number):
#     arr=[]
#     for i in range(len(number)):
#         if number[i]!=7:
#             arr.append(number[i])
#     return arr
# number=[4,5,7,8]
# print(removenumber7(number))
#EX3
# def sum2By2(numbers):
#     result = []
#     for i in range(1, len(numbers)):
#         result.append(numbers[i-1]+numbers[i])
#     return result
# values = [1, 2, 3, 4, 5]
# print(sum2By2(values))
#EX4
values = [5,4,3,2]
hasPair=False
for i in range(len(values)) :
    for j in range(len(values)) :
        if i!=j and values[i] == values[j] :
            hasPair =True
if hasPair:
    print("HAS PAIR")
else:
    print("HAS NO PAIR")# MAIN CODE

