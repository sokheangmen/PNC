list_student=[
 {"name": "Bunthoeun","score": 90},
{"name": "Kunthy","score": 75},
 {"name": "Sreymom","score": 95}
]
best_student="Best student is "
result_studen="no result"
for i in range (len(list_student)):
    if list_student[i]['score']>75:
        best_student=list_student[i]['name']
    if list_student[i]['score']>75:
        result_studen="All student have more than 75"
print(best_student)
print(result_studen)

