# EX1
# studentsDictionary = {"2021A":20,"2021B":30,"2021":15}
# newStudentsNumber= 13
# newStudentsClass = "2021D" 

# if newStudentsClass in studentsDictionary:
#     studentsDictionary[newStudentsClass]+=newStudentsNumber
# else:
#     studentsDictionary[newStudentsClass]=newStudentsNumber
# for key in studentsDictionary:
#     print(str("Class ")+ key +str( " has ")+str(studentsDictionary[key])+str(" students"))

# EX2

# array=['rady', 'ronan', 'seiha', 'him'] 
# dic = {}
# for i in range(len(array)):
#     name = array[i]
#     dic[name] = i
# print(dic)

# EX3
# # dic={"Samnag":25, "Seiha":10} 
# if dic == {}:
#     print("no teacher")
# else:
#     sum=0
#     for key in dic:
#         sum+=dic[key]
#     print(sum/len(dic))

# database = [
# {"name":"Seyla","class":"2023B", "results" : { "algorithm":98, "html":90, "js":45 } },
# {"name":"Rady","class":"2023B", "results" : { "algorithm":41, "html":90, "js":69 } },
# {"name":"Ronan","class":"2023B", "results" : { "algorithm":78, "html":74, "js":45 } },
# {"name":"Mengheang","class":"2023B", "results" : { "algorithm":86, "html":90, "js":14 } },
# ]
# totalScore=0
# for dic in database:
#     if dic["name"]=="Rady":
#         totalScore+=(dic["results"]["html"])
#         totalScore+=(dic["results"]["js"])
#         totalScore+=(dic["results"]["algorithm"])
# print(totalScore)




# sampleDict = {"class":
#                     {"student":
#                             {"name":"Mike","marks":
#                                                 {"physics":70,"history":80
#                                                 }
#                             }
#                     }
#             }
# print(sampleDict["class"]["student"]["marks"]["physics"])


# x = ['a','b',
#             {'foo': 1,'bar':
#                         {'x' : 10,'y' : 20,'z' : 30}
#                         ,'baz': 3},'c','d']
# print(x[2]["bar"]["z"])


# number=[1, 5, 9, 25, 21] 
# numStart=0
# numAfter=0
# for num in number:
#     if numStart>numAfter:
#         numAfter=numStart
# print(numAfter)

# dictionary = {1:"Student",
# "Name":"Waqar Khan",
# "age":"23 years old",
# "Nam": "Yes",
# "Object":"Computer"}

# x = dictionary.pop("Object")
# print(x)
# print (dictionary)




# def sumNumber2By2(number):
#     for num in range(len(number)):
        
# number=[1,2,3,5]
# sum=0
# for i in number:
#     sum+=i
# print(sum)

# def append_sum(lst):
#   for last2 in lst:
#     lst.append(lst[-1] + lst[-2])
#     if len(lst) == 6:
#       return lst

# #Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))






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
print("First Name:",(getFirstName(text)))
# def getLastName(text):
#     isFound=True
#     result=""
#     for i in range(len(text)):
#         if text[i]==";" and isFound:
#             result=""
#         elif text[i]!=";" and isFound:
#             result+=text[i]
#     return result
# text="ronan;ogor"
# print("Last Name: ",(getLastName(text)))