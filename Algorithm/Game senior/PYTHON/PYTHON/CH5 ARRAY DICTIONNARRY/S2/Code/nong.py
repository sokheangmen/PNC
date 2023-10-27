#########################################EX1
# def countsTheQuantity(quantity):
#     sum=0
#     for key in quantity:
#         sum+=quantity[key]
#     return sum
# dic={"Mango":7,"Orange":3,"Banan":1}
# print(countsTheQuantity(dic))

#########################################EX2

def countsTheQuantity(quantity):
    sum=0
    for key in quantity:
        sum+=key["quantity"]
    return sum
dic=[{"Name":"Banana","quantity":16},
    {"Name":"Banana","quantity":4},
    {"Name":"Banana","quantity":20}]
print(countsTheQuantity(dic))


#########################################EX2

# def countsTheQuantity(quantity):
#     sum=0
#     for key in quantity:
#         sum+=key["quantity"]
#     return sum
# dic=[{"Name":"Banana","quantity":16},
#     {"Name":"Orange","quantity":4},
#     {"Name":"Apple","quantity":20}]
# print(countsTheQuantity(dic))
#########################################EX3

# def positive(fruit):
#     result=""
#     for dic in fruit:
#         if dic["quantity"]>0:
#             result+=dic["name"]+"\n"
#     return result [:-1] #ដកspack
# fruit=[{"name":"Banana","quantity":16},
#     {"name":"Orange","quantity":0},
#     {"name":"Apple","quantity":20}]
# print(positive(fruit))

# ########################################EX4
# def sumOFFruit(fruitName):
#     sum=0
#     result=0
#     for dic in fruitName:
#             result=dic["quantity"]*dic["price"]
#             sum+=result
#     return sum
# fruitName=[{'name' : 'Banana', 'quantity':3,'price':10},
#     {'name' : 'Orange', 'quantity':4,'price':14}]
# print(sumOFFruit(fruitName))
#########################################EX5

# def findRowAndCol(array2D):
#     postition=[]
#     countRow=0
#     for row in range(len(array2D)):
#         countCol=0
#         for col in range(len(array2D[row])):
#             countCol+=1
#         countRow+=1
#     if countCol==countRow:
#         postition.append(countRow)
#     else:
#         postition.append(countRow)
#         postition.append(countCol)
#     return postition
# array2D=[[0,0,0],
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]]
# print(findRowAndCol(array2D))
#########################################EX6
# def findRowAndCol(array2D):
#     postition=[]
#     for row in range(len(array2D)):
#         for col in range(len(array2D[row])):
#             if array2D[row][col]==1:
#                 postition.append(row)
#                 postition.append(col)
#     return postition
# array2D=[[0,0,0,0,0],
#         [0,0,0,1,0]]            
# print(findRowAndCol(array2D))

#########################################EX7
# def findRowAndCol(array2D):
#     newarray=[]
#     for row in range(len(array2D)):
#         resultInRow=[]
#         for col in range(len(array2D[row])):
#             if array2D[row][col]==1:
#                 result=0
#             else:
#                 result=1  
#             resultInRow.append(result)
#         newarray.append(resultInRow)    
#     return newarray
# array2D=[[0,0,1,0,0],
#         [0,0,0,1,0]]  
# print(findRowAndCol(array2D))
          
