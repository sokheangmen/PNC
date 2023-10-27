# Ex1
# array=[
#         {"name": "banana","price": 1000,"quantity": 1,},
#         {"name": "mango","price": 4000,"quantity": 2,}
#     ]
# result=0 
# for i in array:
#     total=i["price"]*i["quantity"]
#     result +=total
# print(result)

# Ex2
# arrayDic=[
    # {'fruit': 'banana', 'qty': 10, 'price': 100},
    # {'fruit': 'coconut', 'qty': 5, 'price': 10},
    # {'fruit': 'mango', 'qty': 12, 'price': 30},
    # {'meat': 'bird', 'qty': 1, 'price': 60},
    # {'meat': 'fish', 'qty': 3, 'price': 30},
# ]
# sumFruit=0
# sumMeat=0
# for i in arrayDic:
#         for key in i:
#             if key=="fruit":
#                 sumFruit+=1
#             elif key=="meat":
#                 sumMeat+=1
# print(("meat: ")+str(sumMeat))
# print(("fruit: ")+str(sumFruit))

# Ex3

# studentsData=[
#     {"name": "Bunthoeun","score": 99},
#     {"name": "Kunthy","score": 70},
#     {"name": "Sreymom","score": 95}
# ]
# studentsData = [
#                 {"name": "Bunthoeun", "score": 90}, 
#                 {"name": "Kunthy", "score": 28},
#                  {"name": "Sreymom", "score": 95}
#                 ]
# result = ""
# other = 76
# if len(studentsData)>0:
#     for i in range(len(studentsData)):
#         if studentsData[0]["score"] < studentsData[i]["score"]:
#             result=studentsData[i]["name"]
#         elif studentsData[0]["score"] > studentsData[i]["score"]:
#             other=studentsData[i]["score"]   
#     if other<75:
#         print("The best student is "+ result)
#     else:
#         print("The best student is "+studentsData[i]["name"] )
#         print("All students have more than 75")
# else: 
#     print("No result")

  


#Ex4


# studentsDic1 = {"2021A": 20, "2021B": 30, "2021C": 15 }
# studentsDic2 = {"2021A": 15, "2021C": 10, "2021D": 99 }
# for key in studentsDic2:
#     if key in studentsDic1: 
#         studentsDic1[key]+=studentsDic2[key]
#     else:
#         studentsDic1[key]=studentsDic2[key]
# print(studentsDic1)

