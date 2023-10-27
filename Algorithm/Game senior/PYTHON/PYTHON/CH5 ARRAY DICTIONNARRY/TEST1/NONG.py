# food={
#     "name":"bay char",
#     "price":"100$"
# }
### loob by key###
# for key in food:
#     print(key)
### loob by value#
# for key in food:
#     print(food[key])
##########################
# food={
#     "1":"hello world"
# }
# for key in food:
#     print(food[key])
##########################
array=[ 
        {"student":"A","class":"B","AGO":50,"HTML":90},
        {"student":"B","class":"A","AGO":50,"HTML":80},
        {"student":"C","class":"B","AGO":50,"HTML":70},
        {"student":"D","class":"B","AGO":50,"HTML":60},
        {"student":"F","class":"A","AGO":50,"HTML":50}
    ]
sumAGO=0
# sumHT=0
coun=0
for key in array:
    sumAGO+=key["AGO"]
    # sumHT+=key["HTML"]
    coun+=1
print(sumAGO/coun)
# print(sumHT/coun)

# sumA=0
# sumH0=0
# for dic in array:
#     for key in dic:
#         if key=="AGO":
#             sumA+=dic[key] 
# frut=[{"name":"mango"},{"name":"mango"}]
# print(frut[1]["mango"])