
arrayDic=[
 {'name': 'Nit', 'subject': 'Algorithm', 'score': 70},
 {'name': 'Visal', 'subject': 'PL', 'score': 90},
 {'name': 'Dyna', 'subject': 'Algorithm', 'score': 99},
 {'name': 'Virak','subject': 'English', 'score': 90},
 {'name': 'Sreymom', 'subject': 'Algorithm', 'score': 90},
 {'name': 'Khid', 'subject': 'Algorithm', 'score': 80},
]
countName=""
sum=0
for i in arrayDic:
    if i["subject"] == "Algorithm":
        if i['score']<50:
            countName+=(i["name"])+" "
            sum+=1
if sum==0:
    print(str(sum)+" "+str("student failed algorithm ")+str(countName))
elif sum>=2:
    print(str(sum)+" "+str("students failed algorithm: ")+str(countName))
else:
    print(str(sum)+" "+str("students failed algorithm: ")+str(countName))
