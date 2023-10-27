# # ---1---
# def number(array):
#     result=0
#     for value in array:
#         result+=value
#     return result
# array=[8,2,3,0,7]
# print(number(array))


# # ---2---
# def word(text):
#     result = 0
#     res = 0
#     for i in range (len(text)):
#         if text[i].isupper():
#             result+=1
#         elif text[i].islower():
#             res+=1
#     return result,res
# text =("I am a student at PNC")
# print (word(text))

# ---3---
array=[1,2,3,4,5,6,7,8]
sum=[]
for value in array:
    if value%2==0:
        sum.append(value)
print(sum)


    
