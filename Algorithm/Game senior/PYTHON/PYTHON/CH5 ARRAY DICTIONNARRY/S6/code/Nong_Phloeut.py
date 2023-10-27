# EX1
# arrayOfnumber=eval(input())
# iStrue=False
# for arr in arrayOfnumber:
#     if arr>10 and arr<=20 and arr!=15:
#         iStrue=True
# print(iStrue)
#EX2
# arrayOfnumber = eval(input())
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
#EX3
# arrayDic=eval(input())
# result=0
# for arr in arrayDic:
#     if arr["status"]==True:
#         result+=1
# print(result)
#EX4
# arrayDic1=eval(input())
# arrayDic2=eval(input())
arrayDic1=[
{"ingredient": "noodle","quantity": 200},
{"ingredient": "beef", "quantity": 50},
{"ingredient": "bread", "quantity": 10}
]

arrayDic2=[
{"ingredient" : "banana", "quantity" : 100},
{"ingredient" : "beef", "quantity" : 200},
{"ingredient" : "noodle", "quantity" : 50},
{"ingredient" : "apple", "quantity" : 500}
]
result=0
for key in arrayDic1:
    for key2 in arrayDic2:
        if key["ingredient"]==key2["ingredient"]:
            if key["quantity"]<key2["quantity"]:
                result+=1
                print(result)
if result==len(arrayDic1):
    print(True)
else:
    print(False)