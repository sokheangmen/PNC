# numbers=[2,2,3,7]
# result=0
# for arr in numbers:
#     if arr%2==1:
#         result+=arr
# if result%2==1:
#     print("odd")
# else:
#     print("even")

# EX1

# arrayOfnumber=[1, 5, 9, 15] 
# iStrue=False
# for arr in arrayOfnumber:
#     if arr>10 and arr<=20 and arr!=15:
#         iStrue=True
# print(iStrue)

#Ex2

# arrayOfnumber = [7, 7]
# numbersAfter = 0
# numbersStart = 0
# iStrue = True
# for arr in arrayOfnumber:
#     numbersAfter = arr
#     if numbersStart <= numbersAfter and iStrue:
#         result = "ASCENDING"
#     else:
#         result = "ERROR"
#         iStrue = False
#     numbersStart = arr
# print(result)

# Ex3


# arrayDic=[
# {"name": "Jackma", "status": True},
# {"name": "Kolap baelen", "status": False},
# {"name": "Tom Teav", "status": True},
# {"name": "Elon mask", "status": False},
# {"name" :"Leadership", "status" : True}
# ]
# result=0
# for arr in arrayDic:
#     if arr["status"]==True:
#         result+=1
# print(result)


# Ex4

arrayDic1=[
    {"ingredient" : "noodle","quantity" : 200},
    {"ingredient" : "beef", "quantity" : 50}
]
arrayDic2=[
    {"ingredient": "noodle", "quantity": 300},
    {"ingredient": "beef", "quantity": 200},
    {"ingredient": "rice", "quantity": 300}
]
result=0
for key in arrayDic1:
    for key2 in arrayDic2:
        if key["ingredient"]==key2["ingredient"]:
            if key["quantity"]<key2["quantity"]:
                result+=1
if result==len(arrayDic1):
    print(True)
else:
    print(False)