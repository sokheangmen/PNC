studentsDictionary = {"2021A": 20, "2021B": 30, "2021C": 15 }
newStudentsNumber= 4
newStudentsClass = "2021A"
student =""
for key in studentsDictionary:
    if key == newStudentsClass:
        studentsDictionary[key]+=newStudentsNumber
    student+="Class " + key +" has " + str(studentsDictionary[key]) +" students" +"\n"

print(student)

# ===================3
# studentsDictionary = eval(input())

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# nameOfclass =""
# for key in studentsDictionary:
#     nameOfclass +="Class " + key +" has " + str(studentsDictionary[key]) +" students" +"\n"
# print(nameOfclass)
# -----------------------------4
# name=eval(input())
# dictionary ={}
# for i in range(len(name)):
#     dictionary[name[i]]=i
# print(dictionary)


# ---------------nu2

# studentsDic1 = {"2021A": 20, "2021B": 30, "2021C": 15}
# studentsDic2 = {"2021B": 70, "2021A": 7, "2021D": 15}

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# allDis={}
# for key in studentsDic1:
#     if key in studentsDic2:
#         studentsDic2[key] += studentsDic1[key]
# studentsDic1.update(studentsDic2)
# print(studentsDic1)