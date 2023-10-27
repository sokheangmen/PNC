# EX1

# dic={"2022A": 20, "2022B": 30, "2022C": 15}
# if len(dic)==0:
#     print("No class")
# else:
#     for key in dic:
#         print("Class "+key + "has "+ str(dic[key]) +" students")

# EXT2


# materials = [
# 	{"name": 'Computer', "quantity": 20, "retail_price": 400, "quality": 'Good'},
# 	{"name": 'Computer', "quantity": 10, "retail_price": 200, "quality": 'Not good'},
# 	{"name": 'Monitor', "quantity": 20, "retail_price": 1000, "quality": 'Not good'},
# 	{"name": 'Keyboard', "quantity": 10, "retail_price": 150, "quality": 'Good'},
# 	{"name": 'Speaker', "quantity": 5, "retail_price": 50, "quality": 'Good'}
# ]
# sum=0
# for arr in materials:
#     if arr["quality"]=="Good":
#         sum+=arr["retail_price"]
# print(sum)

# Ex3


# dic=["rady","hello","hi"]
# result={}
# for key in range(len(dic)):
#     name= dic[key]
#     result[name]=key
# print(result)

# Ex4


# dic={}
# result=0
# if len(dic)<=0:
#     print("no")
# else:
#     for key in dic:
#         result+=dic[key]
#     print(result/len(dic))

# Ex5
# arrayDic=[{
# "name": "banana",
# "price": 1000,
# "quantity": 2,
# },{
# "name": "mango",
# "price": 2000,
# "quantity": 1,
# }]
# result=0
# for dic in arrayDic:
#     result+=dic["price"]*dic["quantity"]
# print(result)
# Ex6
# array=eval(input("enter array: "))
# sum=0
# newArray=[]
# for i in range(len(array)):
#     sum+=array[i]+array[i]
#     newArray.append(sum)
#     sum=0
# print(newArray)


# Ex7
def getFirstName(text):
    isFound=True
    result=""
    for i in range(len(text)):
        if text[i]!=";" and isFound:
            result+=text[i]
        elif text[i]==";" and isFound:
            isFound=False
    return result
text="ronan;ogor"
# print("First Name:",(getFirstName(text)))
# print("First Name: "+getFirstName(text))
def getLastName(text):
    isFound=True
    result=""
    for i in range(len(text)):
        if text[i]==";" and isFound:
            result=""
        elif text[i]!=";" and isFound:
            result+=text[i]
    return result
text="ronan;ogor"
print("Last Name: ",(getLastName(text)))