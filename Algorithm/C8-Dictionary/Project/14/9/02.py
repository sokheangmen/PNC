list_food=[  
{'fruit': 'banana', 'qty': 10, 'price': 100},
{'fruit': 'coconut', 'qty': 5, 'price': 10},
{'fruit': 'mango', 'qty': 12, 'price': 30},
{'meat': 'bird', 'qty': 1, 'price': 60},
{'meat': 'fish', 'qty': 3, 'price': 30},
]
count_fruit=0
count_meat=0
for name in list_food:
    for fruit_and_meat in name:
        if fruit_and_meat=='fruit':
            count_fruit+=1
        if fruit_and_meat=='meat':
             count_meat+=1 
print("fruit:"+str(count_fruit))
print("meat:"+str(count_meat))
