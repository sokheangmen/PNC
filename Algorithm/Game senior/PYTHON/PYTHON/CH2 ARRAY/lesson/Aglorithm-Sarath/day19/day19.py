# --------------------num1--------------

# allNameOfPer= {'Him':21, 'Rady': 25, 'Ronan':30, 'Clement': 22, 'Edoure':22}
# sum = 0
# if len(allNameOfPer)>0:
#     for key in allNameOfPer:
#         sum += allNameOfPer[key]
#     aver = str(sum/len(allNameOfPer))
# else:
#     aver ="No teacher here!"
# print(aver)

# --------------------num2----------------------

# arrayDis=[{'fruit': 'banana', 'qty': 10, 'price': 100}, {'meat': 'bird', 'qty': 1, 'price': 60}, {'meat': 'fish', 'qty': 3, 'price': 30}]
# fruit = 0
# meat =0
# for i in arrayDis:     
#     for key in i:
#         if key == 'fruit':
#             fruit+=1
#         elif key =='meat':
#             meat +=1
# print("Fruit:"+str(fruit))
# print("Meat:"+str(meat))

# ---------------------num3-----------------
# def getMax(arr):
#     # Write your code here
#     maxNum= arr[0]
#     for i in range(len(arr)):
#          if arr[i]>maxNum:
#            maxNum= arr[i]
#     result['max']=maxNum
#     return maxNum

# def getMin(arr):
#     # Write your code here
#     minNum= arr[0]
#     for i in range(len(arr)):
#          if arr[i]<minNum:
#            minNum = arr[i]
#     result['min']=minNum
#     return minNum
# def getAvg(arr):
#     # Write your code here
#     sumNum= 0
#     averNum =0
#     for i in range(len(arr)):
#         sumNum += arr[i]
#     averNum+= sumNum//len(listOfNumber)
#     result['avg']=averNum
#     return averNum
    
# # your input here
# result = {}
# listOfNumber = eval(input())
# getMax(listOfNumber)
# getMin(listOfNumber)
# getAvg(listOfNumber)
# print(result)


# ----------------------------------number4
# studentsData = [{"name": "Bunthoeun", "score": 90}, {"name": "Kunthy", "score": 35}, {"name": "Sreymom", "score": 95}]
# # studentsData[2]= 0
# studentsData = eval(input())
# result =""
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



# =========================ho
grid = [[0,0,0,0,0,0],['D',0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0,0,0,0,0,0]]
text ="R"
for row in range(len(grid)):
    for col in range(row):
        if grid[row][col]=="D" and text=="R":
            grid[row][col]= 0
            grid[row][col+1] ="D"
        if grid[row][col]=="D" and text=="L":
            grid[row][col]= 0
            grid[row][col-1] ="D"
        if grid[row][col]=="D" and text=="U":
            grid[row][col]= 0
            grid[row+1][col] ="D"
        if grid[row][col]=="D" and text=="D":
            grid[row][col]= 0
            grid[row-1][col] ="D"
print(grid)







