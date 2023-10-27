
# def sumrowcol(number):
#     # position=[] 
#     result=[]
#     for row in range(len(number)): 
#         fist=[]
#         for col in range(len(number[row])):
#             if number[row][col]==1:
#                 change=0
#             else:
#                 change=1
#             fist.append(change)
#         result.append(fist)
#     return result
# number=[
# [0,0,0]
# ,[0,0,0],
# [0,1,0],
# [0,0,0]]
# print(sumrowcol(number))

# a=[1,2,3]
# print(a[1])

# a={ "cambodia": 17, "thailand" : 30, "france" : 45 }
# print(a["thailand"] )


# countries = { 
# "khmer": 17, 
# "thai" : 30, 
# "vietnam": 50 
# }
# for key in countries:
#     print(countries[key])



# add

# studentAge={}
# studentAge["A"]=20
# studentAge["B"]=25
# print(studentAge)


menu =  {}
menu["SUNDAY"] = "rice"
menu["TUESDAY"] = "noodles"
menu["MONDAY"] = "soup"
# for i in menu:
print(menu.pop("SUNDAY"))
