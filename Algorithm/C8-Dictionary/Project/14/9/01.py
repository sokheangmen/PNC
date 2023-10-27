fruit=[
    {"name": "banana","price": 1000,"quantity": 2,},
    {"name": "mango","price": 2000,"quantity": 1,}, 
]
result=0
for i in range(len(fruit)):
    result+=fruit[i]['price']*fruit[i]['quantity']
print(result)
