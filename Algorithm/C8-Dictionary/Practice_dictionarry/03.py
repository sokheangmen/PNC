students = [
    {'name':'HIM', 'class':'A', 'score':90},
    {'name':'Bopha', 'class':'A', 'score':70},
    {'name':'Tesla', 'class':'A', 'score':80},
    {'name':'Kunthea', 'class':'B', 'score':100},
    {'name':'Kolap', 'class':'B', 'score':90},
    {'name':'Vanna', 'class':'B', 'score':50},
    {'name':'Chompey', 'class':'C', 'score':40},
    {'name':'Romchong', 'class':'C', 'score':90},
]
Class=input("input here")
student_file="No One File"
for i in range (len(students)):
    if students[i]['class']==Class:
        if students[i]['score']<50:
            student_file=students[i]['name']
print(student_file)
        
        
