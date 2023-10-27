# number01=eval(input())
# number02=eval(input())
# remove1=[]
# remove2=[]
# for i in range(len(number01)and len(number02)):
#     if number01[i]%2==0:
#         remove1.append(number01[i])
#     if number02[i]%2==1:
#         remove2.append(number02[i])
# print(remove1)
# print(remove2)

mytext=input()
result=0
for i in range(len(mytext)):
    if mytext[i]=="A":
        result+=5
    if mytext[i]=="a":
        result+=10
    else:
        result+=1
    sum=result+result
print(result)