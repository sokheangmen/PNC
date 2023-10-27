# arrayDic1=[
# {"subject": "html", "class": "WEP-B", "teacher-id": 45},
# {"subject": "algorithm", "class": "WEP-A", "teacher-id": 68},
# {"subject": "algorithm", "class": "WEP-B", "teacher-id": 39},
# ]
# arrayDic2=[
# {"teacher-id": "39", "first-name": "Mengheang", "last-name": "Pho"},
# {"teacher-id": "45", "first-name": "ronan", "last-name": "the best"},
# {"teacher-id": "68", "first-name": "him", "last-name": "Hey"},
# ]
# name=""
# id=""
# sum=0
# for key1 in arrayDic1:
#     if key1["subject"]=="algorithm":
#         sum+=1
#         id = str(key1["teacher-id"])
#         for key2 in arrayDic2:
#             if id == key2["teacher-id"]:
#                 name+=key2["last-name"]+" "
# if sum==0:
#     print("No teacher")
# else:
#     print(name)
