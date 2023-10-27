# EX1
# dic={"2022A": 20, "2022B": 30, "2022C": 15}
# if dic=={}:# Or len(dic)==0:
#     print("no class")
# else:
#     for key in dic:
#         print("Class "+key + " has "+str(dic[key]) +" students")

# EX2
# dic=[
#     {"name": 'Computer', "quantity": 20, "retail_price": 400, "quality": 'Good'},
# 	{"name": 'Computer', "quantity": 10, "retail_price": 200, "quality": 'Not good'},
# 	{"name": 'Monitor', "quantity": 20, "retail_price": 1000, "quality": 'Not good'},
# 	{"name": 'Keyboard', "quantity": 10, "retail_price": 150, "quality": 'Good'},
# 	{"name": 'Speaker', "quantity": 5, "retail_price": 50, "quality": 'Good'}
# ]
# sum=0
# for key in dic:
#     if key["quality"]=="Good":
#         sum+=key["retail_price"]
# print(sum)
  
# EX3

dic=[
{"name":'HIM', "lass":'A', "core":90},
{"name":'Bopha', "lass":'A', "core":40},
{"name":'Tesla', "lass":'A', "core":80},
{"name":'Kunthea', "lass":'B', "core":100},
{"name":'Kolap', "lass":'B', "core":50},
{"name":'Vanna', "lass":'B', "core":70},
{"name":'Chompey', "lass":'C', "core":30},
{"name":'Romchong', "lass":'C', "core":90},
]
word=str(input()) #A B C
maxn=""
mn=0
iStrue=False
for key in dic:
    if word==key["lass"] and not iStrue:
        mn=key["core"]
        iStrue=True
        maxn=key["name"]
    elif word==key["lass"]:
        if key["core"]<mn:
            mn=key["core"]
            maxn=key["name"]
print(maxn)
# tip2
# def findName(array2D):
#     word=str(input()).upper()
#     maxn=""
#     mn=0
#     iStrue=False
#     for key in array2D:
#         if word==key["lass"]:
#             if not iStrue:
#                 mn=key["core"]
#                 iStrue=True
#                 maxn=key["name"]
#             elif key["core"]<mn:
#                 mn=key["core"]
#                 maxn=key["name"]
#     return maxn
# array2D=[
# {"name":'HIM', "lass":'A', "core":90},
# {"name":'Bopha', "lass":'A', "core":40},
# {"name":'Tesla', "lass":'A', "core":80},
# {"name":'Kunthea', "lass":'B', "core":100},
# {"name":'Kolap', "lass":'B', "core":50},
# {"name":'Vanna', "lass":'B', "core":70},
# {"name":'Chompey', "lass":'C', "core":30},
# {"name":'Romchong', "lass":'C', "core":90},
# ]
# print(findName(array2D))
