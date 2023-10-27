studentRecord = [
    {"studentName":"Seyla",'class':"wep-a","algorithm":98,"html":90},
    {"studentName":"seyha",'class':"wep-b","algorithm":80,"html":90},
    {"studentName":"Villa",'class':" wep-a","algorithm":96,"html":92},
    {"studentName":"mengheang",'class' :"wep-a","algorithm":66,"html":54},
]
average=0
web_A=0
sum=0
for i in range(len(studentRecord)):
    if studentRecord[i]['class']=='wep-a':
        web_A+=1
        sum+=studentRecord[i]['algorithm']
average=sum/web_A
print(average)
