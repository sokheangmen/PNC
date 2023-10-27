
# 1 - We create the list of topics
topics = [
  {"name": "java", "teacher-id": 32, "country": "Philippines"},
  {"name": "java", "teacher-id": 33, "country": "Philippines"},
  {"name": "html", "teacher-id": 30, "country": "Cambodia"},
  {"name": "java", "teacher-id": 31, "country": "Cambodia"},
]
    
# 2 - We create the list of teachers
teachers = [	
  {"teacher-id": 30, "first-name": "Him", "last-name": "Hey"},
  {"teacher-id": 31, "first-name": "Ronan", "last-name": "Ogor"},
  {"teacher-id": 32, "first-name": "Gran", "last-name": "Sabandal"},
  {"teacher-id": 33, "first-name": "Christian", "last-name": "Mediola"},
]
 

results = []
teachersId = []
for key in topics:
  if key["name"] == "java" and key['country'] == "Philippines":
    teachersId .append(key["teacher-id"]) 
for teach in teachers:
  for teacher in range(len(teachersId)):
    if (teachersId[teacher] == teach["teacher-id"]):
      results.append(teach['first-name'])
print(results)
